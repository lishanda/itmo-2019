# -*- coding: utf-8 -*-

from typing import Dict

from yumpi.models import Order


def overall_statistics(orders) -> int:
    """Counts all :term:`Order` instances."""
    return orders.count()


def pizza_statistics(orders) -> Dict[str, int]:
    """Counts different :term:`Pizza` types."""
    pizzatype_dict: Dict[str, int] = {}
    for order in orders:
        for pizza in order.pizzas.all():
            try:
                pizzatype_dict[pizza.id] += 1
            except KeyError:
                pizzatype_dict[pizza.id] = 1
    return pizzatype_dict


def status_statistics(orders) -> Dict[str, int]:
    """Counts different statuses of :term:`Order` instances."""
    choices = Order._meta.get_field('status').choices  # noqa: WPS437
    statuses = [choice[0] for choice in choices]
    status_dict = dict.fromkeys(statuses)
    for status in statuses:
        status_dict[status] = orders.filter(status=status).count()
    return status_dict
