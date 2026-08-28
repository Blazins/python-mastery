"""Grading suite for Chapter 4 — Keeping What You Find.

Every expected output in this file was produced by executing a reference
solution, not transcribed by hand.

Three rules govern what may be checked here. The first two come from
CONTRIBUTING.md; the third is new, and is the direct result of the Chapter 3
review.

1. Tests assert behaviour, not the shape of the source. The exceptions are
   `assert_only_taught` and `assert_uses_a_list`, which enforce actual syllabus
   rules rather than stylistic preferences.
2. This suite was validated against structurally different solutions for every
   exercise before shipping.
3. **Every exercise is graded twice: once on the data it was given, and once on
   a second dataset chosen to drive execution into branches the sample data
   never reaches.** Chapters 2 and 3 shipped ten real defects between them, and
   a suite that only ever ran the sample data could not see a single one. If a
   summary line assumes the loop found something, the mutated run is where that
   assumption fails.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

SUBMISSIONS = Path(__file__).parent / "submissions"

UNTAUGHT_KEYWORDS = {
    "def": "functions arrive in a later chapter",
    "import": "modules arrive in a later chapter",
    "class": "classes arrive in a later chapter",
    "lambda": "not taught",
}

UNTAUGHT_CALLS = {
    "dict": "dictionaries arrive in the next chapter",
    "set": "sets arrive with dictionaries",
    "any": "not taught — write the loop",
    "all": "not taught — write the loop",
    "filter": "not taught — write the loop",
    "map": "not taught — write the loop",
}

COMPREHENSION = re.compile(r"\[[^\[\]]*\bfor\b[^\[\]]*\]")
SLICE = re.compile(r"\[[^\[\]]*:[^\[\]]*\]")
BLOCK = "{}\\s*=\\s*\\(.*?^\\)"


def code_only(src, keep_strings=False):
    """Source with comments (and optionally string literals) removed."""
    out = []
    for line in src.splitlines():
        code = line.split("#", 1)[0]
        if not keep_strings:
            code = re.sub(r'"[^"]*"|\'[^\']*\'', '""', code)
        out.append(code)
    return "\n".join(out)


def _execute(path, label):
    result = subprocess.run(
        [sys.executable, str(path)], capture_output=True, text=True, timeout=15
    )
    if result.returncode != 0:
        pytest.fail(
            f"{label} exited with status {result.returncode}.\n"
            f"--- stderr ---\n{result.stderr}"
        )
    lines = [line.rstrip() for line in result.stdout.splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def source_of(name):
    path = SUBMISSIONS / name
    if not path.exists():
        pytest.skip(f"{name} not submitted yet")
    return path.read_text()


def run_submission(name):
    path = SUBMISSIONS / name
    if not path.exists():
        pytest.skip(f"{name} not submitted yet")
    return _execute(path, name)


def run_mutated(name, edits):
    """Run a submission with its input data replaced.

    `edits` is a list of ("block", var, literal) or ("text", old, new). A block
    edit rewrites a whole `var = ( ... )` assignment, so it survives any
    reformatting of the data inside it — only the variable name has to match,
    and the exercise specifies that.
    """
    src = source_of(name)
    for kind, target, replacement in edits:
        if kind == "block":
            pattern = re.compile(BLOCK.format(re.escape(target)), re.M | re.S)
            if not pattern.search(src):
                pytest.fail(
                    f"{name}: could not find a `{target} = ( ... )` assignment to "
                    f"substitute. Keep the given data in a variable of that name "
                    f"so the grader can re-run your solution on other input."
                )
            src = pattern.sub(lambda m: f"{target} = {replacement}", src, count=1)
        else:
            if target not in src:
                pytest.fail(f"{name}: expected to find {target!r} in the source.")
            src = src.replace(target, replacement)

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, dir=SUBMISSIONS) as fh:
        fh.write(src)
        temp = Path(fh.name)
    try:
        return _execute(temp, f"{name} (mutated)")
    finally:
        temp.unlink()


def assert_output(name, expected):
    assert run_submission(name) == expected


def assert_mutated_output(name, edits, expected, why):
    actual = run_mutated(name, edits)
    assert actual == expected, (
        f"\n{name} is correct on its own data but wrong on other input.\n"
        f"Mutation: {why}\n\n"
        f"--- expected ---\n" + "\n".join(expected) +
        f"\n\n--- actual ---\n" + "\n".join(actual)
    )


def assert_only_taught(name):
    code = code_only(source_of(name))
    for keyword, why in UNTAUGHT_KEYWORDS.items():
        assert not re.search(rf"\b{keyword}\b", code), f"{name}: `{keyword}` — {why}"
    for call, why in UNTAUGHT_CALLS.items():
        assert not re.search(rf"\b{call}\s*\(", code), f"{name}: `{call}()` — {why}"
    assert not COMPREHENSION.search(code), (
        f"{name}: comprehension used — write the loop; comprehensions arrive after dictionaries"
    )
    assert not SLICE.search(code), (
        f"{name}: slicing used — slicing arrives in the strings chapter"
    )


def assert_uses_a_list(name):
    code = code_only(source_of(name))
    assert ".append(" in code or re.search(r"=\s*\[\s*\]", code), (
        f"{name}: no list is built. This chapter is about collecting results you "
        f"cannot count in advance — printing inside the loop is the thing it exists "
        f"to replace."
    )


# ── Exercise 1 — The returns desk at close of day ────────────

EX1_EXPECTED = [
    "RESTOCK (3)",
    "  SKU-101",
    "  SKU-104",
    "  SKU-109",
    "INSPECT (2)",
    "  SKU-107      4.38",
    "  SKU-118     15.00",
    "WRITE-OFF (2)",
    "  SKU-102     15.50",
    "  SKU-112     45.00",
    "----------------------------------------------",
    "7 returned   3 restocked   2 to inspect   60.50 lost"
]

EX1_MUTATED = [
    "RESTOCK (7)",
    "  SKU-101",
    "  SKU-102",
    "  SKU-104",
    "  SKU-107",
    "  SKU-109",
    "  SKU-112",
    "  SKU-118",
    "INSPECT (0)",
    "  none",
    "WRITE-OFF (0)",
    "  none",
    "----------------------------------------------",
    "7 returned   7 restocked   0 to inspect   0.00 lost"
]

EX1_EDITS = [
    [
        "text",
        "\"DAMAGED\"",
        "\"SEALED\""
    ],
    [
        "text",
        "\"OPENED\"",
        "\"SEALED\""
    ]
]

EX1_WHY = "nothing opened or damaged \u2014 both lists stay empty"


def test_ex1_output():
    assert_output("ex1.py", EX1_EXPECTED)


def test_ex1_on_other_data():
    assert_mutated_output("ex1.py", EX1_EDITS, EX1_MUTATED, EX1_WHY)


def test_ex1_only_taught():
    assert_only_taught("ex1.py")


def test_ex1_uses_a_list():
    assert_uses_a_list("ex1.py")


# ── Exercise 2 — A picking route in aisle order ──────────────

EX2_EXPECTED = [
    "STOP  AISLE  SHELF   SKU",
    "----------------------------------",
    "1         1      3   SKU-118",
    "2         1     15   SKU-441",
    "3         2      1   SKU-655",
    "4         2      9   SKU-207",
    "5         4      2   SKU-092",
    "6         4     12   SKU-330",
    "----------------------------------",
    "6 stops across 3 aisles"
]

EX2_MUTATED = [
    "STOP  AISLE  SHELF   SKU",
    "----------------------------------",
    "1         1      3   SKU-118",
    "2         1     15   SKU-441",
    "----------------------------------",
    "2 stops across 1 aisles"
]

EX2_EDITS = [
    [
        "block",
        "picks",
        "(\n    (\"SKU-441\", 1, 15),\n    (\"SKU-118\", 1,  3),\n)"
    ]
]

EX2_WHY = "a two-stop route inside one aisle"


def test_ex2_output():
    assert_output("ex2.py", EX2_EXPECTED)


def test_ex2_on_other_data():
    assert_mutated_output("ex2.py", EX2_EDITS, EX2_MUTATED, EX2_WHY)


def test_ex2_only_taught():
    assert_only_taught("ex2.py")


def test_ex2_uses_a_list():
    assert_uses_a_list("ex2.py")


# ── Exercise 3 — The slowest endpoints ───────────────────────

EX3_EXPECTED = [
    "REQUESTS OVER 500ms",
    "1. /search       1620ms",
    "2. /search       1180ms",
    "3. /product       940ms",
    "------------------------------",
    "7 requests   4 slow   fastest 35ms   mean 720.7ms"
]

EX3_MUTATED = [
    "REQUESTS OVER 99999ms",
    "  none",
    "------------------------------",
    "7 requests   0 slow   fastest 35ms   mean 720.7ms"
]

EX3_EDITS = [
    [
        "text",
        "SLOW = 500",
        "SLOW = 99999"
    ]
]

EX3_WHY = "no request is slow \u2014 the top-N list is empty"


def test_ex3_output():
    assert_output("ex3.py", EX3_EXPECTED)


def test_ex3_on_other_data():
    assert_mutated_output("ex3.py", EX3_EDITS, EX3_MUTATED, EX3_WHY)


def test_ex3_only_taught():
    assert_only_taught("ex3.py")


def test_ex3_uses_a_list():
    assert_uses_a_list("ex3.py")


# ── Exercise 4 — Reconciling two feeds ───────────────────────

EX4_EXPECTED = [
    "DISCREPANCIES",
    "  SKU-101      -2",
    "  SKU-109      +5",
    "  SKU-118      -5",
    "------------------------------",
    "2 short   1 over   net -2"
]

EX4_MUTATED = [
    "FEED MISMATCH: 5 expected rows, 4 counted rows",
    "DISCREPANCIES",
    "  none",
    "------------------------------",
    "0 short   0 over   net +0"
]

EX4_EDITS = [
    [
        "block",
        "counted",
        "(\n    (\"SKU-101\", 120),\n    (\"SKU-104\",  40),\n    (\"SKU-109\",  75),\n    (\"SKU-112\",  12),\n)"
    ]
]

EX4_WHY = "feeds of different lengths, and no discrepancy in the overlap"


def test_ex4_output():
    assert_output("ex4.py", EX4_EXPECTED)


def test_ex4_on_other_data():
    assert_mutated_output("ex4.py", EX4_EDITS, EX4_MUTATED, EX4_WHY)


def test_ex4_only_taught():
    assert_only_taught("ex4.py")


def test_ex4_uses_a_list():
    assert_uses_a_list("ex4.py")


# ── Exercise 5 — Deduplicating a supplier feed ───────────────

EX5_EXPECTED = [
    "UNIQUE (4)",
    "1. SKU-301",
    "2. SKU-302",
    "3. SKU-303",
    "4. SKU-304",
    "REPEATS",
    "  SKU-301 first seen at 0, again at 2",
    "  SKU-302 first seen at 1, again at 4",
    "  SKU-301 first seen at 0, again at 5",
    "----------------------------------",
    "7 rows   4 unique   3 repeats"
]

EX5_MUTATED = [
    "UNIQUE (7)",
    "1. SKU-301",
    "2. SKU-302",
    "3. SKU-305",
    "4. SKU-303",
    "5. SKU-306",
    "6. SKU-307",
    "7. SKU-304",
    "REPEATS",
    "  no duplicates",
    "----------------------------------",
    "7 rows   7 unique   0 repeats"
]

EX5_EDITS = [
    [
        "block",
        "feed",
        "(\n    \"SKU-301\", \"SKU-302\", \"SKU-305\", \"SKU-303\",\n    \"SKU-306\", \"SKU-307\", \"SKU-304\",\n)"
    ]
]

EX5_WHY = "a feed with no repeats at all"


def test_ex5_output():
    assert_output("ex5.py", EX5_EXPECTED)


def test_ex5_on_other_data():
    assert_mutated_output("ex5.py", EX5_EDITS, EX5_MUTATED, EX5_WHY)


def test_ex5_only_taught():
    assert_only_taught("ex5.py")


def test_ex5_uses_a_list():
    assert_uses_a_list("ex5.py")


# ── Exercise 6 — The pipeline, with a report ─────────────────

EX6_EXPECTED = [
    "HELD",
    "  ORD-8101  risk  70",
    "  ORD-8106  risk  65",
    "REVIEW",
    "  ORD-8105  risk  35",
    "REJECTED",
    "  ORD-8102  email address is not valid",
    "  ORD-8104  we do not ship to DE",
    "SHIPPED",
    "  ORD-8103     640.00",
    "  ORD-8107      52.95",
    "----------------------------------------------",
    "7 orders   2 shipped   1 review   2 held   2 rejected",
    "dispatched 692.95"
]

EX6_MUTATED = [
    "HELD",
    "  none",
    "REVIEW",
    "  none",
    "REJECTED",
    "  ORD-8101  email address is not valid",
    "  ORD-8102  email address is not valid",
    "  ORD-8103  we do not ship to US",
    "SHIPPED",
    "  none",
    "----------------------------------------------",
    "3 orders   0 shipped   0 review   0 held   3 rejected",
    "dispatched 0.00"
]

EX6_EDITS = [
    [
        "block",
        "orders",
        "(\n    (\"ORD-8101\", \"bad.email\", \"GB\", \"1240.00\",   3, \"GB\", None),\n    (\"ORD-8102\", \"also.bad\",  \"GB\",  \"200.00\", 400, \"GB\", \"07700900123\"),\n    (\"ORD-8103\", \"c@shop.co\", \"US\",  \"640.00\",  90, \"US\", \"07700900555\"),\n)"
    ]
]

EX6_WHY = "every order fails validation \u2014 nothing held, reviewed or shipped"


def test_ex6_output():
    assert_output("ex6.py", EX6_EXPECTED)


def test_ex6_on_other_data():
    assert_mutated_output("ex6.py", EX6_EDITS, EX6_MUTATED, EX6_WHY)


def test_ex6_only_taught():
    assert_only_taught("ex6.py")


def test_ex6_uses_a_list():
    assert_uses_a_list("ex6.py")
