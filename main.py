#!/usr/bin/env python3
"""Write a 1-280 character 30-day plan to /output/entry.txt (stdlib only)."""
import os

PLAN = (
    "Day 1: list a $29 same-day service on Fiverr and Upwork: AI product-photo "
    "cleanup for Etsy sellers. Find 200 Etsy shops with dull photos, send each "
    "one free fixed sample. Do 3 orders a day, reinvest profit in Fiverr ads, "
    "raise to $49 in week 3. No crypto or inventory."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)

if __name__ == "__main__":
    main()
