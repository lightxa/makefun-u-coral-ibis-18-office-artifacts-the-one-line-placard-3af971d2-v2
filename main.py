#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.

The placard: a lanyard, recast as the sash of office of the Keeper
of the Fourth Floor, a minor priesthood of access control whose
badge opened no door in the building. Catalogue details (material,
date, provenance, donor) are kept internally consistent, like a real
museum label, and the joke is left to land without explanation.
"""

import os
import sys

PLACARD = (
    "Lanyard, woven nylon, c. 2019. "
    "Sash of the Keeper of the Fourth Floor, "
    "whose badge opened no door in the building. "
    "Donated by the successor."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLACARD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
