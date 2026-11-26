#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary: one word, erased forever.

Readers flinch at it before they finish reading it, every single time.
Nothing is attached to it; the word has to do all the work alone.
Delete it and nobody would ever miss it — that is the whole point.
"""

import sys

# The entry never changes: it is the whole submission, fixed in advance.
# Every check below exists only to prove this one word is well formed
# before it is written out. Nothing here reads input, touches the
# network, rolls dice, or looks at the clock.
ENTRY = 'moist'
LIMIT = 77
TARGET = "/output/entry.txt"
EMDASH = "\u2014"
MIN_VOWELS = 2


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def check_lowercase_word(text):
    """True when the entry is one lowercase word of letters only."""
    return text.isalpha() and text == text.lower()


def check_nonempty(text):
    """True when trimming the entry leaves something behind."""
    return len(text.strip()) > 0


def check_vowels_enough(text):
    """True when at least MIN_VOWELS vowels keep the word sayable."""
    vowels = [ch for ch in text.lower() if ch in "aeiou"]
    return len(vowels) >= MIN_VOWELS


def check_length_ok(text):
    """True when the entry fits inside the character limit."""
    return len(text) <= LIMIT


def check_letters_present(text):
    """True when the entry holds at least one letter."""
    return any(ch.isalpha() for ch in text)


def check_printable(text):
    """True when every character is printable, none a control code."""
    return all(32 <= ord(ch) <= 126 or ord(ch) > 126 for ch in text)


def check_one_word(text):
    """True when the trimmed entry holds exactly one word."""
    return len(text.strip().split()) == 1


def check_trimmed(text):
    """True when no leading or trailing space survives."""
    return text.strip() == text


def check_not_all_digits(text):
    """True when the trimmed entry is not made of digits alone."""
    stripped = text.strip()
    return len(stripped) > 0 and not stripped.isdigit()


def check_clean_spacing(text):
    """True when no double space or newline hides inside the entry."""
    return text.find("  ") == -1 and text.find("\n") == -1


# Each row is a short name, the check that must hold, and the complaint
# printed when it does not. The order below is the order the checks run.
RULES = [
    ("lowercase_word", check_lowercase_word, "entry must be one lowercase word"),
    ("nonempty", check_nonempty, "entry is empty"),
    ("vowels_enough", check_vowels_enough, "entry must contain at least two vowels"),
    ("length_ok", check_length_ok, "entry is longer than the limit"),
    ("letters_present", check_letters_present, "entry has no letters"),
    ("printable", check_printable, "entry has control characters"),
    ("one_word", check_one_word, "entry must be a single word"),
    ("trimmed", check_trimmed, "entry has leading or trailing space"),
    ("not_all_digits", check_not_all_digits, "entry is digits only"),
    ("clean_spacing", check_clean_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Walk RULES top to bottom; the first failed check stops the run."""
    for index, (slug, check, message) in enumerate(RULES):
        try:
            ok = check(text)
        except Exception:
            ok = False
        if not ok:
            fail(f"rule {index + 1} [{slug}]: {message}")


def emit(text):
    """Write the validated entry plus a trailing newline to TARGET."""
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main():
    """Validate the fixed entry, then emit it."""
    validate(ENTRY)
    emit(ENTRY)


if __name__ == "__main__":
    main()
