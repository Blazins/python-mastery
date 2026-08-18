# Syllabus Map

Running index of every concept, function, and structure **formally taught** so far.
If something feels unfamiliar during an exercise and it is not listed here, that is
a syllabus gap, not a personal one — flag it.

Last updated: after Chapter 1.

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

---

## Known siblings, deliberately deferred

These exist, are real, and are coming — they are not gaps.

| Concept | Sibling tools not yet taught | Planned for |
|---------|------------------------------|-------------|
| Money arithmetic | `decimal.Decimal`; integer-pennies as a standing pattern | Modules chapter (Decimal); pennies pattern introduced informally in Ch.1 Ex.6 |
| Comparison | `==` `!=` `<` `>` `<=` `>=` | Chapter 2 |
| Boolean logic | `and`, `or`, `not`, truthiness of non-bool values | Chapter 2 |
| Branching | `if` / `elif` / `else` | Chapter 2 |
| Repetition | `for`, `while`, `break`, `continue` | Chapter 3 |
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
