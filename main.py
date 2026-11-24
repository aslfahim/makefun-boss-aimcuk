"""One Word for the Boss — entry writer.

Writes exactly one word describing a boss to entry.txt.
The word is chosen once, below, and the program guards it:
it must be a single whitespace-free word of 1-30 characters,
then the file is read back to prove what landed on disk.
"""

import os
import sys

# The single word this entry submits. The boss IS meetings:
# every decision, delay and "quick sync" in the office runs
# through them, and the calendar is the real org chart.
WORD = "Meetings"

MAX_CHARS = 30


def entry_path() -> str:
    """Resolve where entry.txt goes: OUTPUT_DIR, else /output."""
    base = os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def guard(word: str) -> str:
    """Raise unless `word` is one clean word of 1-30 chars."""
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    if not word:
        raise ValueError("word must not be empty")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word is {len(word)} chars, over the 30-char cap")
    if word != word.strip():
        raise ValueError("word must not have leading/trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    if not word.isalpha():
        raise ValueError("word must be letters only (no punctuation)")
    if not word.isprintable():
        raise ValueError("word must be printable text")
    return word


def write_word(path: str, word: str) -> None:
    """Write the word with no trailing newline, then read it back."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        landed = handle.read()
    if landed != word:
        raise RuntimeError(
            f"read-back mismatch: disk holds {landed!r}, expected {word!r}"
        )


def main() -> int:
    try:
        word = guard(WORD)
        write_word(entry_path(), word)
    except (OSError, ValueError, TypeError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(word)}-char word to {entry_path()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
