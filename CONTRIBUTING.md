# How work gets submitted here

> New to Git and GitHub, or unsure what any of the commands below actually do?
> Read [Appendix A — Git, GitHub, and the Working Loop](https://blazins.github.io/python-mastery/guides/git-and-github.html)
> first. It explains what commits, branches, pull requests and continuous
> integration are, rather than only which commands to type.

This repository is deliberately run like a real project rather than a folder of
homework. Solutions arrive as pull requests, continuous integration grades them
before a human looks, and review happens as inline comments on the diff. The
point is that the *workflow* becomes as familiar as the Python.

## Who commits what

| | |
|---|---|
| **`main`** | Chapter content, exercise sets, test suites, styling. Committed by Claude. Never committed to directly by hand. |
| **`chNN-submissions`** | Your solutions for chapter NN. Yours entirely. |

Platform commits carry a `Co-Authored-By: Claude` trailer so that authorship is
unambiguous — the generated chapter content is visibly not being passed off as
hand-written work, and your solution commits are cleanly your own.

## The loop, per chapter

**1. Read the chapter.** Open `index.html` locally, or the published site.

**2. Branch off main.**

```bash
git switch main
git pull
git switch -c ch01-submissions
```

**3. Write your solutions** into that chapter's `submissions/` directory, in
`micro`, unaided.

```bash
micro syllabus/chapter_01_product_feed/submissions/ex1.py
```

**4. Commit as you go — not in one lump at the end.** Incremental history is
the habit being built; one commit per exercise is a good default.

```bash
git add syllabus/chapter_01_product_feed/submissions/ex1.py
git commit -m "ch01: restock order costing"
```

**5. Run the suite locally before pushing.** Faster than waiting on CI.

```bash
.venv/bin/pytest
```

**6. Push and open a pull request.**

```bash
git push -u origin ch01-submissions
gh pr create --fill
```

**7. CI grades it automatically.** The `Grade submissions` check runs the
chapter's pytest suite. Red means something is objectively wrong — fix it and
push again; the check re-runs on every push.

**8. Review happens on the PR.** Inline comments on specific lines, covering
correctness, edge cases, whether the solution is idiomatic, and whether the
right tool was chosen deliberately rather than landed on by luck. Feedback is
direct and unsoftened, per the syllabus rules. Push fixes onto the same branch
until it is green and approved.

**9. Merge.** The chapter's `review.md` and `progress_log.md` are updated, and
the next chapter opens.

```bash
gh pr merge --squash --delete-branch
git switch main && git pull
```

## What `main` will and will not accept

`main` is protected. Three rules apply:

- **The `pytest` check must pass** before a pull request can be merged. Red
  means the merge button is disabled, not that it is discouraged.
- **Review conversations must be resolved** before merging, so review comments
  cannot be quietly merged past.
- **Force-pushes and branch deletion are refused**, so history on `main` cannot
  be rewritten or lost by accident.

Your branch is yours — none of this applies to it while you work. The rules take
effect at the moment you try to merge into `main`.

## On the test suites

Each chapter ships with a **visible** suite covering the published output spec.
Those run in CI, so the objective feedback loop is immediate and self-service.

A **hidden** set of additional edge cases is held back and run during review.
That preserves the syllabus rule that grading includes cases not shown in
advance — so passing CI means your solution meets the spec, not that it is
finished.

### How these suites are built, and what they may not do

A failing test is a hypothesis, not a verdict. Two rules exist because a broken
check once cost a full day of work and, worse, aimed the blame at the learner:

1. **Tests assert behaviour, not the shape of the source.** What a program
   prints is the specification; how it is written is not. A check that greps for
   `+=`, or for a particular ordering of statements, will eventually reject a
   correct solution that used a different structure — and the learner has no way
   to tell that from being wrong. The only source-level exception is the
   untaught-construct guard, which enforces an actual syllabus rule rather than
   a stylistic preference, and even that inspects code with comments and string
   literals stripped first.

2. **Every suite is validated against at least two structurally different
   solutions** before it ships — not one reference implementation. One correct
   solution passing proves nothing except that the suite fits the way its author
   happened to write it.

If a test fails and the code looks right, say so rather than reshaping the code
to satisfy it. Contorting a correct solution to make a check pass teaches the
wrong lesson twice over.

## Rules for writing exercises

Added 2026-09-06, after Chapter 5 Exercise 3 cost the learner most of an evening
— not on the problem, but on reverse-engineering a defect in the specification
and then absorbing three successive changes to it mid-solve.

**1. Every distinct output line must appear as a worked example in the exercise
text.** Not described — shown. "Reported the same way, with the reason
`malformed`" told a reader that a line exists and nothing about what it says.
If a format only exists inside the reference solution, it is not specified.

**2. A section heading must be able to name everything it contains.** A section
called `DUPLICATES` that must also hold malformed lines is broken before a word
of prose is written, and the contradiction surfaces in the learner's output as
`none` followed by an entry. Fix the design, not the wording.

**3. Read every reference solution's output aloud, on the mutated data as well
as the sample.** "Alan Turing no-brackets-here already signed up as malformed"
is not a sentence. Executing it proved it ran; nobody read it.

**4. Expected output must be derivable from the specification alone.** If
passing requires inferring the reference implementation's internal structure,
the specification is incomplete and the test is wrong to enforce it. A learner
saying "the test contains details the question does not" is reporting a bug.

**5. Never change an exercise the learner is currently solving without asking
first.** Show the defect, lay out the options and their costs, let them choose.
The correctness of the fix does not license the disruption — they have already
built against the old text.

**6. Push immediately after changing anything they work against.** Local commits
on a branch with no upstream mean they are debugging against a file that has
already moved, with no way to see it. That is worse than the original defect.

**7. When the same exercise needs a third correction, stop editing and diagnose
the design.** Successive small fixes to a specification are a signal that the
structure underneath is wrong.

## The rule CI cannot enforce

Attempt everything unaided first. No searching, no reference beyond the chapter
content and `syllabus_map.md`, no AI assistance, no autocomplete. CI checks
whether the code is right; only you know whether it was actually yours. The
entire value of this phase depends on that being true.

If something in an exercise seems to need a tool that was never taught, check
`syllabus_map.md` first. If it is not listed there, that is a syllabus gap —
flag it, and it gets fixed. It is not a signal to go and look it up.
