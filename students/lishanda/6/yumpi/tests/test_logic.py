# -*- coding: utf-8 -*-

from unittest import TestCase

from hypothesis import example, given
from hypothesis.strategies import integers

from yumpi.logic.constants import WORKDAY
from yumpi.logic.order_time import (
    calculate_delivery_time,
    order_during_working_hours,
)


class TestWorkingHours(TestCase):
    """Testing order_during_working_hours function."""

    @given(integers(WORKDAY['start'], WORKDAY['end']))
    def test_working_hours(self, hour):
        """Testing at working hours."""
        assert order_during_working_hours(hour)

    @given(integers(WORKDAY['midnight'], WORKDAY['start'] - 1))
    @example(WORKDAY['end'] + 1)
    def test_not_working_hours(self, hour):
        """Testing at morning/night hours."""
        assert not order_during_working_hours(hour)


class TestDeliveryTime(TestCase):
    """Testing calculate_delivery_time function."""

    test_values = [
        (0, False, 60),
        (0, True, 40),
        (1, False, 70),
        (1, True, 50),
        (2, True, 60),
        (10, False, 160),
    ]

    def test_calculation(self):
        """Testing correctness of calculations."""
        for num, working_hours, answer in self.test_values:
            assert calculate_delivery_time(num, working_hours) == answer
