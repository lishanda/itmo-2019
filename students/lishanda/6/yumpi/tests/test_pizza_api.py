from django.test import TestCase

from ..models import *
from ..views import api


class TesPizzaApi(TestCase):

    def decode_json(self, json_response):
        return json_response._container[0].decode('utf-8')

    def test_no_pizzas(self):
        self.assertEqual(self.decode_json(api.get_pizzas(None)), '{"pizzas": []}')

    def test_get_pizzas(self):
        cheese = Ingredient(title='Cheese')
        cheese.save()

        pizza = Pizza(id=1, title='CheesyPizza', price=10)
        pizza.save()

        pizza.ingredients.set([cheese])

        self.assertEqual(self.decode_json(api.get_pizzas(None)),
                         '{"pizzas": [{"id": 1, "title": "CheesyPizza", "price": 10, "ingredients": [{"id": 1, "title": "Cheese"}]}]}')
