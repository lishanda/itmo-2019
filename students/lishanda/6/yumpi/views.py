# -*- coding: utf-8 -*-

import datetime
from typing import Dict

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from yumpi.models import Ingredient, Order, Pizza
from yumpi.serializers import (
    IngredientSerializer,
    OrderSerializer,
    PizzaSerializer,
)


class IngredientViewSet(viewsets.ModelViewSet):
    """Displays all :term:`Ingredient` instances."""

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """Displays all :term:`Pizza` instances."""

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Displays all :term:`Order` instances."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET'])
def get_statistics(request):
    """Counts statistics for :term:`Order`."""
    today = datetime.datetime.today()
    day_ago = today - datetime.timedelta(hours=24)
    orders_today = Order.objects.filter(order_date__gte=day_ago)

    response = {
        'all': overall_statistics(orders_today),
        'pizzas': pizza_statistics(orders_today),
        'statuses': status_statistics(orders_today),
    }
    return Response(response)


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
