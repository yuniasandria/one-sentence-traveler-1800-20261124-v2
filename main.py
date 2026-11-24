"""One Sentence for a Traveler from 1800 (v2).

Writes a single sentence explaining the modern internet to a reader
from 1800, using only words and pictures from that year, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR when set).
Pure Python standard library only.
"""

import os

PART_A = "Imagine a book that holds more books than any man could read in a hundred lifetimes, "
PART_B = "and when you whisper a question to it, it opens to the very page that answers."

SENTENCE = PART_A + PART_B


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
