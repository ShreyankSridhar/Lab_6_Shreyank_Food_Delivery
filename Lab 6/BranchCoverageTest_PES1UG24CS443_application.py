"""Decision and branch tests for the food delivery application."""

import pytest

from food_delivery import apply_coupon, delivery_charge, estimated_time


@pytest.mark.parametrize(
    ("distance", "order_value", "rain", "expected"),
    [
        (2, 200, False, 20),       # Near band, no rain
        (2, 200, True, 50),        # Near band, rain
        (5, 200, False, 40),       # Middle band, no rain
        (5, 200, True, 70),        # Middle band, rain
        (10, 200, False, 60),      # Far band
        (10, 500, False, 0),       # Free delivery
        (10, 500, True, 30),       # Free delivery with rain surcharge
    ],
)
def test_delivery_charge_decision_outcomes(distance, order_value, rain, expected):
    assert delivery_charge(distance, order_value, rain) == expected


@pytest.mark.parametrize("distance", [0, -1, 16])
def test_delivery_charge_rejects_each_invalid_range_path(distance):
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(distance, 200, False)


@pytest.mark.parametrize(
    ("value", "code", "first_order", "expected"),
    [
        (300, None, False, 300),          # No coupon
        (300, "SAVE50", False, 250),      # Known non-WELCOME coupon
        (300, "WELCOME", True, 200),      # First-order WELCOME path
        (150, "SAVE50", False, 150),      # Below the minimum
    ],
)
def test_coupon_valid_decision_paths(value, code, first_order, expected):
    assert apply_coupon(value, code, first_order) == expected


def test_coupon_rejects_unknown_code():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "NOTREAL", True)


def test_welcome_coupon_rejects_non_first_order():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)


@pytest.mark.parametrize(
    ("peak", "busy", "expected"),
    [
        (False, False, 35),
        (True, False, 45),
        (False, True, 50),
        (True, True, 65),
    ],
)
def test_estimated_time_decision_combinations(peak, busy, expected):
    assert estimated_time(5, peak, busy) == expected
