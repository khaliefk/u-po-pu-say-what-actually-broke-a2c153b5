#!/usr/bin/env python3
"""Say What Actually Broke - make.fun entry.

Writes one single-line software error message to /output/entry.txt.
The line names the real failure (server ran out of memory mid-save),
tells the user plainly what happened and what to do next, and lands
the joke with an image anyone can repeat to a colleague.
"""

import os

ENTRY = (
    "The server ran out of memory mid-save and dropped your work "
    "like a waiter dropping a tray. Nothing was saved, so try again, "
    "we have mopped the floor."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
