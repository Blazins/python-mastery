"""Grading suite for Chapter 3 — Doing It Once for Every Order.

Every expected output in this file was produced by executing a reference
solution, not transcribed by hand.

Two rules from CONTRIBUTING.md govern what may be checked here:

1. Tests assert behaviour, not the shape of the source. The exceptions are
   `assert_only_taught` and `assert_uses_iteration`, which enforce actual
   syllabus rules rather than stylistic preferences — a submission that solves
   these by copying a block per row has not done the exercise.
2. This suite was validated against two structurally different solutions for
   every exercise (unpacking vs. indexing, `for` vs. `while`, guard clauses vs.
   nested chains) before shipping. Both pass.
"""

import re
import subprocess
import sys
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
    "sum": "write the accumulator yourself — Chapter 3 §5",
    "min": "write the accumulator yourself — Chapter 3 §5",
    "max": "write the accumulator yourself — Chapter 3 §5",
    "sorted": "sorting arrives with lists",
    "enumerate": "deferred to the lists chapter",
    "zip": "deferred to the lists chapter",
    "list": "lists arrive in the next chapter",
    "set": "sets arrive later",
    "dict": "dictionaries arrive later",
}


def code_only(src, keep_strings=False):
    """Source with comments (and optionally string literals) removed."""
    out = []
    for line in src.splitlines():
        code = line.split("#", 1)[0]
        if not keep_strings:
            code = re.sub(r'"[^"]*"|\'[^\']*\'', '""', code)
        out.append(code)
    return "\n".join(out)


