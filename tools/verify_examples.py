"""Verify that every code example in a chapter page produces its printed output.

Each `<pre><code>` block is executed and, where the page shows a `<div class="out">`
immediately afterwards, its stdout is compared against that block. Blocks share
one namespace in document order, so an example may build on the one before it —
exactly as a reader following along would experience it.

A code block with no output block after it is an illustrative fragment: a snippet
quoted mid-argument rather than a runnable program. Fragments are still executed,
so that later examples depending on them work, but neither their output nor their
failure is checked.

Expected output ending in an exception line is split: the printed part is compared
as normal, and the error is compared by its final line only, since file names and
line numbers cannot match.

    python tools/verify_examples.py syllabus/chapter_04_keeping/content.html
    python tools/verify_examples.py          # every chapter
"""
import contextlib
import glob
import signal
import html
import io
import re
import sys

CODE = re.compile(r'<pre><code>(?P<code>.*?)</code></pre>', re.S)
OUT = re.compile(r'\s*<div class="out">(?P<out>.*?)</div>', re.S)
ERROR_LINE = re.compile(r'^\w+(Error|Exception|Warning|Interrupt):')
TRACEBACK_NOISE = ('Traceback ', '  File "', '    ', '  ~', '  ^', '~', '^')


def text(fragment):
    """Strip tags, unescape entities, and treat &nbsp; as an ordinary space.

    Chapter pages use non-breaking spaces in output blocks so column alignment
    survives HTML rendering; a running program emits plain spaces.
    """
    plain = html.unescape(re.sub(r'<[^>]+>', '', fragment))
    return plain.replace('\xa0', ' ')


def blocks(page):
    """Yield (code, expected_or_None) for every code block, in document order."""
    for block in CODE.finditer(page):
        following = OUT.match(page, block.end())
        expected = text(following.group('out')).strip('\n') if following else None
        yield text(block.group('code')), expected


def split_expected(expected):
    """Separate expected stdout from an expected exception line, if any."""
    lines = expected.splitlines()
    if not lines or not ERROR_LINE.match(lines[-1].strip()):
        return expected, None
    error = lines[-1].strip()
    body = lines[:-1]
    while body and (not body[-1].strip() or body[-1].startswith(TRACEBACK_NOISE)):
        body.pop()
    return '\n'.join(body), error


class Hung(Exception):
    """Raised when an example runs longer than its time budget."""


def _ring(signum, frame):                   # noqa: ARG001 - signal handler signature
    raise Hung('example exceeded its time budget')


def run(code, namespace, origin, budget=5):
    """Execute one block, capturing stdout, under a wall-clock budget.

    Chapters demonstrate non-terminating loops on purpose — Chapter 3 §7 teaches
    `while True` alongside Ctrl+C and `KeyboardInterrupt` — so a block that never
    returns is an expected input to this tool rather than a fault in it.
    """
    buffer = io.StringIO()
    previous = signal.signal(signal.SIGALRM, _ring)
    signal.alarm(budget)
    try:
        with contextlib.redirect_stdout(buffer):
            exec(compile(code, origin, 'exec'), namespace)
    except BaseException as exc:            # noqa: BLE001 - demonstrating errors is the point
        return buffer.getvalue().strip('\n'), f'{type(exc).__name__}: {exc}'
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)
    return buffer.getvalue().strip('\n'), None


def check(path):
    page = open(path, encoding='utf-8').read()
    namespace, failures, checked = {}, [], 0

    for n, (code, expected) in enumerate(blocks(page), start=1):
        try:
            actual, error = run(code, namespace, f'{path}#block{n}')
        except SyntaxError as exc:
            actual, error = '', f'SyntaxError: {exc}'

        if expected is None:                # illustrative fragment
            continue
        checked += 1
        want_out, want_error = split_expected(expected)

        if want_error is None and error is not None:
            failures.append((n, 'unexpected error', want_out, error))
        elif want_error is not None and error is None:
            failures.append((n, 'expected an error, none raised', want_error, actual))
        elif want_error is not None and error != want_error:
            failures.append((n, 'wrong error', want_error, error))
        elif actual != want_out:
            failures.append((n, 'output mismatch', want_out, actual))

    return checked, failures


def main(argv):
    targets = argv[1:] or sorted(glob.glob('syllabus/*/content.html'))
    total = bad = 0
    for path in targets:
        count, failures = check(path)
        total += count
        bad += len(failures)
        print(f'{path}: {count} examples, {"ok" if not failures else f"{len(failures)} FAILED"}')
        for n, why, expected, actual in failures:
            print(f'  block {n}: {why}')
            print(f'    expected: {expected!r}')
            print(f'    actual  : {actual!r}')
    print(f'\n{total} examples checked, {bad} failing')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
