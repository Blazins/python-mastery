---
layout: exercises
title: "Chapter 4 · Exercises"
eyebrow: "Chapter Four · Exercises"
heading: "Keeping What You Find"
standfirst: "Six problems on lists, sorting and collection. Every one of them requires gathering results during a scan and reporting them afterwards — printing inside the loop will not produce the output asked for."
---

## How to submit

Files go in `syllabus/chapter_04_keeping/submissions/`, named `ex1.py` through
`ex6.py`. Same rules throughout: every value is given, values shown in quotes are
text and must be converted, output is compared exactly, and the work is unaided.

```bash
git switch main && git pull
git switch -c ch04-submissions
micro syllabus/chapter_04_keeping/submissions/ex1.py
```

## What the grader now does differently

**Every exercise is graded twice — once on the data you were given, and once on
a second dataset you have not seen.** The second one is chosen to push execution
into branches the sample data never reaches: a scan that finds nothing, two feeds
of different lengths, a batch where every row is rejected.

This is a direct consequence of the Chapter 3 review. Ten real defects across
Chapters 2 and 3 survived a green test suite, every one of them because the
sample data never entered the branch containing the bug. A grader that only runs
the sample data cannot see that class of defect at all, and it is now the only
class you produce.

Practical consequence: **keep the given data in a variable with the name shown.**
The grader substitutes a new dataset into that assignment. Rename it and the
mutation test fails with a message telling you so.

## What is newly allowed

Lists, and everything §6–§9 taught: `.append()`, item assignment, `.pop()`,
`.insert()`, `.remove()`, `sum()`, `min()`, `max()`, `sorted()`, `.sort()`,
`enumerate()` and `zip()`. You wrote those accumulators by hand for three
chapters; they are earned.

Still not taught, still rejected: `def`, `import`, `class`, `lambda`, `dict`,
`set`, `any`, `all`, `filter`, `map`, comprehensions (`[x for x in ...]`), string
slicing (`text[1:3]`), and string methods such as `.split()` or `.strip()`.
Check `syllabus_map.md` if unsure — and if something you need genuinely is not
listed there, that is a syllabus gap and worth saying so.

---

## Exercise 1 — The returns desk at close of day

Seven items came back today. **SEALED** goods go straight back into sellable
stock. **OPENED** goods can be resold at half their value, but must be inspected
first. Anything else is damaged and written off at full value.

```python
returns = (
    ("SKU-104", "SEALED",  99.00),
    ("SKU-101", "SEALED",  24.99),
    ("SKU-112", "DAMAGED", 45.00),
    ("SKU-107", "OPENED",   8.75),
    ("SKU-109", "SEALED",  24.99),
    ("SKU-102", "DAMAGED", 15.50),
    ("SKU-118", "OPENED",  30.00),
)
```

Print three sections in the order below. Each has a heading with its count in
parentheses, and each lists `  none` — two leading spaces — when it is empty.
RESTOCK lists SKUs alphabetically. INSPECT and WRITE-OFF list SKU then amount,
sorted by SKU, with the SKU left-aligned in 10 and the amount right-aligned in 7
to 2 decimals, all indented two spaces. The rule is 46 hyphens.

```
RESTOCK (3)
  SKU-101
  SKU-104
  SKU-109
INSPECT (2)
  SKU-107      4.38
  SKU-118     15.00
WRITE-OFF (2)
  SKU-102     15.50
  SKU-112     45.00
----------------------------------------------
7 returned   3 restocked   2 to inspect   60.50 lost
```

The closing line reports the number returned, restocked, to inspect, and the
total value lost — separated by three spaces, the loss with thousands separators
and 2 decimals.

---

## Exercise 2 — A picking route in aisle order

Picks arrive in the order customers ordered them, which is the worst possible
order to walk a warehouse in. Reorder them by aisle, then by shelf within the
aisle. Each row is `(sku, aisle, shelf)`.

```python
picks = (
    ("SKU-330", 4, 12),
    ("SKU-118", 1,  3),
    ("SKU-207", 2,  9),
    ("SKU-441", 1, 15),
    ("SKU-092", 4,  2),
    ("SKU-655", 2,  1),
)
```

Number the stops from 1. Columns: stop left in 6, aisle right in 5, shelf right
in 7, then three spaces and the SKU. The rule is 34 hyphens.

```
STOP  AISLE  SHELF   SKU
----------------------------------
1         1      3   SKU-118
2         1     15   SKU-441
3         2      1   SKU-655
4         2      9   SKU-207
5         4      2   SKU-092
6         4     12   SKU-330
----------------------------------
6 stops across 3 aisles
```

The closing line reports the number of stops and **the number of distinct aisles
the route passes through** — which you must work out from the route itself, not
by counting the data by eye. It must read `nothing to pick` when there is
nothing to pick.

---

## Exercise 3 — The slowest endpoints

A sample of requests, each with the endpoint and how long it took in
milliseconds. Anything at or above the threshold counts as slow.

```python
requests = (
    ("/checkout",  412),
    ("/search",   1180),
    ("/cart",       88),
    ("/product",   940),
    ("/search",   1620),
    ("/home",       35),
    ("/checkout",  770),
)
```

```python
SLOW = 500
```

List **the three slowest requests**, worst first, numbered from 1 — and print
`  none` if nothing is slow. The endpoint is left-aligned in 12 and the duration
right-aligned in 6 followed by `ms`. The rule is 30 hyphens.

```
REQUESTS OVER 500ms
1. /search       1620ms
2. /search       1180ms
3. /product       940ms
------------------------------
7 requests   4 slow   fastest 35ms   mean 720.7ms
```

