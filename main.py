"""Entry for make.fun bounty: The plan make.fun will carry out in public.

Writes the 30-day plan (278 characters, verbatim) to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

PLAN = (
    "Sell $49 24h AI ad creatives to Shopify stores already running Meta ads. "
    "Day 1: list 200 from Meta Ad Library; email 30/day: 3 UGC-style ads, "
    "$49, 24h delivery, money-back. Cost ~$2/ad. Close 2/day from day 6 = "
    "$98/day. Reinvest profit in outreach. Target ~$1,500 net by day 30."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
