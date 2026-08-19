# Syllabus Map

Running index of every concept, function, and structure **formally taught** so far.
If something feels unfamiliar during an exercise and it is not listed here, that is
a syllabus gap, not a personal one — flag it.

Last updated: after Chapter 2.

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
- f-strings: `f"…{expression}…"`
- Format specifiers: `.2f`, `.0f`, `,`, `,.2f`, `>n`, `<n`, `.1%`
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

---

## Known siblings, deliberately deferred

These exist, are real, and are coming — they are not gaps.

| Concept | Sibling tools not yet taught | Planned for |
|---------|------------------------------|-------------|
| Money arithmetic | `decimal.Decimal`; integer-pennies as a standing pattern | Modules chapter (Decimal); pennies pattern introduced informally in Ch.1 Ex.6 |
| Repetition | `for`, `while`, `break`, `continue` | Chapter 3 |
| Multi-way dispatch | `match` statement (3.10+) | After data structures |
| Membership of several options | `x in (a, b, c)` | Chapter 3 (tuples) |
| Float comparison | `math.isclose()` | Modules chapter |
| String methods | `.strip()`, `.split()`, `.upper()`, `.replace()`, indexing, slicing | Strings chapter |
| Functions | `def`, parameters, `return`, scope | Functions chapter |
| Older string formatting | `%` formatting, `str.format()` | Mentioned when f-strings are revisited; f-strings are the modern default |
| Input | `input()` | Deferred — exercises use fixed values so grading stays deterministic |

---

## Notes on grading shape

Chapter 1 exercises are graded by running each submission as a script and
comparing standard output exactly. This is because functions have not been
taught yet, so there is nothing to import. Once functions exist, grading moves
to importing and calling them directly, which allows far better edge-case
coverage.
