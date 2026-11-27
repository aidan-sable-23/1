"""Tests for tip_calculator.split_bill and CLI."""

import pytest

from tip_calculator import main, split_bill


def test_even_split_with_tip():
    # $100 + 20% tip = $120 / 4 people = $30.00
    assert split_bill(100, 20, 4) == 30.00


def test_zero_tip():
    assert split_bill(90, 0, 3) == 30.00


def test_single_person():
    assert split_bill(50, 15, 1) == 57.50


def test_rounds_to_two_decimals():
    # $10 + 15% = $11.50 / 3 ≈ 3.833... → 3.83
    assert split_bill(10, 15, 3) == 3.83


def test_zero_bill():
    assert split_bill(0, 20, 2) == 0.00


@pytest.mark.parametrize(
    "bill, tip_percent, people, match",
    [
        (-1, 20, 2, "bill"),
        (100, -5, 2, "tip_percent"),
        (100, 20, 0, "people"),
        (100, 20, -1, "people"),
    ],
)
def test_invalid_inputs_raise(bill, tip_percent, people, match):
    with pytest.raises(ValueError, match=match):
        split_bill(bill, tip_percent, people)


def test_cli_prints_per_person_share(capsys):
    # $120 + 18% tip = $141.60 / 3 people = $47.20
    exit_code = main(["120", "18", "3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "47.20"
