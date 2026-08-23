"""Objective grading for Chapter 2 — Deciding What to Do With an Order.

Submissions are standalone scripts (functions arrive later), so each is run with
the current interpreter and its standard output compared exactly.

Expected outputs in this file were generated from verified reference solutions
written using only Chapter 1 and Chapter 2 material — no loops, no functions, no
collections.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

SUBMISSIONS = Path(__file__).parent / "submissions"

UNTAUGHT = {
    "for": "loops arrive in Chapter 3",
    "while": "loops arrive in Chapter 3",
    "def": "functions arrive in a later chapter",
    "import": "modules arrive in a later chapter",
    "class": "classes arrive in a later chapter",
    "lambda": "not taught",
}


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
    """Chapter 2 has no loops, functions, imports or classes available."""
    src = source_of(name)
    for line in src.splitlines():
        # Strip comments and string literals first, so an ordinary English word
        # inside printed text is never mistaken for a keyword.
        code = line.split("#", 1)[0]
        code = re.sub(r'"[^"]*"|\'[^\']*\'', '""', code)
        # Sequence literals have no keyword to match on, so they need their
        # own patterns: `x in ("A", "B")` and `x in [1, 2]` are tuple/list
        # membership, and `[` is only ever a list or a subscript. Neither is
        # taught until Chapter 3.
        if re.search(r"\bin\s*[\(\[]", code):
            pytest.fail(
                f"{name}: uses membership against a sequence literal "
                "(`x in (a, b)`), which needs tuples — Chapter 3.\n"
                f"  {line.strip()!r}\n"
                "For now, spell the alternatives out: `x == a or x == b`."
            )
        if "[" in code:
            pytest.fail(
                f"{name}: uses `[`, which means a list or a subscript. "
                "Neither has been taught yet.\n"
                f"  {line.strip()!r}"
            )
        for kw, why in UNTAUGHT.items():
            if re.search(rf"(?<![\w.]){kw}\b", code):
                pytest.fail(
                    f"{name}: uses `{kw}`, which has not been taught yet "
                    f"({why}).\n  {line.strip()!r}\n"
                    "Chapter 2 exercises are solvable with straight-line code, "
                    "branching, and what Chapter 1 established. The duplication "
                    "is deliberate."
                )


def assert_converts(name, raw_values):
    src = source_of(name)
    for raw in raw_values:
        assert f'"{raw}"' in src or f"'{raw}'" in src, (
            f"{name}: {raw!r} was given as text and must be written as text, "
            "then converted. Do not retype it as a number."
        )


def assert_no_equals_none(name):
    src = source_of(name)
    assert not re.search(r"[!=]=\s*None", src), (
        f"{name}: compares against None with == or !=. Use `is None` / "
        "`is not None` — Chapter 2 §3 explains why this is a firm convention."
    )


def assert_no_always_true_or(name):
    """Catches `x == "A" or "B"` — always true, raises nothing."""
    src = source_of(name)
    hits = re.findall(r"==\s*[\"\'][^\"\']*[\"\']\s+or\s+[\"\'][^\"\']*[\"\']", src)
    assert not hits, (
        f"{name}: found {hits[0]!r}.\n"
        "This is always true for every input. Python reads it as "
        '(x == "A") or ("B"), and a non-empty string is truthy. Every '
        "comparison needs its own left-hand side. Chapter 2 §2."
    )


def assert_no_redundant_bool_compare(name):
    src = source_of(name)
    hits = re.findall(r"==\s*(?:True|False)\b", src)
    assert not hits, (
        f"{name}: found `== {hits[0].split()[-1]}`. A bool is already a "
        "condition — write `if flag:` or `if not flag:`."
    )


# ── Exercise 1 ───────────────────────────────────────────────────────────

EX1_EXPECTED = [
    'ORDER          VALUE  BAND        SHIP      TOTAL',
    '-----------------------------------------------',
    'ORD-1001      642.50  FREE        0.00     642.50',
    'ORD-1002      120.00  STANDARD    3.95     123.95',
    'ORD-1003      500.00  FREE        0.00     500.00',
]


def test_ex1_output():
    assert_output("ex1.py", EX1_EXPECTED)


def test_ex1_only_taught():
    assert_only_taught("ex1.py")


def test_ex1_converts_feed_text():
    assert_converts("ex1.py", ["642.50", "120.00", "500.00"])


# ── Exercise 2 ───────────────────────────────────────────────────────────

EX2_EXPECTED = [
    'ORD-2001: ACCEPTED - 3 units to IE',
    'ORD-2002: REJECTED - email address is not valid',
    'ORD-2003: REJECTED - quantity must be at least 1',
    'ORD-2004: REJECTED - we do not ship to DE',
]


def test_ex2_output():
    assert_output("ex2.py", EX2_EXPECTED)


def test_ex2_only_taught():
    assert_only_taught("ex2.py")


def test_ex2_no_always_true_or():
    assert_no_always_true_or("ex2.py")


def test_ex2_converts_quantity():
    assert_converts("ex2.py", ["3", "0", "2"])


# ── Exercise 3 ───────────────────────────────────────────────────────────

EX3_EXPECTED = [
    'ORD-3001  applied                     10.0%    25.00    225.00',
    'ORD-3002  no code supplied             0.0%     0.00    250.00',
    'ORD-3003  percentage is zero           0.0%     0.00    250.00',
    'ORD-3004  order below 100.00 minimum   0.0%     0.00     80.00',
]


def test_ex3_output():
    assert_output("ex3.py", EX3_EXPECTED)


def test_ex3_only_taught():
    assert_only_taught("ex3.py")


def test_ex3_uses_is_none():
    assert_no_equals_none("ex3.py")
    assert "is None" in source_of("ex3.py"), (
        "ex3.py: a missing code is None and must be tested with `is None`."
    )


# ── Exercise 4 ───────────────────────────────────────────────────────────

EX4_EXPECTED = [
    'ORD-4001   90  HOLD       1,240.00',
    'ORD-4002    0  SHIP          80.00',
    'ORD-4003   40  REVIEW     1,500.00',
]


def test_ex4_output():
    assert_output("ex4.py", EX4_EXPECTED)


def test_ex4_only_taught():
    assert_only_taught("ex4.py")


def test_ex4_uses_is_none():
    assert_no_equals_none("ex4.py")


def test_ex4_factors_are_independent():
    """The four risk factors must accumulate, not form a chain.

    ORD-4001 trips all four factors and must score 90. This checks the score
    the program actually produces rather than the shape of the source text:
    accumulating with `+=`, rebinding with `x = x + n`, and summing conditional
    expressions are all correct, and no text heuristic distinguishes those from
    a chain without false positives.
    """
    lines = run_submission("ex4.py")
    if not lines:
        pytest.fail("ex4.py produced no output.")
    fields = lines[0].split()
    if len(fields) < 2 or not fields[1].lstrip("-").isdigit():
        pytest.skip("ex4.py line 1 is not in the expected shape; see the output test")
    score = int(fields[1])
    if score == 90:
        return
    if score in (30, 25, 20, 15):
        pytest.fail(
            f"ex4.py: ORD-4001 scored {score}, which is exactly one factor's "
            "points. The four factors are independent — an order can trip any "
            "combination and every one that applies adds. A chain "
            "(`if`/`elif`/`elif`) stops at the first match, which is what this "
            "score means. Chapter 2 §4 covers the distinction.\n"
            "Note the routing below it is the opposite case: exactly one route "
            "applies, so that one *is* a chain."
        )
    pytest.fail(
        f"ex4.py: ORD-4001 scored {score}, expected 90 "
        "(30 + 25 + 20 + 15 — it trips all four factors)."
    )


# ── Exercise 5 ───────────────────────────────────────────────────────────

EX5_EXPECTED = [
    'SKU-5001   2.5  FRAGILE     PRIORITY  Y',
    'SKU-5002  --    WEIGH       EXPRESS   N',
    'SKU-5003  31.0  TWO-PERSON  ECONOMY   Y',
]


def test_ex5_output():
    assert_output("ex5.py", EX5_EXPECTED)


def test_ex5_only_taught():
    assert_only_taught("ex5.py")


def test_ex5_uses_is_none():
    assert_no_equals_none("ex5.py")


def test_ex5_no_redundant_bool_compare():
    assert_no_redundant_bool_compare("ex5.py")


# ── Exercise 6 ───────────────────────────────────────────────────────────

EX6_EXPECTED = [
    'ORD-6001  HOLD        risk  70    1,240.00',
    'ORD-6002  REJECTED    email address is not valid',
    'ORD-6003  SHIP        risk   0      640.00',
]


def test_ex6_output():
    assert_output("ex6.py", EX6_EXPECTED)


def test_ex6_only_taught():
    assert_only_taught("ex6.py")


def test_ex6_uses_is_none():
    assert_no_equals_none("ex6.py")


def test_ex6_no_always_true_or():
    assert_no_always_true_or("ex6.py")
