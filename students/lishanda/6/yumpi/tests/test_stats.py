from django.test import TestCase
from django.http import HttpRequest

from ..models import *
from ..views import api


class TestStats(TestCase):

    def decode_json(self, json_response):
        return json_response._container[0].decode('utf-8')

    def test_empty_stats(self):
        res = api.stats(HttpRequest())
        self.assertEqual(self.decode_json(res),
                         '{"total_orders": 0, "accepted_orders": 0, "cooking_orders": 0, "delivery_orders": 0, "completed_orders": 0, "ordered_pizzas": []}')

    def test_accepted_stats(self):
        cheese = Ingredient(title='Cheese')
        cheese.save()

        pizza = Pizza(id=1, title='CheesyPizza', price=10)
        pizza.save()

        pizza.ingredients.set([cheese])

        order = Order(
            delivery_address='address',
            customer_email='e@ma.il',
            status=OrderType.Accepted
        )
        order.save()
        order.pizzas.set([pizza])

        res = api.stats(HttpRequest())
        self.assertEqual(self.decode_json(res),
                         '{"total_orders": 1, "accepted_orders": 1, "cooking_orders": 0, "delivery_orders": 0, "completed_orders": 0, "ordered_pizzas": [{"pizza_title": "CheesyPizza", "count": 1}]}')