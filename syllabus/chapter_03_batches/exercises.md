---
layout: exercises
title: "Chapter 3 · Exercises"
eyebrow: "Chapter Three · Exercises"
heading: "Doing It Once for Every Order"
standfirst: "Six problems on tuples, loops and accumulation. Chapter 2 made you write the same block four times; these are sized so that doing it that way is no longer possible."
---

## How to submit

Files go in `syllabus/chapter_03_batches/submissions/`, named `ex1.py` through
`ex6.py`. Same rules throughout: every value is given, values shown in quotes are
text and must be converted, output is compared exactly, and the work is unaided.

```bash
git switch main && git pull
git switch -c ch03-submissions
micro syllabus/chapter_03_batches/submissions/ex1.py
```

## What has changed, and what the grader now enforces

Chapters 1 and 2 banned loops, functions, lists and imports. **Loops and tuples
are now taught**, so the grader accepts them — and it additionally rejects any
submission that solves these by copying a block per row, because that is the
habit this chapter exists to end.

Still not taught, still rejected: `def`, `import`, `class`, `lambda`, lists
(`[1, 2]`), string methods such as `.split()` or `.strip()`, and the built-ins
`sum()`, `min()`, `max()`, `sorted()`, `enumerate()` and `zip()`. Several of
those would shorten these exercises considerably. That is precisely why they are
held back — §5 exists so that you write the accumulator yourself before being
handed the one-liner. Check `syllabus_map.md` if unsure.

Indexing with `[i]` **is** taught and allowed, since §1 and §6 cover it.

---

## Exercise 1 — A shipping report with totals

Chapter 2's exercise 1 printed five rows. This one prints five rows *and* has to
know what they add up to, which is the part duplication cannot do.

Bands: `500.00` or more ships free; `100.00` or more is STANDARD at `3.95`;
`25.00` or more is SMALL at `5.95`; anything less is MINIMUM at `7.95`.

```python
orders = (
    ("ORD-1101", "642.50"),
    ("ORD-1102", "120.00"),
    ("ORD-1103", "18.99"),
    ("ORD-1104", "500.00"),
    ("ORD-1105", "64.00"),
)
```

Print a header row, a rule of exactly 50 hyphens, one line per order, the rule
again, then a summary. Columns: order id left in 10, goods right in 10 with
separators and 2 decimals, two spaces, band left in 12, shipping right in 5 with
2 decimals, total right in 11 with separators and 2 decimals.

```
ORDER          GOODS  BAND         SHIP      TOTAL
--------------------------------------------------
ORD-1101      642.50  FREE         0.00     642.50
ORD-1102      120.00  STANDARD     3.95     123.95
ORD-1103       18.99  MINIMUM      7.95      26.94
ORD-1104      500.00  FREE         0.00     500.00
ORD-1105       64.00  SMALL        5.95      69.95
--------------------------------------------------
5 orders   goods 1,345.49   shipping 17.85   total 1,363.34
```

The summary line is `N orders`, then `goods`, `shipping` and `total`, each
separated by three spaces, all with thousands separators and 2 decimals.

---

## Exercise 2 — A reorder scan that skips and stops

A stock scan walks the catalogue in order. Discontinued lines are skipped
entirely. A line with nothing on hand halts the whole scan — the warehouse has a
problem that must be dealt with before the rest is meaningful.

Each row is `(sku, on_hand, reorder_level, active)`.

```python
stock = (
    ("SKU-201", 140, 50, True),
    ("SKU-202", 12, 40, True),
    ("SKU-203", 88, 20, False),
    ("SKU-204", 0, 30, True),
    ("SKU-205", 5, 25, True),
)
```

For each active line: if `on_hand` is zero, print the STOCKOUT line and stop the
scan immediately. If `on_hand` is at or below `reorder_level`, it needs
reordering — the quantity to order brings it to twice the reorder level. Anything
else is OK.

The status column is left-aligned in 12, following two spaces after the sku. The
rule is 38 hyphens.

```
SKU-201  OK          140 on hand
SKU-202  REORDER     68 units
SKU-203  SKIPPED     discontinued
SKU-204  STOCKOUT    scan halted
--------------------------------------
halted at SKU-204: 1 reorder lines, 68 units, 1 skipped
```

The closing line differs depending on whether the scan halted. Both forms are
shown by the data above — you will have to reason about the other one.

**This exercise is where `break` and `continue` earn their place.** Solving it
with flags and nested conditions is possible and will be marked down.

---

## Exercise 3 — Duplicate rows in a supplier feed

A supplier feed sometimes lists the same SKU more than once. Before loading it
you want to know every position where a repeat occurs.

```python
feed = ("SKU-301", "SKU-302", "SKU-301", "SKU-303", "SKU-302", "SKU-301")
```

Report every *pair* of positions holding the same SKU, in the order a systematic
scan finds them: for each position, compare it against every position after it.
Positions are indices, counting from zero.

```
SKU-301 repeats at positions 0 and 2
SKU-301 repeats at positions 0 and 5
SKU-302 repeats at positions 1 and 4
SKU-301 repeats at positions 2 and 5
--------------------------------------
6 rows, 4 duplicate pairs
```

Note that a SKU appearing three times produces three pairs, not two. That falls
out of the scan rather than needing special handling — if you find yourself
writing special handling, your loops are the wrong shape.

The rule is 38 hyphens. The closing line reports total rows and total pairs, and
must read `no duplicates` when there are none.

