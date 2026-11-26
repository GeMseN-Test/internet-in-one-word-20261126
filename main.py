#!/usr/bin/env python3
"""The Internet in One Word -- make.fun entry.

The whole entry is one word. This program writes that word to
/output/entry.txt, where the sealed scorer reads it: UTF-8 text of
1 to 30 characters, not only white space.
"""

import os

# "Ballyhoo" means loud, sensational hype about nothing much at all --
# a single punchy word that captures the entire internet in one beat.
WORD = "Ballyhoo"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
