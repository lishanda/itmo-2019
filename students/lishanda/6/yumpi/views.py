# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ingredient, Order, Pizza
from .serializers import IngredientSerializer, OrderSerializer, PizzaSerializer


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


def overall_statistics(orders):
    """Counts all :term:`Order`s."""
    return orders.count()


def pizza_statistics(orders):
    """Counts different Pizza types."""
    pizzatype_dict = {}
    for order in orders:
        for pizza in order.pizzas.all():
            try:
                pizzatype_dict[pizza.id] += 1
            except KeyError:
                pizzatype_dict[pizza.id] = 1
    return pizzatype_dict


def status_statistics(orders):
    """Counts different statuses of orders."""
    choices = Order._meta.get_field('status').choices  # noqa: WPS437
    statuses = [choice[0] for choice in choices]
    status_dict = dict.fromkeys(statuses)
    for status in statuses:
        status_dict[status] = orders.filter(status=status).count()
    return status_dict