The closing line reports the request count, the slow count, the fastest time,
and the mean to one decimal place. Note that the threshold is a value you must
read from `SLOW` rather than write into the logic — the grader changes it.

---

## Exercise 4 — Reconciling two feeds

The supplier says what it shipped. The warehouse says what it counted. The two
should agree, and today they do not. Each row is `(sku, quantity)`.

```python
expected = (
    ("SKU-101", 120),
    ("SKU-104",  40),
    ("SKU-109",  75),
    ("SKU-112",  12),
    ("SKU-118",  60),
)

counted = (
    ("SKU-101", 118),
    ("SKU-104",  40),
    ("SKU-109",  80),
    ("SKU-112",  12),
    ("SKU-118",  55),
)
```

Walk the two feeds together and report every discrepancy, sorted by SKU, with
the difference **signed** — a shortfall is negative, an overage positive. The
SKU is left-aligned in 10 and the difference right-aligned in 5 with a forced
sign. Print `  none` when the feeds agree. The rule is 30 hyphens.

```
DISCREPANCIES
  SKU-101      -2
  SKU-109      +5
  SKU-118      -5
------------------------------
2 short   1 over   net -2
```

**Two things the sample data does not show you.** If a row appears in a different
position in the two feeds, say so rather than reporting a false discrepancy. And
if the two feeds are not the same length, print this as the very first line,
before anything else:

```
FEED MISMATCH: 5 expected rows, 4 counted rows
```

then carry on and reconcile as much as you can. §9 explains why this cannot be
left to chance.

---

## Exercise 5 — Deduplicating a supplier feed

Chapter 3's exercise 3 found duplicate pairs and could not keep them. This is
that problem with the tool it needed.

```python
feed = (
    "SKU-301", "SKU-302", "SKU-301", "SKU-303",
    "SKU-302", "SKU-301", "SKU-304",
)
```

Build the list of unique SKUs **in the order they first appear** — not sorted —
and separately record every repeat. Print the unique list numbered from 1, then
the repeats, each giving where the SKU was first seen and where it appeared
again.

```
UNIQUE (4)
1. SKU-301
2. SKU-302
3. SKU-303
4. SKU-304
REPEATS
  SKU-301 first seen at 0, again at 2
  SKU-302 first seen at 1, again at 4
  SKU-301 first seen at 0, again at 5
----------------------------------
7 rows   4 unique   3 repeats
```

Print `  no duplicates` when there are none. The rule is 34 hyphens, and the
closing line reports rows, unique count and repeat count.

---

## Exercise 6 — The pipeline, with a report

Everything at once: Chapter 2's validation and risk scoring, Chapter 3's guard
clauses, and this chapter's collection and ordering. Each row is
`(order_id, email, dest, value, account_age_days, billing_country, phone)`.

```python
ALLOWED = ("GB", "IE", "FR")

orders = (
    ("ORD-8101", "a@shop.co", "GB", "1240.00",   3, "GB", None),
    ("ORD-8102", "bad.email", "GB",  "200.00", 400, "GB", "07700900123"),
    ("ORD-8103", "c@shop.co", "IE",  "640.00",  90, "IE", "07700900555"),
    ("ORD-8104", "d@shop.co", "DE",   "80.00",  12, "GB", None),
    ("ORD-8105", "e@shop.co", "FR",  "300.00",  90, "GB", None),
    ("ORD-8106", "f@shop.co", "GB",  "920.00",   2, "FR", None),
    ("ORD-8107", "g@shop.co", "IE",   "45.00", 200, "IE", "07700900999"),
)
```

Validation first, in order: the email must contain `@`, then the destination must
be allowed. A rejected order prints its reason and takes no further part.

Surviving orders are risk-scored on four independent factors: account under 7
days old adds 30, value above `1000.00` adds 25, billing country different from
destination adds 20, missing phone adds 15. Then: 50 or more is HELD, 25 to 49
is REVIEW, below 25 SHIPS. Shipping is free at `500.00` or above, otherwise
`7.95`.

Print four sections — HELD, REVIEW, REJECTED, SHIPPED — in that order. HELD and
REVIEW list order id and risk, **highest risk first**, risk right-aligned in 3.
REJECTED lists order id and reason in arrival order. SHIPPED lists order id and
the total charged, **largest first**, right-aligned in 9 with separators and 2
decimals. Every section prints `  none` when empty. The rule is 46 hyphens.

```
HELD
  ORD-8101  risk  70
  ORD-8106  risk  65
REVIEW
  ORD-8105  risk  35
REJECTED
  ORD-8102  email address is not valid
  ORD-8104  we do not ship to DE
SHIPPED
  ORD-8103     640.00
  ORD-8107      52.95
----------------------------------------------
7 orders   2 shipped   1 review   2 held   2 rejected
dispatched 692.95
```

The closing lines report the counts for every route and the total dispatched.

---

## Checklist before you push

- Every exercise builds a list. Nothing is printed from inside the scan that
  should have been collected and reported afterwards.
- **Every closing line has been read while asking: what does this print when the
  loop found nothing?** Four of Chapter 3's five defects were in that line.
- Every `<=` versus `<` has been checked at its exact boundary.
- If both branches of an `if`/`else` are the same, one of them is wrong.
- `is None` for sentinels; `==` for values.
- The given data is still in a variable with the name shown, so the grader can
  substitute its own.
- Run the suite before committing:

```bash
.venv/bin/python -m pytest syllabus/chapter_04_keeping/ -q
```

Both runs must pass — the one on your data, and the one on data you have not
seen.