---

## Exercise 4 — Stock depletion forecast

A line sells `34` units a week and is restocked with `20`. Starting from `90`,
when does it run out?

```python
sku = "SKU-401"
stock = 90
weekly_demand = 34
weekly_restock = 20
week = 0
```

Simulate week by week. Each week, demand is taken and the restock arrives; stock
can never go below zero. Print the stock at the end of each week, then a closing
line.

**Cap the simulation at 12 weeks.** A forecast that runs forever is not a
forecast, and a stock line that is stable would loop indefinitely without the
cap — the guard is part of the exercise, not scaffolding.

```
week  1  stock   76
week  2  stock   62
week  3  stock   48
week  4  stock   34
week  5  stock   20
week  6  stock    6
week  7  stock    0
--------------------------
SKU-401 runs out in week 7
```

Week numbers are right-aligned in 2, stock right-aligned in 4, and the rule is 26
hyphens. Your closing line must handle the stable case too — change
`weekly_restock` to `40` while testing and satisfy yourself that it reports
sensibly, then change it back before submitting.

---

## Exercise 5 — The validation gauntlet, with a tally

Chapter 2's exercise 2 validated four orders and printed a verdict for each. This
one validates six and has to report *how many failed for each reason* — which
means the checks cannot simply print and forget.

```python
ALLOWED = ("GB", "IE", "FR")

orders = (
    ("ORD-5101", "buyer@shop.co", "3", "IE"),
    ("ORD-5102", "buyer.shop.co", "2", "GB"),
    ("ORD-5103", "buyer@shop.co", "0", "GB"),
    ("ORD-5104", "buyer@shop.co", "4", "DE"),
    ("ORD-5105", "buyer@shop.co", "1", "FR"),
    ("ORD-5106", "shop.co", "0", "US"),
)
```

Checks apply in order: a valid email must contain `@`; quantity must be at least
1; the destination must be one of the allowed countries. **The first failure
decides the verdict** — an order with both a bad email and a zero quantity is
counted once, against the email.

```
ORD-5101: ACCEPTED - 3 units to IE
ORD-5102: REJECTED - email address is not valid
ORD-5103: REJECTED - quantity must be at least 1
ORD-5104: REJECTED - we do not ship to DE
ORD-5105: ACCEPTED - 1 units to FR
ORD-5106: REJECTED - email address is not valid
--------------------------------------------
2 accepted, 4 rejected
  email 2   quantity 1   destination 1
```

The rule is 44 hyphens. The final line is indented by two spaces and separates
its three counts by three spaces.

Write the allowed countries once, as a tuple, and test membership with `in`.

---

## Exercise 6 — The pipeline, whole

The Chapter 2 review closed with an instruction: do not patch that exercise's
bugs, rewrite it once iteration exists. This is that rewrite, with two additions
— a sixth order, and a summary the original could not have produced.

```python
ALLOWED = ("GB", "IE", "FR")

orders = (
    ("ORD-6101", "buyer@shop.co", "2", "GB", "1240.00", 3, "GB", None),
    ("ORD-6102", "buyer.shop.co", "2", "GB", "200.00", 400, "GB", "07700900123"),
    ("ORD-6103", "buyer@shop.co", "1", "IE", "640.00", 90, "IE", "07700900555"),
    ("ORD-6104", "buyer@shop.co", "5", "DE", "80.00", 12, "GB", None),
    ("ORD-6105", "buyer@shop.co", "0", "GB", "310.00", 40, "GB", "07700900777"),
    ("ORD-6106", "buyer@shop.co", "3", "FR", "300.00", 90, "GB", None),
)

```

Validation first, in order: email contains `@`, quantity at least 1, destination
allowed. A rejected order prints its reason and takes no further part.

Surviving orders are risk-scored on four **independent** factors: account under
7 days old adds 30, value above `1000.00` adds 25, billing country different from
destination adds 20, missing phone adds 15. The route is then decided by the
total: 50 or more HOLDs, 25 to 49 REVIEWs, below 25 SHIPs. Shipping is free at
`500.00` or above, otherwise `7.95`.

```
ORD-6101  HOLD        risk  70    1,240.00
ORD-6102  REJECTED    email address is not valid
ORD-6103  SHIP        risk   0      640.00
ORD-6104  REJECTED    we do not ship to DE
ORD-6105  REJECTED    quantity must be at least 1
ORD-6106  REVIEW      risk  35      307.95
----------------------------------------------
6 orders   1 shipped   1 review   1 held   3 rejected
dispatched value 640.00
```

The route column is left-aligned in 12 after two spaces, `risk` then the score
right-aligned in 3, three spaces, then the total right-aligned in 9 with
separators and 2 decimals. The rule is 46 hyphens.

The summary counts every route and reports the total value of orders that
actually shipped — not held, not reviewed, not rejected.

---

## Checklist before you push

- Every exercise uses a loop. No block is written twice.
- No `def`, `import`, `class`, `lambda`, lists, string methods, or
  `sum`/`min`/`max`/`sorted`/`enumerate`/`zip`.
- Accumulators are initialised **before** the loop, not inside it.
- `is None` for the sentinels; `==` for values.
- Run the suite before committing:

```bash
.venv/bin/python -m pytest syllabus/chapter_03_batches/ -q
```

- Before submitting, change one value in each exercise's data and check the
  output still makes sense. Chapter 2's review found five defects that the fixed
  data hid — that habit is the one being built.
