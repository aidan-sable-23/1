# Tip Calculator

A small Python helper that splits a restaurant bill between people, including tip.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```python
from tip_calculator import split_bill

# Each of 4 people pays $30.00 on a $100 bill with 20% tip
per_person = split_bill(bill=100, tip_percent=20, people=4)
print(per_person)  # 30.0
```

`split_bill(bill, tip_percent, people)` returns each person's share rounded to two decimal places.

- `bill` — pre-tip amount (must be ≥ 0)
- `tip_percent` — tip percentage (must be ≥ 0)
- `people` — number of people (must be ≥ 1)

Invalid values raise `ValueError`.

## Tests

```bash
pytest
```
