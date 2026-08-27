# Syllabus Map

Running index of every concept, function, and structure **formally taught** so far.
If something feels unfamiliar during an exercise and it is not listed here, that is
a syllabus gap, not a personal one — flag it.

Last updated: after the Chapter 3 review. Chapter 3 §9 expanded 2026-08-27 —
index-based nested loops were required by Ex.3 but never taught; see review.
Chapter 1 amended 2026-08-20 — string
repetition and literals-in-braces added after gaps were flagged in the Ch.1 review.

---

## Taught

### Chapter 1 — Pricing a Product Feed

**Running a program**
- `.py` files; the `python3` interpreter; top-to-bottom execution
- `micro` for editing (Ctrl+S save, Ctrl+Q quit)

**Values and types**
- `int`, `float`, `str`, `bool`, `NoneType`
- `2` vs `2.0`; `4.99` vs `"4.99"`
- `type(x)` — reporting a value's type
- Literals: `True`, `False`, `None`

**Names**
- Assignment `name = value`; `=` as binding, not equality
- Names as labels on objects, not containers; rebinding moves the label
- Naming rules (no leading digit, no spaces/hyphens, case-sensitive, no keywords)
- Convention: `snake_case`, descriptive names, units in the name

**Comments**
- `#` to end of line; commenting *why*, not *what*

**Arithmetic**
- `+` `-` `*` `/` `//` `%` `**`
- `/` always returns `float`; `//` truncates toward negative infinity
- `//` and `%` as the "how many whole, how many left over" pair
- Operator precedence and parentheses
- Augmented assignment: `+=` `-=` `*=` `/=` `//=` `%=` `**=`

**Float precision**
- Binary representation; `0.1 + 0.2` != `0.3`
- Why displayed money must be rounded or formatted

**Conversion and rounding**
- `int(x)`, `float(x)`, `str(x)` — return new values, do not mutate
- `int("7.5")` raises `ValueError`; `int(7.9)` truncates to `7`
- `round(x)` → `int`; `round(x, n)` → `float`
- Banker's rounding (half-to-even)

**Strings and output**
- `print(...)`, multiple arguments, automatic newline
- Single vs double quotes
- `+` concatenation; `TypeError` on `str + number`
- `*` repetition: `"-" * n`; count may be a name or expression; `0`/negative gives
  `""`; `str * str` is a `TypeError`
- f-strings: `f"…{expression}…"`
- Literals inside the braces: `f"{'PRODUCT':<20}"`; quote nesting (single inside
  double); padding the *label* to a fixed width instead of retuning the number's
- Format specifiers: `.2f`, `.0f`, `,`, `,.2f`, `>n`, `<n`, `^n` (centre), `.1%`
- Which alignment to use: numbers right, text left, short markers centred
- Rounding (changes the value) vs formatting (changes the display)

**Errors**
- Reading a traceback bottom-up
- `NameError`, `TypeError`, `ValueError`, `SyntaxError`

### Chapter 2 — Deciding What to Do With an Order

**Comparison**
- `==` `!=` `<` `>` `<=` `>=` — produce `bool`, usable as values
- `=` (binds) versus `==` (asks) — the latter is an expression
- Equality across types is `False`, not an error; ordering across types is `TypeError`
- `500 == 500.0` is `True`; `500 == "500"` is `False`
- String comparison: lexicographic by character code, case-sensitive; uppercase sorts before lowercase
- Never compare computed floats with `==`; compare `abs(a - b) < tolerance`
- `abs(x)` — built-in, distance from zero
- Chained comparisons: `100 <= x <= 500`

**Boolean logic**
- `and`, `or`, `not` and their truth tables
- Precedence: `not` > `and` > `or`; parenthesise when mixed
- `x == "A" or "B"` is always true — the always-true-or trap
- Short-circuit evaluation, and using it as a guard

**Truthiness**
- Falsy: `False`, `None`, `0`, `0.0`, `""`. Everything else truthy, including `"0"`
- `bool(x)` — fourth conversion function alongside `int()`, `float()`, `str()`
- `if value:` idiom, and when it is wrong (numeric fields where 0 is legitimate)
- `is` versus `==`; `is None` / `is not None` as firm convention
- `None` versus `0` versus `""` versus `False` — all falsy, different meanings

**Branching**
- `if` / `elif` / `else`; the colon; the indented block
- Indentation as syntax: 4 spaces, no tabs, `TabError`, `IndentationError`
- `pass` for a deliberately empty block
- First match wins; branch order is part of the logic
- Chain (alternatives) versus separate `if`s (independent) — and why it matters
- Nesting, and flattening it with `and` or named conditions

