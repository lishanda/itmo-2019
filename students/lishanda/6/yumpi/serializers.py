# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from .models import Ingredient, Order, Pizza


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'title']


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'title', 'price', 'ingredients']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_date', 'pizzas', 'delivery_address',
                  'customer_email', 'status']
