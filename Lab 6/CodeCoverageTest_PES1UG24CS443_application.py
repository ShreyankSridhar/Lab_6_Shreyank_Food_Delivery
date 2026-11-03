"""Line-coverage tests for the food delivery application."""

import pytest

from food_delivery import apply_coupon, delivery_charge, estimated_time


def test_delivery_charge_rejects_distance_at_or_below_zero():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)


def test_delivery_charge_rejects_distance_above_limit():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(16, 200, False)


def test_delivery_charge_free_order_still_gets_rain_surcharge():
    assert delivery_charge(5, 500, True) == 30


def test_delivery_charge_uses_near_distance_band():
    assert delivery_charge(3, 200, False) == 20


def test_delivery_charge_uses_middle_distance_band_and_rain():
    assert delivery_charge(5, 200, True) == 70


def test_delivery_charge_uses_far_distance_band():
    assert delivery_charge(10, 200, False) == 60


def test_apply_coupon_without_code_returns_original_value():
    assert apply_coupon(300, None, False) == 300


def test_apply_coupon_rejects_unknown_code():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "NOTREAL", True)


def test_welcome_coupon_requires_first_order():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)


def test_coupon_below_minimum_order_does_not_apply():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_save50_coupon_applies_to_eligible_order():
    assert apply_coupon(300, "SAVE50", False) == 250


def test_welcome_coupon_applies_to_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_estimated_time_includes_peak_busy_and_combined_adjustments():
    assert estimated_time(5, True, True) == 65