def run_submission(name):
    path = SUBMISSIONS / name
    if not path.exists():
        pytest.skip(f"{name} not submitted yet")
    result = subprocess.run(
        [sys.executable, str(path)], capture_output=True, text=True, timeout=15
    )
    if result.returncode != 0:
        pytest.fail(
            f"{name} exited with status {result.returncode}.\n"
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


def assert_output(name, expected):
    actual = run_submission(name)
    if len(actual) != len(expected):
        pytest.fail(
            f"{name}: expected {len(expected)} lines, got {len(actual)}.\n"
            "--- expected ---\n" + "\n".join(expected) +
            "\n--- actual ---\n" + "\n".join(actual)
        )
    for i, (got, want) in enumerate(zip(actual, expected), start=1):
        assert got == want, (
            f"{name}: line {i} differs.\n"
            f"  expected: {want!r}\n"
            f"  actual:   {got!r}"
        )


def assert_only_taught(name):
    """Chapters 1-3: loops, tuples and indexing are in; everything else is not."""
    src = code_only(source_of(name))
    for line in src.splitlines():
        for kw, why in UNTAUGHT_KEYWORDS.items():
            if re.search(rf"(?<![\w.]){kw}\b", line):
                pytest.fail(
                    f"{name}: uses `{kw}`, which has not been taught yet ({why}).\n"
                    f"  {line.strip()!r}"
                )
        for fn, why in UNTAUGHT_CALLS.items():
            if re.search(rf"(?<![\w.]){fn}\s*\(", line):
                pytest.fail(
                    f"{name}: calls `{fn}()`, which has not been taught yet ({why}).\n"
                    f"  {line.strip()!r}"
                )
        if re.search(r"\.\s*[A-Za-z_]\w*\s*\(", line):
            pytest.fail(
                f"{name}: calls a method. No method or attribute access has been "
                "taught yet — string methods such as `.split()` and `.strip()` "
                "arrive in the strings chapter.\n"
                f"  {line.strip()!r}"
            )
        # `[` is a subscript when something precedes it, and a list literal
        # otherwise. Indexing is taught (§1, §6); lists are not.
        for m in re.finditer(r"\[", line):
            before = line[:m.start()].rstrip()
            if not before or before[-1] not in "_)]" and not before[-1].isalnum():
                pytest.fail(
                    f"{name}: uses a list literal `[...]`. Lists arrive in the next "
                    "chapter — a tuple `(...)` is what this chapter taught.\n"
                    f"  {line.strip()!r}"
                )


def assert_uses_iteration(name):
    """The whole point of the chapter: one block, not one block per row."""
    src = code_only(source_of(name))
    if not re.search(r"(?<![\w.])(for|while)\b", src):
        pytest.fail(
            f"{name}: contains no loop. These exercises are solvable by copying a "
            "block per row, and that is exactly the habit Chapter 3 exists to end "
            "— the Chapter 2 review found four defects caused by it. Write the "
            "block once and iterate."
        )


# ── Exercise 1 ───────────────────────────────────────────────────────────

EX1_EXPECTED = [
    'ORDER          GOODS  BAND         SHIP      TOTAL',
    '--------------------------------------------------',
    'ORD-1101      642.50  FREE         0.00     642.50',
    'ORD-1102      120.00  STANDARD     3.95     123.95',
    'ORD-1103       18.99  MINIMUM      7.95      26.94',
    'ORD-1104      500.00  FREE         0.00     500.00',
    'ORD-1105       64.00  SMALL        5.95      69.95',
    '--------------------------------------------------',
    '5 orders   goods 1,345.49   shipping 17.85   total 1,363.34',
]


def test_ex1_output():
    assert_output("ex1.py", EX1_EXPECTED)


def test_ex1_only_taught():
    assert_only_taught("ex1.py")


def test_ex1_uses_iteration():
    assert_uses_iteration("ex1.py")


# ── Exercise 2 ───────────────────────────────────────────────────────────

EX2_EXPECTED = [
    'SKU-201  OK          140 on hand',
    'SKU-202  REORDER     68 units',
    'SKU-203  SKIPPED     discontinued',
    'SKU-204  STOCKOUT    scan halted',
    '--------------------------------------',
    'halted at SKU-204: 1 reorder lines, 68 units, 1 skipped',
]


def test_ex2_output():
    assert_output("ex2.py", EX2_EXPECTED)


def test_ex2_only_taught():
    assert_only_taught("ex2.py")


def test_ex2_uses_iteration():
    assert_uses_iteration("ex2.py")


# ── Exercise 3 ───────────────────────────────────────────────────────────

EX3_EXPECTED = [
    'SKU-301 repeats at positions 0 and 2',
    'SKU-301 repeats at positions 0 and 5',
    'SKU-302 repeats at positions 1 and 4',
    'SKU-301 repeats at positions 2 and 5',
    '--------------------------------------',
    '6 rows, 4 duplicate pairs',
]


def test_ex3_output():
    assert_output("ex3.py", EX3_EXPECTED)


def test_ex3_only_taught():
    assert_only_taught("ex3.py")


def test_ex3_uses_iteration():
    assert_uses_iteration("ex3.py")


# ── Exercise 4 ───────────────────────────────────────────────────────────

EX4_EXPECTED = [
    'week  1  stock   76',
    'week  2  stock   62',
    'week  3  stock   48',
    'week  4  stock   34',
    'week  5  stock   20',
    'week  6  stock    6',
    'week  7  stock    0',
    '--------------------------',
    'SKU-401 runs out in week 7',
]


def test_ex4_output():
    assert_output("ex4.py", EX4_EXPECTED)


def test_ex4_only_taught():
    assert_only_taught("ex4.py")


def test_ex4_uses_iteration():
    assert_uses_iteration("ex4.py")


# ── Exercise 5 ───────────────────────────────────────────────────────────

EX5_EXPECTED = [
    'ORD-5101: ACCEPTED - 3 units to IE',
    'ORD-5102: REJECTED - email address is not valid',
    'ORD-5103: REJECTED - quantity must be at least 1',
    'ORD-5104: REJECTED - we do not ship to DE',
    'ORD-5105: ACCEPTED - 1 units to FR',
    'ORD-5106: REJECTED - email address is not valid',
    '--------------------------------------------',
    '2 accepted, 4 rejected',
    '  email 2   quantity 1   destination 1',
]


def test_ex5_output():
    assert_output("ex5.py", EX5_EXPECTED)


def test_ex5_only_taught():
    assert_only_taught("ex5.py")


def test_ex5_uses_iteration():
    assert_uses_iteration("ex5.py")


# ── Exercise 6 ───────────────────────────────────────────────────────────

EX6_EXPECTED = [
    'ORD-6101  HOLD        risk  70    1,240.00',
    'ORD-6102  REJECTED    email address is not valid',
    'ORD-6103  SHIP        risk   0      640.00',
    'ORD-6104  REJECTED    we do not ship to DE',
    'ORD-6105  REJECTED    quantity must be at least 1',
    'ORD-6106  REVIEW      risk  35      307.95',
    '----------------------------------------------',
    '6 orders   1 shipped   1 review   1 held   3 rejected',
    'dispatched value 640.00',
]


def test_ex6_output():
    assert_output("ex6.py", EX6_EXPECTED)


def test_ex6_only_taught():
    assert_only_taught("ex6.py")


def test_ex6_uses_iteration():
    assert_uses_iteration("ex6.py")
