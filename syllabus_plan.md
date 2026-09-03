# Syllabus Plan — Chapters 6 to 31

Reverse-engineered from two things rather than from a generic curriculum: the
**Canonical Python Engineer** role description, and the **Python codebases
Canonical actually maintains**. Written 2026-09-03, after Chapter 5.

## Why the shape changed

The original syllabus aimed at ML engineering, which justified graphs, trees and
algorithm depth. The near target is now a systems-and-infrastructure Python role,
so the weighting moves: **less algorithm theory, far more production Python.**

Two evidence sources decided the sizing.

**Reported Canonical technical questions.** Merging sorted arrays. Evaluating
Reverse Polish Notation. Partitioning strings into fixed-size groups. And this
one, which is worth reading twice:

> *"Write a Python script that parses a large log file **asynchronously**,
> extracts specific error metrics, and outputs a structured **JSON** report."*

That single question spans files, JSON, streaming and asyncio. It is a better
statement of the target than any syllabus outline.

**The codebases.** Canonical's Python is `cloud-init`, `snapcraft`, MAAS,
Landscape and Launchpad. (Juju and LXD are **Go** — worth knowing before
spending a weekend on them.) What those repositories are made of: CLI tools,
YAML and JSON config parsing, subprocess and system interaction, HTTP APIs,
heavy pytest, and packaging. The professional-Python block below is that list.

**What is cut, and why:** trees, graphs, dynamic programming, balancing, linked
lists as a topic. None appear in any reported Canonical interview, and none
appear in the role description. They return if the ML arc resumes.

---

## The plan — 26 chapters, 68 days of chapter work

### Core language — 12 chapters, 29 days

| # | Chapter | Days |
|---|---------|------|
| 6 | Dictionaries — lookup by key, counting, grouping | 3 |
| 7 | Sets — membership, dedup, set algebra | 1 |
| 8 | Comprehensions — and when not to | 2 |
| 9 | Functions I — `def`, parameters, return, scope | 3 |
| 10 | Functions II — first-class functions, `key=`, closures | 2 |
| 11 | Exceptions — `try`/`except`/`raise`, EAFP, custom types | 3 |
| 12 | Files and I/O — `open`, `with`, paths, large files, CSV | 3 |
| 13 | JSON and structured data | 2 |
| 14 | Modules and program structure — packages, `__main__` | 2 |
| 15 | Classes I — state, `__init__`, methods | 3 |
| 16 | Classes II — dunders, properties, dataclasses | 3 |
| 17 | Composition versus inheritance | 2 |

### Data structures and algorithms — 4 chapters, 11 days

Right-sized to the evidence. Competent-engineer level, not competitive
programming.

| # | Chapter | Days | Directly interview-tested |
|---|---------|------|---------------------------|
| 18 | Iterators and generators — laziness, streaming | 3 | "parses a **large** log file" |
| 19 | Recursion — and when not to | 2 | — |
| 20 | Stacks and queues — RPN evaluation, `deque` | 3 | **Reverse Polish Notation** |
| 21 | Searching, sorting, complexity | 3 | **merging sorted arrays** |

### Professional Python — 10 chapters, 28 days

This is the block the old syllabus lacked entirely, and it is what the role
actually asks for.

| # | Chapter | Days | Why |
|---|---------|------|-----|
| 22 | Type hints and `mypy` | 2 | "thoroughly designed, modern" Python |
| 23 | Testing properly — fixtures, parametrize, coverage | 3 | "comprehensively tested"; "deep quality and test engineering" |
| 24 | Decorators and context managers — writing your own | 3 | Everywhere in the codebases |
| 25 | CLI tools — `argparse`, exit codes, stdin/stdout | 2 | "tastefully presented in its CLI"; snapcraft is a CLI |
| 26 | Logging and configuration | 2 | cloud-init, MAAS, Landscape are configuration engines |
| 27 | Packaging and distribution — `pyproject`, entry points | 2 | Debian/Ubuntu packaging listed; snapcraft *is* packaging |
| 28 | Concurrency — threads, `asyncio`, async I/O | 4 | Named explicitly in a reported interview question |
| 29 | HTTP and APIs — consuming and serving | 3 | "REST and gRPC API experience" |
| 30 | Databases — SQL and `sqlite3` | 2 | "SQL and NoSQL data store expertise" |
| 30b | **Python and the system** — `subprocess`, `pathlib`, permissions, processes, environment, exit codes | 3 | **New, 2026-09-03.** Linux appears in nearly every reported technical round: *permissions, shell commands, processes, services, links, containers, troubleshooting* |
| 31 | Capstone — multi-module CLI, typed, tested, packaged | 5 | The portfolio artifact and the written-interview material |

---

## Priority correction — 2026-09-03

520 aggregated candidate reports establish that **the written interview, the
psychometric tests and the timed technical assessment are the main gate**, and
that most rejections happen before any human conversation. Topic prominence
across reported loops: Python 96%, **Written Assessments 94%**, problem solving
82%, GIA 75%, psychometric 72%, aptitude 70%.

The chapters below are gate four. **Three things now run in parallel with them,
starting immediately, because they are cheap and they are where candidates are
actually eliminated:**

1. **The written-interview file.** Add to it monthly rather than writing 10–20
   pages in one sitting. Motivation, projects and the decisions inside them,
   open-source philosophy, education history, STAR examples.
2. **Timed browser coding, no IDE.** Short sessions, increasing in frequency
   near application time. The DevSkiller assessment is reported at **1h 25m**,
   and at least one loop had a **separate Python take-home** as well.
3. **GIA practice.** Timed, speed-sensitive, and practisable. Cheap to improve.

**Linux fluency is a fourth parallel track**, and mostly not a Python-syllabus
topic. Chapter 30b covers the Python-facing half; the shell half — permissions,
processes, services, symlinks, systemd, troubleshooting — is daily practice on a
machine he already runs, not a chapter.

## Assessment

Two formats, because **Canonical uses both** and they test different things.

- **Timed closed-book exam, ~2 hours, four of them** (after chapters 11, 17, 21,
  27). This is the DevSkiller assessment: browser editor, no IDE, fundamentals
  under time pressure. Tests recall.
- **Take-home project, 5 days, three of them** (after the core language, the
  DSA block, and the professional block). This is Automattic's entire hiring
  process, and it produces both a portfolio artifact and the "favourite projects,
  and why you built them that way" material the Canonical written interview
  demands. Tests synthesis.

Budget: 8 days of exams, 15 of take-homes. **Total 91 days.**

---

## Timeline

| Slippage | Syllabus done | Apply (after 2–3 months building) |
|----------|---------------|-----------------------------------|
| On plan | **4 Dec 2026** | Feb–Mar 2027 |
| +20% | 22 Dec 2026 | Feb–Mar 2027 |
| +40% | 9 Jan 2027 | Mar–Apr 2027 |

Current measured pace is 3.5 days per chapter against these estimates, so **+20%
is the honest planning assumption**, not the optimistic one.

Note how little the apply date moves. Forty per cent slippage across four months
costs roughly one month at the end, because the build phase dominates the tail.
**The lever is not working faster — it is not adding scope.**

---

## Contribution targets, when Phase 2.5-equivalent arrives

Python, and therefore relevant:

- **`canonical/cloud-init`** — system initialisation, config parsing, cloud
  provider integration, heavy test suite
- **`canonical/snapcraft`** — the packaging CLI; a large, well-tested Python
  command-line tool
- **MAAS**, **Landscape**, **Launchpad** — larger, more involved

Not Python, do not spend weekends here: **Juju** and **LXD** are Go.