**Other**
- Conditional expression: `A if cond else B`
- `in` / `not in` for substring tests (case-sensitive, any position)

### Chapter 3 — Doing It Once for Every Order

**Tuples**
- `(a, b, c)` — one value holding several, in order; type `tuple`
- `len(x)` — item count, also works on strings; empty tuple `()` is falsy
- Indexing `t[0]`, counting from zero; negative indices from the end
- `IndexError` when the position does not exist
- Immutability: `t[0] = x` raises `TypeError`
- The one-item comma: `("GB",)` is a tuple, `("GB")` is a string
- Nesting: a tuple of tuples as a table of rows

**Packing and unpacking**
- `a, b = 1, 2` — packing on the right, unpacking on the left (closes the
  used-before-taught gap from Ch.2)
- Count must match; `ValueError: too many values to unpack`
- The swap `a, b = b, a`, and why it works

**Membership**
- `in` / `not in` against a tuple — replaces chains of `or`
- Distinct from `in` on a string, which tests for a substring

**Iteration**
- `for name in sequence:` — the loop name, the body, one iteration per item
- Looping over tuples and over strings
- Unpacking in the loop header: `for a, b, c in rows:`
- The loop name persists after the loop ends
- Nested loops over two sequences, and the multiplication of work they imply
- Nested loops over **one** sequence by index: `feed[i]` against `feed[j]`
- An inner `range` whose bounds depend on the outer loop variable —
  `range(i + 1, len(x))`, "every position after this one" — and why it removes
  both self-comparison and duplicate pairs; `n × (n − 1) ÷ 2` comparisons
- Pairwise scanning as a recognisable shape: duplicates, collisions, conflicts

**The accumulator pattern**
- Initialise before the loop, update inside, use after
- Sums, counts, and running maxima; `+=` as the core move
- The starting value as a real decision (`0`, `0.0`, `""`, `None`)
- `None` as a sentinel for "nothing seen yet", tested with `is None`

**`range`**
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- Exclusive end, and why it makes `range(len(x))` exactly the valid indices
- When to prefer a direct `for` over `range(len(...))`

**`while`**
- Condition checked before each iteration; may run zero times
- Infinite loops, `Ctrl+C` and `KeyboardInterrupt`
- Choosing `for` versus `while`

**Flow control inside loops**
- `break` — abandon the loop; `continue` — abandon this iteration
- Guard-clause shape: check, report, `continue`
- Both affect only the innermost loop

**Formatting**
- `:+` — force an explicit sign, for signed columns

---

---

## Known siblings, deliberately deferred

These exist, are real, and are coming — they are not gaps.

| Concept | Sibling tools not yet taught | Planned for |
|---------|------------------------------|-------------|
| Money arithmetic | `decimal.Decimal`; integer-pennies as a standing pattern | Modules chapter (Decimal); pennies pattern introduced informally in Ch.1 Ex.6 |
| ~~Repetition~~ | ~~`for`, `while`, `break`, `continue`~~ | **Taught in Chapter 3** |
| Multi-way dispatch | `match` statement (3.10+) | After data structures |
| ~~Membership of several options~~ | ~~`x in (a, b, c)`~~ | **Taught in Chapter 3** |
| Float comparison | `math.isclose()` | Modules chapter |
| String methods | `.strip()`, `.split()`, `.upper()`, `.replace()`, indexing, slicing | Strings chapter |
| Functions | `def`, parameters, `return`, scope | Functions chapter |
| Older string formatting | `%` formatting, `str.format()` | Mentioned when f-strings are revisited; f-strings are the modern default |
| ~~Multiple assignment~~ | ~~`a, b = 1, 2`~~ | **Taught in Chapter 3** — the Ch.2 gap is closed |
| Sequences that change | `list`, `.append()`, indexing assignment | Lists chapter (next) |
| Index with item | `enumerate()` | Lists chapter |
| Finding a position by value | `.index()`, `.count()` | Lists chapter — `.index()` returns only the *first* match, so it does not solve repeat-detection |
| Two sequences in step | `zip()` | Lists chapter |
| Built-in accumulators | `sum()`, `min()`, `max()`, `sorted()` | Lists chapter — after writing them by hand |
| Loop as an expression | comprehensions | After lists and dictionaries |
| Loop with no `break` | `for … else` | Mentioned with searching |
| Lookup by key | `dict` | Dictionaries chapter |
| Input | `input()` | Deferred — exercises use fixed values so grading stays deterministic |

---

## Notes on grading shape

Chapter 1 exercises are graded by running each submission as a script and
comparing standard output exactly. This is because functions have not been
taught yet, so there is nothing to import. Once functions exist, grading moves
to importing and calling them directly, which allows far better edge-case
coverage.
