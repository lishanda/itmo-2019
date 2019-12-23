# -*- coding: utf-8 -*-

import datetime

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pizzapp.settings import ENABLE_MAILING
from yumpi.logic.constants import BAD_REQUEST_CODE, CREATED_CODE
from yumpi.logic.order_mail import send_mail_on_order
from yumpi.logic.order_statistics import (
    overall_statistics,
    pizza_statistics,
    status_statistics,
)
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
    """
    Displays all :term:`Pizza` instances.

    .. literalinclude:: /user_stories/get_pizzas.feature
        :language: gherkin

    .. versionadded:: 0.1.0
    """

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Displays all :term:`Order` instances."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['POST'])
def post_order(request):
    """
    Posts :term:`Order` and sends email to customer.

    .. literalinclude:: /user_stories/post_order.feature
        :language: gherkin

    .. versionadded:: 0.1.0
    """
    if request.method == 'POST':
        order_data = request.POST.copy()
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            order = Order.objects.get(pk=serializer.data['id'])
            order.save()
            if ENABLE_MAILING:
                send_mail_on_order(order.delivery_time, order.customer_email)
                order.email_sent = True
                order.save()
        if serializer.errors:
            return JsonResponse(serializer.errors, status=BAD_REQUEST_CODE)
        return JsonResponse(serializer.data, status=CREATED_CODE)


@api_view(['GET'])
def get_statistics(request):
    """
    Counts statistics for :term:`Order`.

    .. literalinclude:: /user_stories/get_statistics.feature
        :language: gherkin

    .. versionadded:: 0.1.0
    """
    today = datetime.datetime.today()
    day_ago = today - datetime.timedelta(hours=24)
    orders_today = Order.objects.filter(order_date__gte=day_ago)

    response = {
        'all': overall_statistics(orders_today),
        'pizzas': pizza_statistics(orders_today),
        'statuses': status_statistics(orders_today),
    }
    return Response(response)
