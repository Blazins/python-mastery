---
layout: exercises
title: "Chapter 5 · Exercises"
eyebrow: "Chapter Five · Exercises"
heading: "Reading What Arrives"
standfirst: "Six problems on text. Nothing arrives pre-split, several lines are wrong in ways the sample data will not show you, and one exercise exists specifically to be solved without the built-in that would do it for you."
---

## How to submit

Files go in `syllabus/chapter_05_text/submissions/`, named `ex1.py` through
`ex6.py`. Every value is given, output is compared exactly, and the work is
unaided.

```bash
git switch main && git pull
git switch -c ch05-submissions
micro syllabus/chapter_05_text/submissions/ex1.py
```

## What the grader does differently this time

Chapter 4's suite ran every exercise against a second dataset and still caught
**none** of the six defects the review found. Two of those misses were design
errors: the mutated data preserved the very property each bug leaned on. The
aisle bug counted matching *pairs* instead of distinct values, and survived
because every aisle in both datasets appeared exactly twice — making pairs and
distinct coincide.

So the rule is now stricter. **A mutation must break a structural property of
the sample data, not merely change its values.** Where the sample has even
counts, the mutation has uneven ones. Where the sample always finds a match, the
mutation finds none. Where the sample always has a separator, the mutation has
none at all.

Practical consequences: **keep the given data in a variable with the name
shown**, and assume that anything true of the sample data by coincidence will be
false in the second run.

## Newly allowed

Slicing, and the string methods from §4 and §5: `.strip()`, `.lstrip()`,
`.rstrip()`, `.upper()`, `.lower()`, `.startswith()`, `.endswith()`,
`.isdigit()`, `.find()`, `.count()`, `.replace()`, `.split()`, `.join()`.

**Deliberately withheld**, because each would hand over an exercise built to make
you derive it: `.rfind()`, `.rindex()`, `.rsplit()`, `.partition()`,
`.rpartition()`, `.splitlines()`, `.removeprefix()`, `.removesuffix()`, and
`.index()`. Still rejected as before: `def`, `import`, `class`, `lambda`,
`dict`, `set`, `any`, `all`, `filter`, `map`, and comprehensions.

---

## Exercise 1 — A supplier feed that has been through several hands

Six lines of raw text with inconsistent spacing and capitalisation, one line
missing a field, one with a non-numeric quantity, one out of stock.

```python
feed = (
    "SKU-301|Blue Mug|12|4.99",
    "  sku-302 | Red Mug | 40 | 5.49 ",
    "SKU-303|Green Mug|abc|3.10",
    "SKU-304|Yellow Mug|7",
    "sku-305|Black Mug|0|8.00",
    "SKU-306|White Mug|5|12.75",
)
```

Accept a line only if it has exactly four fields, a numeric quantity, and a
quantity above zero. Normalise the SKU to upper case and strip whitespace from
every field. Accepted rows print sorted by SKU: SKU left in 10, name left in 12,
quantity right in 4, price right in 8 to 2 decimals, then the **line value**
(quantity × price) right in 10 to 2 decimals.

Rejected rows print what failed — the SKU where you have one, the whole stripped
line where you do not — left-aligned in 28, then the reason. The rule is 44
hyphens.

```
ACCEPTED (3)
  SKU-301   Blue Mug      12    4.99     59.88
  SKU-302   Red Mug       40    5.49    219.60
  SKU-306   White Mug      5   12.75     63.75
REJECTED (3)
  SKU-303                     quantity is not a number
  SKU-304|Yellow Mug|7        expected 4 fields, found 3
  SKU-305                     out of stock
--------------------------------------------
6 lines   3 accepted   3 rejected   value 343.23
```

Both sections print `  none` when empty. The closing line reports lines,
accepted, rejected, and total stock value with separators.

---

## Exercise 2 — Triaging a log

Each line is a timestamp, a level, and a message. The timestamp occupies the
first 19 characters; the level and message follow.

