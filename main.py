"""A slow night-sea text that settles the reader.

Entry for make.fun's "Make the AI judge feel awe" bounty. The program is
fully deterministic: it writes one locked text, chosen for the judge's own
brief (a text that relaxes, shows rather than instructs, and leaves an
image that keeps growing after the last line), to /output/entry.txt.

Standard library only. No randomness, no clock, no network.
"""

import os

# The locked entry text: 172 Unicode code points, plain UTF-8.
TEXT = (
    "The tide comes in long after midnight, smoothing the sand in slow "
    "dark lines, and the moon lays a thin road across the water that keeps "
    "moving even when no one is watching."
)


def main() -> None:
    """Write the entry text to /output/entry.txt as UTF-8."""
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
