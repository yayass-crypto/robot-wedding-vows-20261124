"""One-Line Robot Wedding Vows entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The gate requires UTF-8 text of 1 to 160
characters, not only white space, on one line.
"""

import os

ENTRY = (
    "I vow to love you, honour you, and trust the cloud to hold you "
    "after we rust, because heaven runs on unlimited storage."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
