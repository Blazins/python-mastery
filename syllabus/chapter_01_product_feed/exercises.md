# Chapter 1 — Exercises

**Pricing a Product Feed**

---

## How to submit

Each exercise is one Python file, written into
`syllabus/chapter_01_product_feed/submissions/`, named exactly as stated
(`ex1.py`, `ex2.py`, …). Open each with `micro`:

```
micro syllabus/chapter_01_product_feed/submissions/ex1.py
```

Every input value is given to you in the exercise and must be written into your
file exactly as shown — including the ones given as text in quotes. Those are
text on purpose: they represent data arriving from a supplier feed, and part of
each exercise is converting them correctly.

Your program prints the specified lines and nothing else. Grading runs each file
with `python3` and compares standard output **exactly**, line for line. A stray
extra `print`, a missing `£`, or a wrong number of decimal places is a failure —
this is deliberate, because matching an output spec precisely is a real and
constant part of the job.

**Attempt these unaided.** No searching, no reference beyond `content.html` and
`syllabus_map.md`. If something appears to need a tool that Chapter 1 did not
teach, that is a syllabus gap — flag it rather than assuming the fault is yours.

---

## Exercise 1 — Restock order costing

A supplier feed sends the wholesale cost and the number of units for a restock.
Trading has negotiated a bulk discount that applies to the wholesale cost
*before* any markup is added. Company markup and VAT then apply as normal.

Use exactly these values:

```
raw_unit_cost      = "12.75"   # GBP ex-VAT, as text from the feed
raw_units          = "340"     # as text from the feed
bulk_discount_rate = 0.08      # applied to wholesale cost first
markup_rate        = 0.45      # applied after the discount
vat_rate           = 0.20      # applied last
```

Print exactly five lines:

```
Effective unit cost: £11.73
Retail ex VAT:       £17.01
Retail inc VAT:      £20.41
Order cost:          £3,988.20
Projected revenue:   £6,939.47
```

Where:

- **Effective unit cost** — wholesale cost after the bulk discount.
- **Retail ex VAT** — effective unit cost plus markup.
- **Retail inc VAT** — retail ex VAT plus VAT.
- **Order cost** — what *we* pay: effective unit cost × units.
- **Projected revenue** — what customers pay: retail inc VAT × units.

All money is shown to 2 decimal places with thousands separators.
The label column is padded so the `£` signs align — match it exactly.

---

## Exercise 2 — Pallet planning

The warehouse packs units into cartons, and cartons onto pallets. Anything that
does not fill a whole carton ships loose; anything that does not fill a whole
pallet ships as loose cartons. Nothing is rounded up — a partly-filled carton is
never counted as a full one.

Use exactly these values:

```
raw_units          = "2437"    # as text from the feed
raw_unit_weight_g  = "462"     # grams per unit, as text from the feed
units_per_carton   = 12
cartons_per_pallet = 40
```

Print exactly five lines:

```
Full cartons:  203
Loose units:   1
Full pallets:  5
Loose cartons: 3
Total weight:  1,125.89 kg
```

Note that pallets are counted from the **full cartons only** — loose units never
make it onto a pallet. Total weight covers every unit in the order, loose ones
included, and is given in kilograms to 2 decimal places with thousands
separators.

---

## Exercise 3 — Foreign currency invoice

A European supplier invoices in euros. The bank converts at an agreed rate and
charges a handling fee calculated on the *converted* sterling amount. Finance
wants the true all-in cost, and the effective exchange rate once the fee is
included — because that, not the headline rate, is what the money actually cost.

Use exactly these values:

```
raw_invoice_eur = "8450.00"    # as text from the supplier's system
eur_to_gbp      = 0.853        # agreed conversion rate
fx_fee_rate     = 0.02         # charged on the converted GBP amount
```

Print exactly five lines:

```
Invoice (EUR):   €8,450.00
Converted (GBP): £7,207.85
FX fee:          £144.16
Total (GBP):     £7,352.01
Effective rate:  0.8701
```

**Effective rate** is the total sterling actually paid divided by the euro
invoice amount, shown to 4 decimal places. It is deliberately worse than the
headline `eur_to_gbp` rate — if yours comes out lower, you have divided the
wrong way round.

---

## Exercise 4 — The daily catalogue report

Produce a column-aligned report over three products. This is the exercise where
format specifiers earn their keep: **do not pad anything with manually typed
spaces.** Every column is produced by a width specifier.

Use exactly these values:

```
name_1, raw_cost_1, price_1, raw_qty_1 = "Blue Mug",           "4.99",  9.58,  "3"
name_2, raw_cost_2, price_2, raw_qty_2 = "Oak Chopping Board", "18.50", 41.25, "12"
name_3, raw_cost_3, price_3, raw_qty_3 = "Linen Tea Towel",    "3.20",  7.99,  "140"
```

