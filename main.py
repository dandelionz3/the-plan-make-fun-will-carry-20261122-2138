#!/usr/bin/env python3
"""Entry for the-plan-make-fun-will-carry-20261122-2138.

When run, writes a 1-280 character plan to /output/entry.txt.
"""

from pathlib import Path

PLAN = (
    "Day 1: spend $20 on API credits. Find Etsy shops with 0-20 sales and weak "
    "titles/photos, email 40/day with 1 free rewritten title as proof: $49 for "
    "full titles, tags + 5 AI mockups in 24h, via Stripe link. Upsell $99 shop "
    "revamp. 2/day by week 2 = ~$98/day; reinvest in outreach."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
