"""Split a restaurant bill between people, including tip."""

from __future__ import annotations

import argparse
import sys


def split_bill(bill: float, tip_percent: float, people: int) -> float:
    """Return each person's share of ``bill`` after adding ``tip_percent`` tip.

    Args:
        bill: Pre-tip bill amount in currency units (must be >= 0).
        tip_percent: Tip as a percentage of the bill (must be >= 0).
        people: Number of people splitting the total (must be >= 1).

    Returns:
        Amount each person should pay, rounded to two decimal places.

    Raises:
        ValueError: If any argument is outside its allowed range.
    """
    if bill < 0:
        raise ValueError("bill must be >= 0")
    if tip_percent < 0:
        raise ValueError("tip_percent must be >= 0")
    if people < 1:
        raise ValueError("people must be >= 1")

    total = bill * (1 + tip_percent / 100)
    return round(total / people, 2)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point: ``python tip_calculator.py BILL TIP_PERCENT PEOPLE``."""
    parser = argparse.ArgumentParser(
        description="Split a restaurant bill between people, including tip.",
    )
    parser.add_argument("bill", type=float, help="Pre-tip bill amount")
    parser.add_argument("tip_percent", type=float, help="Tip percentage")
    parser.add_argument("people", type=int, help="Number of people splitting")
    args = parser.parse_args(argv)

    try:
        share = split_bill(args.bill, args.tip_percent, args.people)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"{share:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