```python
log = (
    "2026-09-01 09:14:02 INFO  checkout completed for ORD-8101",
    "2026-09-01 09:14:07 WARN  slow query on /search took 1620ms",
    "2026-09-01 09:15:31 ERROR payment gateway timeout for ORD-8102",
    "2026-09-01 09:16:00 INFO  cart updated",
    "2026-09-01 09:17:45 ERROR payment gateway timeout for ORD-8103",
    "2026-09-01 09:18:12 WARN  slow query on /product took 940ms",
)
```

```python
LEVEL = "ERROR"
```

List every entry at `LEVEL`, showing **only the time** — not the date — and the
message. Then report how many lines occurred at **each level present**, in the
order the levels first appear.

```
ERROR ENTRIES (2)
  09:15:31  payment gateway timeout for ORD-8102
  09:17:45  payment gateway timeout for ORD-8103
BY LEVEL
  INFO    2
  WARN    2
  ERROR   2
----------------------------------------
6 lines   3 levels   2 error
```

The rule is 40 hyphens. Print `  none` when no entry matches. Note that `LEVEL`
is a value to read, not a string to write into the logic — the grader changes it,
and it changes the level counts too.

---

## Exercise 3 — Deduplicating messy signups

Each line is a name and an email in angle brackets, with unpredictable spacing
and capitalisation. Two people signed up twice.

```python
signups = (
    "  Ada Lovelace <ADA@shop.co>  ",
    "Grace Hopper <grace@shop.co>",
    "ada lovelace <ada@shop.co>",
    "Alan Turing <alan@SHOP.co>",
    "Grace Hopper <GRACE@shop.co>",
    "Katherine Johnson <katherine@shop.co>",
)
```

An email is the identity: two entries are the same person if their emails match
**once trimmed and lower-cased**, regardless of how the name is written. Keep the
first occurrence of each, in arrival order, numbered from 1 with the name left in
20 followed by the normalised email.

Report every duplicate with **the line number it appeared on**, counting from
zero, the name as written on that line, and the email it collided with. A line
with no angle brackets is malformed and reported the same way, with the reason
`malformed`.

```
KEPT (4)
1. Ada Lovelace        ada@shop.co
2. Grace Hopper        grace@shop.co
3. Alan Turing         alan@shop.co
4. Katherine Johnson   katherine@shop.co
DUPLICATES
  line 2: ada lovelace already signed up as ada@shop.co
  line 4: Grace Hopper already signed up as grace@shop.co
----------------------------------------------
6 signups   4 unique   2 duplicate
```

The rule is 46 hyphens, and the duplicates section prints `  none` when there
are none.

---

## Exercise 4 — Splitting on the last separator

A path splits into a folder and a filename at the **last** slash — not the first.
`.split("/")` gives you every piece and does not tell you which boundary matters,
and `.rfind()` is rejected by the grader on purpose. §5 showed you how to find a
delimiter by walking the string; this asks you to find the *last* one.

```python
paths = (
    "reports/2026/september/stock.csv",
    "stock.csv",
    "reports/2026/",
    "reports//stock.csv",
    "reports/2026/september/archive/old.stock.csv",
)
```

Split each path at the last `/` into folder and filename, then split the filename
at the **last** `.` into stem and extension. A path with no slash has an empty
folder, printed as a single `.`; a path ending in a slash has no filename; a
filename with no dot has no extension.

Folder left in 34, stem left in 14, then the extension. The rule is 52 hyphens.

```
PARSED (4)
  reports/2026/september            stock         csv
  .                                 stock         csv
  reports/                          stock         csv
  reports/2026/september/archive    old.stock     csv
ODD
  reports/2026/                     no filename
----------------------------------------------------
5 paths   4 parsed   1 odd
```

Note `old.stock.csv` — the stem is `old.stock`, not `old`. Splitting on the
first dot gives the wrong answer, which is the whole point of the exercise.

---

