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

**Exams every 4 chapters, starting immediately after Chapter 5.** Seven across
the plan: after chapters **5**, 9, 13, 17, 21, 25 and 29. Two hours, closed
book, browser editor or `micro` with no reference material — the DevSkiller
format. Frequent low-stakes retrieval beats infrequent high-stakes examination
for retention, and a bad result costs less to repair when each exam covers less.

**Exam 1 comes first, and it is overdue.** Chapters 1–5 are complete and none
has been examined. Three reasons it should not wait for Chapter 9:

1. **There is no closed-book data at all.** Every assessment so far has been
   open book, unlimited time, with a diagnostician available. Everything
   believed about ability is measured under conditions that will not exist in a
   real technical assessment.
2. **Retention across Chapters 1–3 is untested** and those chapters are weeks
   old. Two `weak_spots.md` entries have clearing conditions that explicitly
   require re-testing, and the Ex.5 cold redo is already logged as pending. One
   exam subsumes all of it.
3. **Sitting a timed closed-book exam is itself a skill** — pacing, not freezing
   on a blank editor, choosing what to attempt first. Learn it on material
   already known, not on generators and asyncio.

Chapters 1–5 are a coherent boundary in their own right: everything needed to
**parse, transform and report on data** without dictionaries, functions or
classes.

**Three take-home projects**, five days each, after roughly chapters 15, 21 and
31.

### What a take-home is for

**Testing integration, first and only.** Portfolio value is a welcome
by-product, not the objective. These are not attempts at a real open-source tool
— a genuinely-used tool is friction-driven, long-horizon and usually
collaborative, and pretending a five-day exercise can be one produces exactly
the pet project this is meant to avoid.

### The standard — pet projects versus finished work

**A pet project is an unfinished sketch of an ambitious idea. The opposite is not
a bigger idea; it is a smaller idea, finished to production standard.**

A todo app fails as portfolio evidence not because the subject is trivial, but
because it is a demo — no tests, no packaging, no error handling, a README
saying `run python main.py`. A *small* tool that is genuinely finished is rare,
and rarity is what gets noticed.

Canonical states the rubric themselves: *"a great product is more than code —
it is ready for the unexpected, it is well documented, it is comprehensively
tested, it is tastefully presented in its CLI."*

### Delivery requirements — every take-home, regardless of subject

| | Requirement |
|---|---|
| **Form** | A **CLI tool**. Canonical's Python is CLI-shaped — snapcraft is a command-line tool. Not a web app |
| **Install** | `pip install .` then a working command. One step, no instructions beyond it |
| **Input** | Real, messy input — text, config, logs. Never a hand-tidied fixture |
| **Failure** | Every failure mode handled and reported usefully. Non-zero exit codes. Nothing crashes with a traceback |
| **Tests** | pytest, meaningful cases, including the branches the sample data never reaches |
| **Types** | Annotated throughout; `mypy` clean (from Ch.22) |
| **Structure** | Multi-module with a real package layout. Not one file |
| **Docs** | README: what problem, how to install, how to run, worked example, and **scope — what it deliberately does not do** |
| **Decisions** | A section stating what was chosen, what was rejected, why, and **what would change the answer at ten thousand times the input**. Three independent sources name this as the deciding interview signal |
| **History** | Real incremental commits with messages that explain why. The repository is evidence too |

### Choosing subjects

Deferred, deliberately. Each take-home's subject is picked when its chapters are
done — informed by what has actually been taught and by the **friction log**
(see below). Choosing now would mean designing an exercise for skills that do
not yet exist.

Shape by stage, as a guide rather than a specification:

- **After ~Ch.15** — parse messy real input, validate it, report. Multi-module,
  tested, packaged. Core language integration.
- **After ~Ch.21** — something with streaming or large input where the
  algorithm and its cost actually matter.
- **After Ch.31** — the full instrument: packaged CLI, typed, tested, logged,
  configurable, concurrent where warranted, talking to something over HTTP.

### The friction log — separate, and long-horizon

Not a take-home. A running file, one dated line each time something in daily
work is awkward, unclear, needs a workaround, or prompts *"why isn't there a
tool for this"* — in Ubuntu, in Python tooling, in packaging, anywhere.

By Chapter 20 it holds dozens of entries and three to five are real candidates.
This is how usable tools actually get found; almost none are brainstormed. The
open-source contributions are the other half of the reconnaissance — working
inside `cloud-init` or `snapcraft` shows where the gaps are and what users
complain about, which cannot be seen from outside.

If a take-home subject and a friction-log entry happen to coincide, take it.
Do not force it.



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
