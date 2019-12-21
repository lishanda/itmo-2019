# -*- coding: utf-8 -*-

from yumpi.logic.constants import LONG_TIME, SHORT_TIME, WORKDAY


def order_during_working_hours(hour: int) -> bool:
    """Calculates whether current hour is working."""
    return WORKDAY['start'] <= hour <= WORKDAY['end']


def calculate_delivery_time(number_of_pizzas: int, working_hours: bool) -> int:
    """Calculates delivery time for placed :term:`Order`."""
    waiting_time = SHORT_TIME if working_hours else LONG_TIME
    return number_of_pizzas * 10 + waiting_time