## Exercise 5 — Building the export

The other direction. You have structured rows and must produce delimited text,
then measure it.

```python
rows = (
    ("SKU-306", "White Mug", 5, 12.75),
    ("SKU-301", "Blue Mug", 12, 4.99),
    ("SKU-302", "Red Mug", 40, 5.49),
)
```

```python
HEADERS = ("sku", "name", "qty", "price")
```

Build a list of lines: the header joined by `|`, then one line per row sorted by
SKU, with the quantity converted to text and the price shown to exactly two
decimals. Print each indented two spaces.

Then compute, for **each column**, the width of its widest field across every
line including the header, and report it — header left in 6, width right in 3.

```
EXPORT
  sku|name|qty|price
  SKU-301|Blue Mug|12|4.99
  SKU-302|Red Mug|40|5.49
  SKU-306|White Mug|5|12.75
WIDTHS
  sku     7
  name    9
  qty     3
  price   5
----------------------------------------
4 lines   4 columns   90 characters
```

The rule is 40 hyphens. The closing line reports lines, columns, and the total
number of characters across all lines.

---

## Exercise 6 — The pipeline, from raw text

Everything: parsing, normalising, validating, deduplicating, scoring, sorting and
reporting. Each line is `order_id|email|destination|value|account_age_days`.

```python
ALLOWED = ("GB", "IE", "FR")

feed = (
    "ORD-9101|a@shop.co|GB|1240.00|3",
    "ORD-9102|bad.email|GB|200.00|400",
    "  ord-9103 | C@Shop.co | ie | 640.00 | 90 ",
    "ORD-9104|d@shop.co|DE|80.00|12",
    "ORD-9105|e@shop.co|FR|abc|90",
    "ORD-9103|c@shop.co|IE|640.00|90",
    "ORD-9106|f@shop.co|GB|920.00",
)
```

Strip and split each line. Reject anything without exactly five fields. Normalise
the order id and destination to upper case and the email to lower case, then
reject in this order: a **duplicate order id** already seen, an email without
`@`, a destination not in `ALLOWED`, a non-numeric account age, and a value that
is not a number.

Surviving orders score risk: account under 7 days adds 30, value above `1000.00`
adds 25. Print accepted orders **highest risk first**: id left in 10, destination
left in 4, value right in 10 with separators and 2 decimals, then `risk` and the
score right in 3.

```
ACCEPTED (2)
  ORD-9101  GB    1,240.00   risk  55
  ORD-9103  IE      640.00   risk   0
REJECTED (5)
  ORD-9102                          email address is not valid
  ORD-9104                          we do not ship to DE
  ORD-9105                          value is not a number
  ORD-9103                          duplicate order
  ORD-9106|f@shop.co|GB|920.00      expected 5 fields, found 4
--------------------------------------------------
7 lines   2 accepted   5 rejected   banked 1,880.00
```

Rejected rows print the id where you have one and the whole stripped line where
you do not, left in 34, then the reason. The rule is 50 hyphens, both sections
print `  none` when empty, and the closing line reports lines, accepted,
rejected, and the total value banked.

---

## Checklist before you push

Run `pre_submission.md` against every file. The items that bit hardest last
chapter:

- **Anything true of the sample data by coincidence will be false in the second
  run.** Even counts, a match always existing, a separator always present — none
  of those survive.
- **What does each closing line print when the loop found nothing?** And is every
  name it reads bound on *both* paths?
- **Every `<=` versus `<` at the exact boundary.** "Under 7" is not `<= 7`;
  "above 1000.00" is not `>= 1000.00`.
- **`in` — what does the container actually hold?** And on a string it means
  substring, not membership.
- **Both branches of an `if`/`else` identical? One is wrong.**
- Convert only after validating. `isdigit()` before `int()`.

```bash
.venv/bin/python -m pytest syllabus/chapter_05_text/ -q
```

Both runs must pass — yours, and the one on data you have not seen.
