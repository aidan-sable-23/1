"""Split a restaurant bill between people, including tip."""

from __future__ import annotations


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
