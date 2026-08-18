"""Objective grading for Chapter 1 — Pricing a Product Feed.

Each submission is a standalone script (functions are not taught until a later
chapter), so grading runs the file with the current interpreter and compares
standard output exactly, line for line.

Alongside the output checks there are source checks. Those exist because a
script can produce correct output by printing hardcoded answers, which would
pass an output-only test while demonstrating nothing. The source checks assert
that the numbers were actually computed and that the tools the exercise is
about were the ones used.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

SUBMISSIONS = Path(__file__).parent / "submissions"


# ── helpers ──────────────────────────────────────────────────────────────

def run_submission(name):
    """Execute a submission and return its stdout as a list of lines.

    Trailing blank lines are discarded so that a stray final newline is not
    treated as a failure; every other line must match exactly.
    """
    path = SUBMISSIONS / name
    if not path.exists():
        pytest.skip(f"{name} not submitted yet")

    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        timeout=15,
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
            f"--- expected ---\n" + "\n".join(expected) +
            f"\n--- actual ---\n" + "\n".join(actual)
        )

    for i, (got, want) in enumerate(zip(actual, expected), start=1):
        assert got == want, (
            f"{name}: line {i} differs.\n"
            f"  expected: {want!r}\n"
            f"  actual:   {got!r}"
        )


def assert_not_hardcoded(name, forbidden):
    """The computed answers must not appear as literals in the source."""
    src = source_of(name)
    for literal in forbidden:
        assert literal not in src, (
            f"{name}: the value {literal!r} appears literally in your source. "
            f"That figure is supposed to be computed from the inputs, not typed in."
        )


def assert_converts(name, raw_values):
    """The values the exercise supplies as text must appear as text."""
    src = source_of(name)
    for raw in raw_values:
        assert f'"{raw}"' in src or f"'{raw}'" in src, (
            f"{name}: {raw!r} was given as text (a str) and must be written as "
            f"text in your file, then converted. Do not retype it as a number."
        )


def assert_no_float_division_trick(name, why):
    """Reject int(a / b) where floor division is the correct tool.

    ``int(a / b)`` happens to agree with ``a // b`` for small positive integers,
    so an output-only check cannot tell them apart. They are not the same
    operation: the first routes through a float and loses precision on large
    integers, and the two disagree on negatives. Passing by coincidence is not
    passing.
    """
    src = source_of(name)
    hits = re.findall(r"(?<![\w.])int\(\s*[^()]*(?<![/\w])/(?!/)[^()]*\)", src)
    assert not hits, (
        f"{name}: found {hits[0]!r}. {why}\n"
        f"int(a / b) is not floor division — it divides into a float and then "
        f"truncates. It agrees with a // b for small positive integers and "
        f"disagrees on large ones and on negatives. Use // directly."
    )


# ── Exercise 1 — restock order costing ───────────────────────────────────

EX1_EXPECTED = [
    "Effective unit cost: £11.73",
    "Retail ex VAT:       £17.01",
    "Retail inc VAT:      £20.41",
    "Order cost:          £3,988.20",
    "Projected revenue:   £6,939.47",
]


def test_ex1_output():
    assert_output("ex1.py", EX1_EXPECTED)


def test_ex1_converts_feed_text():
    assert_converts("ex1.py", ["12.75", "340"])


def test_ex1_not_hardcoded():
    assert_not_hardcoded("ex1.py", ["11.73", "17.01", "20.41", "3988.2", "6939.47"])


# ── Exercise 2 — pallet planning ─────────────────────────────────────────

EX2_EXPECTED = [
    "Full cartons:  203",
    "Loose units:   1",
    "Full pallets:  5",
    "Loose cartons: 3",
    "Total weight:  1,125.89 kg",
]


def test_ex2_output():
    assert_output("ex2.py", EX2_EXPECTED)


def test_ex2_converts_feed_text():
    assert_converts("ex2.py", ["2437", "462"])


def test_ex2_uses_integer_division():
    src = source_of("ex2.py")
    assert "//" in src, (
        "ex2.py: cartons and pallets are whole things. Floor division (//) is "
        "the tool this exercise is about."
    )
    assert "%" in src, (
        "ex2.py: the leftovers come from the modulo operator (%)."
    )


def test_ex2_no_float_division_trick():
    assert_no_float_division_trick(
        "ex2.py",
        "Cartons and pallets are counted with floor division.",
    )


def test_ex2_not_hardcoded():
    assert_not_hardcoded("ex2.py", ["203", "1125.89"])


# ── Exercise 3 — foreign currency invoice ────────────────────────────────

EX3_EXPECTED = [
    "Invoice (EUR):   €8,450.00",
    "Converted (GBP): £7,207.85",
    "FX fee:          £144.16",
    "Total (GBP):     £7,352.01",
    "Effective rate:  0.8701",
]


def test_ex3_output():
    assert_output("ex3.py", EX3_EXPECTED)


def test_ex3_converts_feed_text():
    assert_converts("ex3.py", ["8450.00"])


def test_ex3_not_hardcoded():
    assert_not_hardcoded("ex3.py", ["7207.85", "144.16", "7352.01", "0.8701"])


# ── Exercise 4 — daily catalogue report ──────────────────────────────────

def _ex4_row(name, cost, price, qty):
    total = price * qty
    margin = (price - cost) / price
    return f"{name:<20}{qty:>5}{cost:>10.2f}{price:>10.2f}{total:>12,.2f}{margin:>9.1%}"


EX4_EXPECTED = [
    f"{'PRODUCT':<20}{'QTY':>5}{'COST':>10}{'PRICE':>10}{'TOTAL':>12}{'MARGIN':>9}",
    "-" * 66,
    _ex4_row("Blue Mug", 4.99, 9.58, 3),
    _ex4_row("Oak Chopping Board", 18.50, 41.25, 12),
    _ex4_row("Linen Tea Towel", 3.20, 7.99, 140),
    f"{'TOTAL':<45}{9.58 * 3 + 41.25 * 12 + 7.99 * 140:>12,.2f}",
]


def test_ex4_output():
    assert_output("ex4.py", EX4_EXPECTED)


def test_ex4_converts_feed_text():
    assert_converts("ex4.py", ["4.99", "18.50", "3.20", "3", "12", "140"])


def test_ex4_no_manual_padding():
    """Columns must come from width specifiers, not typed spaces.

    Only the contents of string literals are inspected. Lining up the ``=`` of
    consecutive assignments with extra spaces is a style the chapter itself
    uses and is explicitly fine; typing spaces *into the output* is not.
    """
    src = source_of("ex4.py")
    literals = re.findall(r'"""(.*?)"""|\'\'\'(.*?)\'\'\'|"([^"\n]*)"|\'([^\'\n]*)\'',
                          src, flags=re.DOTALL)
    for groups in literals:
        for text in groups:
            if not text or "----" in text:   # the 66-hyphen rule may be a literal
                continue
            assert "    " not in text, (
                f"ex4.py: the string literal {text!r} contains four or more "
                f"consecutive spaces. Every column in this exercise must be "
                f"produced by a width specifier such as {{name:<20}}, not by "
                f"typing spaces into the output."
            )


def test_ex4_uses_width_specifiers():
    src = source_of("ex4.py")
    assert ":<20" in src or ":<20}" in src, (
        "ex4.py: the product column is specified as left-aligned in 20 characters."
    )
    assert ":>9.1%" in src or ".1%" in src, (
        "ex4.py: the margin column is specified as a percentage to 1 decimal place. "
        "Use the % format specifier rather than multiplying by 100 by hand."
    )


# ── Exercise 5 — margin against markup ───────────────────────────────────

EX5_EXPECTED = [
    "Cost:            £18.50",
    "Price:           £41.25",
    "Margin:          55.2%",
    "Markup:          123.0%",
    "Gap:             67.8 percentage points",
]


def test_ex5_output():
    assert_output("ex5.py", EX5_EXPECTED)


def test_ex5_converts_feed_text():
    assert_converts("ex5.py", ["18.50", "41.25"])


def test_ex5_not_hardcoded():
    assert_not_hardcoded("ex5.py", ["55.2", "123.0", "67.8"])


# ── Exercise 6 — till reconciliation ─────────────────────────────────────

EX6_EXPECTED = [
    "Till total: £1,026.86",
    "Pennies:    102686",
    "£50  x 20",
    "£20  x 1",
    "£10  x 0",
    "£5   x 1",
    "£1   x 1",
    "50p  x 1",
    "20p  x 1",
    "10p  x 1",
    "5p   x 1",
    "2p   x 0",
    "1p   x 1",
]


def test_ex6_output():
    assert_output("ex6.py", EX6_EXPECTED)


def test_ex6_converts_feed_text():
    assert_converts("ex6.py", ["1026.86"])


def test_ex6_rounds_before_truncating():
    """int() alone loses a penny; round() is the tool the chapter taught."""
    src = source_of("ex6.py")
    assert "round(" in src, (
        "ex6.py: float('1026.86') * 100 is 102685.99999999999, and int() "
        "truncates that to 102685 — a penny short. Chapter 1 §8 taught the "
        "function that fixes this."
    )


def test_ex6_uses_integer_arithmetic():
    src = source_of("ex6.py")
    assert "//" in src and "%" in src, (
        "ex6.py: the denomination breakdown is built from floor division (//) "
        "and modulo (%) on integer pennies."
    )


def test_ex6_no_float_division_trick():
    assert_no_float_division_trick(
        "ex6.py",
        "The whole point of this exercise is integer arithmetic on pennies.",
    )


def test_ex6_not_hardcoded():
    assert_not_hardcoded("ex6.py", ["102686"])
