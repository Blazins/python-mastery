---
layout: exercises
title: "Chapter 2 · Exercises"
eyebrow: "Chapter Two · Exercises"
heading: "Deciding What to Do With an Order"
standfirst: "Six problems on comparison, boolean logic and branching. Every one processes several orders, because a decision rule you only ever run once teaches you nothing about whether it is right."
---

## How to submit

Files go in `syllabus/chapter_02_order_routing/submissions/`, named `ex1.py`
through `ex6.py`. Same rules as Chapter 1: every value is given, values shown in
quotes are text and must be converted, output is compared exactly, and the work
is done unaided.

```bash
git switch main && git pull
git switch -c ch02-submissions
micro syllabus/chapter_02_order_routing/submissions/ex1.py
```

## Before you start: the repetition is deliberate

Each exercise processes three or four orders, and you have no way yet to avoid
writing the same decision logic once per order. **That is intentional, and you
should feel it.**

Chapter 3 introduces repetition, and the first thing it will do is collapse
exactly this duplication into a few lines. Meeting that after having typed the
same `elif` chain four times is the difference between "here is a loop" and
"*obviously* there has to be a loop." Do not try to be clever about avoiding it —
write it out.

One thing worth doing as you go: notice which parts differ between the copies
and which are identical. That distinction is the entire idea behind every
abstraction you will meet for the rest of the syllabus.

---

## Exercise 1 — Shipping bands across a batch

Three orders arrive, values as text from the order system. Charge shipping by
band: free at £500 or above, £3.95 from £100, £5.95 from £25, £7.95 below that.

```
a_id, a_raw = "ORD-1001", "642.50"
b_id, b_raw = "ORD-1002", "120.00"
c_id, c_raw = "ORD-1003", "500.00"
```

Print a header row, a rule of exactly 47 hyphens, then one row per order.

| Column | Width | Alignment | Format |
|--------|-------|-----------|--------|
| Order  | 10 | left  | — |
| Value  | 10 | right | 2 decimals, thousands separators |
| *(gap)* | 2 | — | two literal spaces |
| Band   | 10 | left  | — |
| Ship   | 6  | right | 2 decimals |
| Total  | 11 | right | 2 decimals, thousands separators |

Header labels: `ORDER`, `VALUE`, `BAND`, `SHIP`, `TOTAL`, using the same widths
and alignments.

```
ORDER          VALUE  BAND        SHIP      TOTAL
-----------------------------------------------
ORD-1001      642.50  FREE        0.00     642.50
ORD-1002      120.00  STANDARD    3.95     123.95
ORD-1003      500.00  FREE        0.00     500.00
```

`ORD-1003` is exactly on the boundary. Read the rule again and decide
deliberately which band it belongs to — do not let the operator you happen to
type decide for you.

---

## Exercise 2 — The validation gauntlet

Four orders must pass three checks before acceptance, **in this order**:

1. The email must contain an `@`.
2. The quantity must be at least 1.
3. The destination must be one we ship to: `GB`, `IE` or `FR`.

Report only the **first** failure for each order. An order failing two checks
produces one line, naming the first.

```
a_id, a_email, a_raw_qty, a_dest = "ORD-2001", "mike@example.com", "3",  "IE"
b_id, b_email, b_raw_qty, b_dest = "ORD-2002", "mike.example.com", "3",  "GB"
c_id, c_email, c_raw_qty, c_dest = "ORD-2003", "buyer@shop.co",   "0",  "GB"
d_id, d_email, d_raw_qty, d_dest = "ORD-2004", "buyer@shop.co",   "2",  "DE"
```

```
ORD-2001: ACCEPTED - 3 units to IE
ORD-2002: REJECTED - email address is not valid
ORD-2003: REJECTED - quantity must be at least 1
ORD-2004: REJECTED - we do not ship to DE
```

Two things this exercise is actually testing. The destination check must compare
each option properly — `dest == "GB" or "IE" or "FR"` is always true and would
accept every country on earth. And the quantity arrives as text, so comparing it
to a number without converting raises `TypeError`.