(If assigning several names on one line is unfamiliar — it was not taught in
Chapter 1 — write them as separate assignments instead. Both are fine.)

The column layout, left to right:

| Column  | Width | Alignment | Number format          |
|---------|-------|-----------|------------------------|
| Product | 20    | left      | —                      |
| Qty     | 5     | right     | whole number           |
| Cost    | 10    | right     | 2 decimals             |
| Price   | 10    | right     | 2 decimals             |
| Total   | 12    | right     | 2 decimals, separators |
| Margin  | 9     | right     | percentage, 1 decimal  |

Print, in order:

1. A header row using those same widths and alignments, with the labels
   `PRODUCT`, `QTY`, `COST`, `PRICE`, `TOTAL`, `MARGIN`.
2. A rule of exactly 66 hyphen characters.
3. One row per product.
4. A final row: the word `TOTAL` left-aligned in **45** characters, followed by
   the sum of the three line totals right-aligned in 12 with 2 decimals and
   thousands separators.

Reminders that decide whether this is right or plausible-but-wrong:

- **Total** is price × quantity.
- **Margin** is profit as a proportion of the *selling price* —
  `(price - cost) / price`. It is not markup. Chapter 1, Example 3.
- Cost and quantity arrive as text and must be converted before use.

The first row of your output should read:

```
Blue Mug                3      4.99      9.58       28.74    47.9%
```

---

## Exercise 5 — Margin against markup

Trading and Finance keep disagreeing about a product's profitability because
they are quoting two different numbers, both of which they call "the profit
percentage". Settle it by printing both, plus the gap between them.

Use exactly these values:

```
raw_cost  = "18.50"   # as text from the feed
raw_price = "41.25"   # as text from the feed
```

Print exactly five lines:

```
Cost:            £18.50
Price:           £41.25
Margin:          55.2%
Markup:          123.0%
Gap:             67.8 percentage points
```

Where:

- **Margin** = profit ÷ price, shown as a percentage to 1 decimal place.
- **Markup** = profit ÷ cost, shown as a percentage to 1 decimal place.
- **Gap** = markup minus margin, expressed in *percentage points* — that is, the
  difference between the two percentages, to 1 decimal place, printed as a plain
  number followed by the words `percentage points` (no `%` sign).

The gap line is the one worth thinking about. A percentage point is not a
percentage; subtracting `0.552` from `1.230` gives a proportion, and you need
that difference rendered as `67.8`, not `0.678` and not `67.8%`. There is more
than one way to get there — choose deliberately.

---

## Exercise 6 — End-of-day till reconciliation

The hardest exercise in this set, and the one that pulls the chapter together.

A shop's till reports its closing cash total as a string of pounds and pence.
The cash office needs that broken down into the exact denominations that make it
up, using the largest denomination possible at each step, so the float can be
counted and checked.

Because this is money, you must **not** do this arithmetic in floats. Convert the
total to a whole number of pennies once, at the start, and do everything after
that in integers. Section 7 of the chapter explains why; this exercise is where
it stops being theoretical.

Use exactly this value:

```
raw_till_total = "1026.86"   # pounds and pence, as text from the till
```

Denominations available, in pennies: 5000 (£50), 2000 (£20), 1000 (£10),
500 (£5), 100 (£1), 50, 20, 10, 5, 2, 1.

Print exactly thirteen lines:

```
Till total: £1,026.86
Pennies:    102686
£50  x 20
£20  x 1
£10  x 0
£5   x 1
£1   x 1
50p  x 1
20p  x 1
10p  x 1
5p   x 1
2p   x 0
1p   x 1
```

Notes that will decide whether this works:

- Denomination labels are **left-aligned in 4 characters**, then ` x `, then the
  count. Note `£50` and `50p` are 3 characters, `£5` and `5p` are 2 — the width
  specifier handles that, you do not type the spaces.
- Denominations with a count of zero are still printed. The cash office needs the
  full breakdown, not the non-empty parts of it.
- `float("1026.86") * 100` does **not** give `102686.0`. It gives
  `102685.99999999999`. Feeding that to `int()` truncates it to `102685` — the
  till is now a penny short and every denomination below it is wrong. This is
  §7 arriving in person. Chapter 1 taught the function that solves it; reach for
  that one, not `int()` alone.
- Each step takes the largest denomination that fits, records how many, and
  carries the remainder forward. `//` and `%` are the whole of the mechanism.

---

## Checklist before submitting

- [ ] Six files: `ex1.py` through `ex6.py`, in `submissions/`.
- [ ] Each prints only the specified lines — no debugging output left behind.
- [ ] Every value given as text was actually converted, not retyped as a number.
- [ ] Every money figure shows exactly 2 decimal places.
- [ ] No column was aligned by typing spaces into a string literal.
- [ ] Each file runs without a traceback: `python3 submissions/exN.py`.
