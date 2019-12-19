# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from yumpi.models import Ingredient, Order, Pizza


class IngredientSerializer(ModelSerializer):
    """Class for serializing :term:`Ingredient` model."""

    class Meta(object):
        """Setting up serializer for :term:`Ingredient` model."""

        model = Ingredient
        fields = ['id', 'title']


class PizzaSerializer(ModelSerializer):
    """Class for serializing :term:`Pizza` model."""

    class Meta(object):
        """Setting up serializer for :term:`Pizza` model."""

        model = Pizza
        fields = ['id', 'title', 'price', 'ingredients']


class OrderSerializer(ModelSerializer):
    """Class for serializing :term:`Order` model."""

    class Meta(object):
        """Setting up serializer for :term:`Order` model."""

        model = Order
        fields = [
            'id',
            'order_date',
            'pizzas',
            'delivery_address',
            'customer_email',
            'status',
        ]