---

## Exercise 3 — Discount codes that may not be there

Discount codes arrive from a promotions system that is, as promotions systems
tend to be, unreliable. A code may be missing entirely (`None`), present with a
blank percentage (`""`), or present with a percentage of zero.

Apply the first matching rule:

| Condition | Reason text | Rate |
|-----------|-------------|------|
| Code is `None` | `no code supplied` | 0.0 |
| Percentage is the empty string | `code has no percentage` | 0.0 |
| Percentage is zero or less | `percentage is zero` | 0.0 |
| Order value below £100 | `order below 100.00 minimum` | 0.0 |
| Otherwise | `applied` | the given percentage |

```
a_id, a_code, a_pct, a_raw_value = "ORD-3001", "SAVE10", "10",  "250.00"
b_id, b_code, b_pct, b_raw_value = "ORD-3002", None,     "",    "250.00"
c_id, c_code, c_pct, c_raw_value = "ORD-3003", "SAVE00", "0",   "250.00"
d_id, d_code, d_pct, d_raw_value = "ORD-3004", "SAVE20", "20",  "80.00"
```

Each line: order id, two spaces, reason left-aligned in 26, rate right-aligned
in 6 to 1 decimal, a literal `%`, the discount amount right-aligned in 9 with
separators and 2 decimals, then the amount payable right-aligned in 10 the same
way.

```
ORD-3001  applied                     10.0%    25.00    225.00
ORD-3002  no code supplied             0.0%     0.00    250.00
ORD-3003  percentage is zero           0.0%     0.00    250.00
ORD-3004  order below 100.00 minimum   0.0%     0.00     80.00
```

**The trap is real and it will crash your program if you get it wrong.**
`float("")` raises `ValueError`. Your third check calls `float()` on the
percentage — so it must be impossible to reach when the percentage is blank.
Chapter 2 §2 explains the mechanism that guarantees this. Get the order of the
checks wrong and you will see a traceback rather than a wrong answer.

Note also that `b`'s code is `None` **and** its percentage is blank. Only the
first reason is reported.

---

## Exercise 4 — Fraud risk scoring

Score each order, then route it. The four risk factors are **independent** — an
order can trigger any combination, and every one that applies adds its points:

| Factor | Points |
|--------|--------|
| Account under 7 days old | 30 |
| Order value above £1,000 | 25 |
| Billing country differs from shipping country | 20 |
| No phone number on file | 15 |

The route is then decided by total score — and here exactly one applies: 50 or
above holds the order, 25 to 49 flags it for review, below 25 ships it.

```
a_id, a_raw_value, a_age, a_bill, a_ship_to, a_phone = "ORD-4001", "1240.00", 3,  "GB", "DE", None
b_id, b_raw_value, b_age, b_bill, b_ship_to, b_phone = "ORD-4002", "80.00",  400, "GB", "GB", "07700900123"
c_id, c_raw_value, c_age, c_bill, c_ship_to, c_phone = "ORD-4003", "1500.00", 90, "FR", "FR", None
```

Each line: order id, score right-aligned in 5, two spaces, route left-aligned in
8, value right-aligned in 11 with separators and 2 decimals.

```
ORD-4001   90  HOLD       1,240.00
ORD-4002    0  SHIP          80.00
ORD-4003   40  REVIEW     1,500.00
```

**The structural point:** the four factors use one kind of structure and the
routing uses another. Getting that backwards produces plausible output and wrong
scores — an order tripping three factors would score only the first. Chapter 2
§4 covers the distinction directly.

The missing phone number is `None`, not `""`. Test for it accordingly.

---

## Exercise 5 — Warehouse handling and dispatch priority

Each item needs a handling instruction and a dispatch priority.

**Handling** — first match wins:

| Condition | Handling |
|-----------|----------|
| Weight is missing | `WEIGH` |
| Weight 30 kg or more | `TWO-PERSON` |
| Item is fragile | `FRAGILE` |
| Otherwise | `STANDARD` |

**Priority** — by order value: £1,000 or more is `EXPRESS`, £100 or more is
`PRIORITY`, otherwise `ECONOMY`.

**Domestic** — `Y` if the destination is `GB`, otherwise `N`.

```
a_sku, a_raw_w, a_fragile, a_dest, a_raw_value = "SKU-5001", "2.5",  True,  "GB", "480.00"
b_sku, b_raw_w, b_fragile, b_dest, b_raw_value = "SKU-5002", None,   False, "FR", "1200.00"
c_sku, c_raw_w, c_fragile, c_dest, c_raw_value = "SKU-5003", "31.0", False, "GB", "95.00"
```

Each line: SKU, then the weight column, two spaces, handling left-aligned in 12,
priority left-aligned in 10, then the domestic flag.

The **weight column** is 6 characters wide. When a weight exists, show it right-aligned
to 1 decimal place. When it is missing, show the literal six characters
`··--··` — that is two spaces, two hyphens, two spaces.

```
SKU-5001   2.5  FRAGILE     PRIORITY  Y
SKU-5002  --    WEIGH       EXPRESS   N
SKU-5003  31.0  TWO-PERSON  ECONOMY   Y
```

Note that `a_fragile` is already a `bool`. It needs no comparison — `if
a_fragile:` is the whole test, and writing `if a_fragile == True:` is redundant
in a way reviewers will comment on.

The priority rule is a three-way choice producing one value. Chapter 2 §5 covers
a compact form for this; using it is not required, but decide deliberately
rather than by default.

---

## Exercise 6 — The full order pipeline

The hardest exercise in the set, and the one that combines everything.

Each order runs the Exercise 2 validation gauntlet first. If it fails, report
the first failure and that order produces nothing else. If it passes, score it
with the Exercise 4 risk factors, route it, add shipping (free at £500 or above,
otherwise £7.95), and report.

Note one deliberate change from Exercise 4: the billing country is compared
against the **destination**, since that is what the order actually has.

```
a_id, a_email, a_raw_qty, a_dest, a_raw_value, a_age, a_bill, a_phone = "ORD-6001", "buyer@shop.co", "2", "GB", "1240.00", 3,  "GB", None
b_id, b_email, b_raw_qty, b_dest, b_raw_value, b_age, b_bill, b_phone = "ORD-6002", "buyer.shop.co", "2", "GB", "200.00", 400, "GB", "07700900123"
c_id, c_email, c_raw_qty, c_dest, c_raw_value, c_age, c_bill, c_phone = "ORD-6003", "buyer@shop.co", "1", "IE", "640.00",  90, "IE", "07700900555"
```

A **rejected** order prints: id, two spaces, `REJECTED` left-aligned in 12, then
the reason.

An **accepted** order prints: id, two spaces, route left-aligned in 12, then
`risk ` and the score right-aligned in 3, then three spaces, then the total
charged right-aligned in 9 with separators and 2 decimals.

```
ORD-6001  HOLD        risk  70    1,240.00
ORD-6002  REJECTED    email address is not valid
ORD-6003  SHIP        risk   0      640.00
```

You have no way yet to skip the rest of an order's processing once it is
rejected — that needs a tool from a later chapter. Work out a structure that
gets the right output anyway. There is more than one way; choose one you could
explain.

---

## Checklist

- [ ] Six files, `ex1.py` to `ex6.py`, in `submissions/`.
- [ ] Every value given in quotes was converted, not retyped as a number.
- [ ] No column aligned with typed spaces — width specifiers only.
- [ ] `None` tested with `is None`, never `== None`.
- [ ] Multi-option comparisons spelled out in full, each with its own left side.
- [ ] Chains used where cases are alternatives; separate `if`s where they are independent.
- [ ] No debugging output or commented-out code left behind.
- [ ] Every file runs without a traceback.
