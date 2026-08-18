# Python Mastery

A textbook and graded exercise platform for learning to write Python fluently.

**📖 [Read the chapters](https://blazins.github.io/python-mastery/)**

---

## What this is

Python here is not really the subject — it is the notation. The subject is
problem-solving: recognising what a real problem actually needs, and expressing
that solution correctly.

Each chapter opens with a problem a working developer genuinely encounters —
pricing a supplier feed, planning pallet loads, reconciling a till — and teaches
whatever that problem requires. The structure mirrors how mathematics is taught
well: **theory → worked examples → exercises harder than the examples**, attempted
unaided and submitted the next day.

Two rules shape everything:

- **Content is self-sufficient.** No exercise requires anything the chapters have
  not already taught. If something appears to, that is a gap in the syllabus and
  gets fixed — it is never assumed prior knowledge.
- **Build before you borrow.** Where a chapter is about to introduce a built-in or
  standard-library structure, a simpler version gets built by hand first, so the
  library version is transparent rather than magic.

## How it is graded

Objectively, then qualitatively.

Every chapter ships a `pytest` suite that runs automatically on each pull
request. Passing means a solution meets the published spec. It does not mean the
solution is good — that is decided in review, which covers edge cases beyond the
visible tests, whether the code is idiomatic, and whether the right tool was
chosen deliberately rather than arrived at by luck.

The suites also check *how* a result was reached, not only what was printed. A
script that prints hardcoded answers, or reaches for `int(a / b)` where floor
division is the correct tool, fails — being accidentally correct is not passing.

## Layout

```
index.html                     contents page (the site root)
assets/textbook.css            shared styling
syllabus/chapter_NN_<slug>/
    content.html               theory, diagrams, worked examples
    exercises.md               that chapter's exercise set
    test_chapter_NN.py         objective grading suite
    submissions/               solutions
```

## Running it locally

```bash
python3 -m venv .venv
.venv/bin/pip install pytest
.venv/bin/pytest
```

Chapters are read in a browser; solutions are written in a plain editor and run
in a real terminal. See [CONTRIBUTING.md](CONTRIBUTING.md) for the submission
workflow.
