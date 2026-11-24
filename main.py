"""Entry for u-suga-two-lines-to-your-past-self-f36c83ca.

Writes two lines to /output/entry.txt, the path the sealed scorer
reads. Line 1 warns the writer's past self about one specific moment,
a 2 a.m. text on 14 March 2019; line 2 says why that moment mattered
and what changed because of it.
"""

import os

ENTRY = (
    "Do not send that 2 a.m. text to Maya on 14 March 2019, the one that "
    "starts with 'we need to talk' and ends the friendship before "
    "sunrise.\n"
    "That message bought you three silent years and a birthday spent "
    "alone, while the apology you never sent would have cost you one "
    "honest minute."
)

MAX_CHARS = 280


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "no line may be blank"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
