"""Grading suite for Chapter 5 — Reading What Arrives.

Every expected output here was produced by executing a reference solution.

**What changed in this suite, and why.** Chapter 4's grader ran every exercise
against a second dataset and still caught none of the six defects the review
found. Two of those misses were design errors rather than bad luck: the mutated
data preserved the very structural property each bug was leaning on. The aisle
bug counted matching pairs instead of distinct values and survived because every
aisle in *both* datasets appeared exactly twice, making pairs and distinct
coincide.

So the rule for this suite is stricter: **a mutation must break a structural
property of the sample data, not merely change its values.** Where the sample
has even counts, the mutation has uneven ones. Where the sample always finds a
match, the mutation finds none. Where the sample always has a separator, the
mutation has none at all. Each mutation records which property it breaks.
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

# String methods that exist but are deliberately held back, because each one
# would hand over the answer to an exercise built to make you derive it.
UNTAUGHT_METHODS = {
    "rfind": "search backwards from the end yourself — Ch.5 Ex.4 is that exercise",
    "rindex": "as rfind",
    "rsplit": "as rfind",
    "partition": "not taught — use split with a count",
    "rpartition": "not taught — use split with a count",
    "splitlines": "not taught",
    "removeprefix": "not taught — use slicing or startswith",
    "removesuffix": "not taught — use slicing or endswith",
    "index": "returns only the first match and raises on absence — use find",
}

COMPREHENSION = re.compile(r"\[[^\[\]]*\bfor\b[^\[\]]*\]")
BLOCK = "{}\\s*=\\s*\\(.*?^\\)"


def code_only(src, keep_strings=False):
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
    src = source_of(name)
    for kind, target, replacement in edits:
        if kind == "block":
            pattern = re.compile(BLOCK.format(re.escape(target)), re.M | re.S)
            if not pattern.search(src):
                pytest.fail(
                    f"{name}: could not find a `{target} = ( ... )` assignment to "
                    f"substitute. Keep the given data in a variable of that name."
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
        f"The property this mutation breaks: {why}\n\n"
        f"--- expected ---\n" + "\n".join(expected) +
        f"\n\n--- actual ---\n" + "\n".join(actual)
    )


def assert_only_taught(name):
    code = code_only(source_of(name))
    for keyword, why in UNTAUGHT_KEYWORDS.items():
        assert not re.search(rf"\b{keyword}\b", code), f"{name}: `{keyword}` — {why}"
    for call, why in UNTAUGHT_CALLS.items():
        assert not re.search(rf"\b{call}\s*\(", code), f"{name}: `{call}()` — {why}"
    for method, why in UNTAUGHT_METHODS.items():
        assert not re.search(rf"\.{method}\s*\(", code), f"{name}: `.{method}()` — {why}"
    assert not COMPREHENSION.search(code), (
        f"{name}: comprehension used — write the loop"
    )


# ── Exercise 1 — A supplier feed that has been through several hands 

EX1_EXPECTED = [
    "ACCEPTED (3)",
    "  SKU-301   Blue Mug      12    4.99     59.88",
    "  SKU-302   Red Mug       40    5.49    219.60",
    "  SKU-306   White Mug      5   12.75     63.75",
    "REJECTED (3)",
    "  SKU-303                     quantity is not a number",
    "  SKU-304|Yellow Mug|7        expected 4 fields, found 3",
    "  SKU-305                     out of stock",
    "--------------------------------------------",
    "6 lines   3 accepted   3 rejected   value 343.23"
]

EX1_MUTATED = [
    "ACCEPTED (0)",
    "  none",
    "REJECTED (3)",
    "  SKU-301|Blue Mug|12         expected 4 fields, found 3",
    "  SKU-302|Red Mug             expected 4 fields, found 2",
    "  SKU-303|Green Mug|abc|3.10|extraexpected 4 fields, found 5",
    "--------------------------------------------",
    "3 lines   0 accepted   3 rejected   value 0.00"
]

EX1_EDITS = [
    [
        "block",
        "feed",
        "(\n    \"SKU-301|Blue Mug|12\",\n    \"SKU-302|Red Mug\",\n    \"SKU-303|Green Mug|abc|3.10|extra\",\n)"
    ]
]

EX1_WHY = "every line is malformed \u2014 the accepted list stays empty, and any total computed only inside the accepted branch is exposed"


def test_ex1_output():
    assert_output("ex1.py", EX1_EXPECTED)


def test_ex1_on_other_data():
    assert_mutated_output("ex1.py", EX1_EDITS, EX1_MUTATED, EX1_WHY)


def test_ex1_only_taught():
    assert_only_taught("ex1.py")


# ── Exercise 2 — Triaging a log ──────────────────────────

EX2_EXPECTED = [
    "ERROR ENTRIES (2)",
    "  09:15:31  payment gateway timeout for ORD-8102",
    "  09:17:45  payment gateway timeout for ORD-8103",
    "BY LEVEL",
    "  INFO    2",
    "  WARN    2",
    "  ERROR   2",
    "----------------------------------------",
    "6 lines   3 levels   2 error"
]

EX2_MUTATED = [
    "FATAL ENTRIES (0)",
    "  none",
    "BY LEVEL",
    "  INFO    4",
    "  WARN    1",
    "  DEBUG   1",
    "----------------------------------------",
    "6 lines   3 levels   0 fatal"
]

EX2_EDITS = [
    [
        "text",
        "LEVEL = \"ERROR\"",
        "LEVEL = \"FATAL\""
    ],
    [
        "block",
        "log",
        "(\n    \"2026-09-01 09:14:02 INFO  checkout completed for ORD-8101\",\n    \"2026-09-01 09:14:07 INFO  cart updated\",\n    \"2026-09-01 09:15:31 INFO  session opened\",\n    \"2026-09-01 09:16:00 INFO  cart updated again\",\n    \"2026-09-01 09:17:45 WARN  slow query on /product took 940ms\",\n    \"2026-09-01 09:18:12 DEBUG cache warm\",\n)"
    ]
]

EX2_WHY = "counts are 4/1/1 rather than the sample's even 2/2/2, and no line matches the level \u2014 anything counting pairs instead of distinct values, or assuming a match exists, breaks here"


def test_ex2_output():
    assert_output("ex2.py", EX2_EXPECTED)


def test_ex2_on_other_data():
    assert_mutated_output("ex2.py", EX2_EDITS, EX2_MUTATED, EX2_WHY)


def test_ex2_only_taught():
    assert_only_taught("ex2.py")


# ── Exercise 3 — Deduplicating messy signups ─────────────

EX3_EXPECTED = [
    "KEPT (4)",
    "1. Ada Lovelace        ada@shop.co",
    "2. Grace Hopper        grace@shop.co",
    "3. Alan Turing         alan@shop.co",
    "4. Katherine Johnson   katherine@shop.co",
    "DUPLICATES",
    "  line 2: ada lovelace already signed up as ada@shop.co",
    "  line 4: Grace Hopper already signed up as grace@shop.co",
    "----------------------------------------------",
    "6 signups   4 unique   2 duplicate"
]

EX3_MUTATED = [
    "KEPT (2)",
    "1. Ada Lovelace        ada@shop.co",
    "2. Grace Hopper        grace@shop.co",
    "DUPLICATES",
    "  line 2: Alan Turing no-brackets-here already signed up as malformed",
    "----------------------------------------------",
    "3 signups   2 unique   1 duplicate"
]

EX3_EDITS = [
    [
        "block",
        "signups",
        "(\n    \"Ada Lovelace <ada@shop.co>\",\n    \"Grace Hopper <grace@shop.co>\",\n    \"Alan Turing no-brackets-here\",\n)"
    ]
]

EX3_WHY = "no duplicates at all, and one entry is malformed \u2014 both the empty branch and the malformed branch fire"


def test_ex3_output():
    assert_output("ex3.py", EX3_EXPECTED)


def test_ex3_on_other_data():
    assert_mutated_output("ex3.py", EX3_EDITS, EX3_MUTATED, EX3_WHY)


def test_ex3_only_taught():
    assert_only_taught("ex3.py")


# ── Exercise 4 — Splitting on the last separator ─────────

EX4_EXPECTED = [
    "PARSED (4)",
    "  reports/2026/september            stock         csv",
    "  .                                 stock         csv",
    "  reports/                          stock         csv",
    "  reports/2026/september/archive    old.stock     csv",
    "ODD",
    "  reports/2026/                     no filename",
    "----------------------------------------------------",
    "5 paths   4 parsed   1 odd"
]

EX4_MUTATED = [
    "PARSED (2)",
    "  .                                 stock         csv",
    "  .                                 notes         txt",
    "ODD",
    "  README                            no extension",
    "----------------------------------------------------",
    "3 paths   2 parsed   1 odd"
]

EX4_EDITS = [
    [
        "block",
        "paths",
        "(\n    \"stock.csv\",\n    \"notes.txt\",\n    \"README\",\n)"
    ]
]

EX4_WHY = "no path contains a separator, so the folder is empty for every row \u2014 any code assuming a slash exists breaks"


def test_ex4_output():
    assert_output("ex4.py", EX4_EXPECTED)


def test_ex4_on_other_data():
    assert_mutated_output("ex4.py", EX4_EDITS, EX4_MUTATED, EX4_WHY)


def test_ex4_only_taught():
    assert_only_taught("ex4.py")


# ── Exercise 5 — Building the export ─────────────────────

EX5_EXPECTED = [
    "EXPORT",
    "  sku|name|qty|price",
    "  SKU-301|Blue Mug|12|4.99",
    "  SKU-302|Red Mug|40|5.49",
    "  SKU-306|White Mug|5|12.75",
    "WIDTHS",
    "  sku     7",
    "  name    9",
    "  qty     3",
    "  price   5",
    "----------------------------------------",
    "4 lines   4 columns   90 characters"
]

EX5_MUTATED = [
    "EXPORT",
    "  sku|name|qty|price",
    "  A|B|1|2.00",
    "WIDTHS",
    "  sku     3",
    "  name    4",
    "  qty     3",
    "  price   5",
    "----------------------------------------",
    "2 lines   4 columns   28 characters"
]

EX5_EDITS = [
    [
        "block",
        "rows",
        "(\n    (\"A\", \"B\", 1, 2.0),\n)"
    ]
]

EX5_WHY = "one row only, so every column width is decided by the header rather than the data \u2014 the reverse of the sample"


def test_ex5_output():
    assert_output("ex5.py", EX5_EXPECTED)


def test_ex5_on_other_data():
    assert_mutated_output("ex5.py", EX5_EDITS, EX5_MUTATED, EX5_WHY)


def test_ex5_only_taught():
    assert_only_taught("ex5.py")


# ── Exercise 6 — The pipeline, from raw text ─────────────

EX6_EXPECTED = [
    "ACCEPTED (2)",
    "  ORD-9101  GB    1,240.00   risk  55",
    "  ORD-9103  IE      640.00   risk   0",
    "REJECTED (5)",
    "  ORD-9102                          email address is not valid",
    "  ORD-9104                          we do not ship to DE",
    "  ORD-9105                          value is not a number",
    "  ORD-9103                          duplicate order",
    "  ORD-9106|f@shop.co|GB|920.00      expected 5 fields, found 4",
    "--------------------------------------------------",
    "7 lines   2 accepted   5 rejected   banked 1,880.00"
]

EX6_MUTATED = [
    "ACCEPTED (0)",
    "  none",
    "REJECTED (5)",
    "  ORD-9101                          email address is not valid",
    "  ORD-9102                          we do not ship to US",
    "  ORD-9103                          account age is not a number",
    "  ORD-9104                          value is not a number",
    "  ORD-9105|e@shop.co|GB|100.00      expected 5 fields, found 4",
    "--------------------------------------------------",
    "5 lines   0 accepted   5 rejected   banked 0.00"
]

EX6_EDITS = [
    [
        "block",
        "feed",
        "(\n    \"ORD-9101|bad.email|GB|1240.00|3\",\n    \"ORD-9102|b@shop.co|US|200.00|400\",\n    \"ORD-9103|c@shop.co|IE|640.00|abc\",\n    \"ORD-9104|d@shop.co|GB|nope|12\",\n    \"ORD-9105|e@shop.co|GB|100.00\",\n)"
    ]
]

EX6_WHY = "every line is rejected for a different reason \u2014 the accepted list stays empty and the banked total must still be defined"


def test_ex6_output():
    assert_output("ex6.py", EX6_EXPECTED)


def test_ex6_on_other_data():
    assert_mutated_output("ex6.py", EX6_EDITS, EX6_MUTATED, EX6_WHY)


def test_ex6_only_taught():
    assert_only_taught("ex6.py")
