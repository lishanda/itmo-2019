# -*- coding: utf-8 -*-

from typing import List

from yumpi.models import Ingredient, Order, Pizza

default_dataset = {
    'ingredient': ['Cheese', 'Chicken', 'Tomato', 'Bacon'],
    'pizza': [
        ('Margaret', 100, [1]),
        ('Classic', 120, [1, 2]),
        ('Megameat', 140, [1, 2, 3, 4]),
    ],
    'order': [
        ([1, 2, 3], 'Nevskii pr., 12', 'customer@real.com'),
        ([1], 'Sovetkaja ul., 120', 'pizza@lover.ru'),
    ],
}


def create_test_ingredient(title: str) -> Ingredient:
    """Creates :term:`Ingredient` object for test purpose."""
    ingredient = Ingredient(title=title)
    ingredient.save()
    return ingredient


def create_test_pizza(title: str, price: int, ingredients: List[int]) -> Pizza:
    """Creates :term:`Pizza` object for test purpose."""
    pizza = Pizza(
        title=title,
        price=price,
    )
    pizza.save()
    pizza.ingredients.set(ingredients)
    return pizza


def create_test_order(
    pizzas: List[int],
    delivery_address: str,
    customer_email: str,
) -> Order:
    """Creates :term:`Order` object for test purpose."""
    order = Order(
        delivery_address=delivery_address,
        customer_email=customer_email,
    )
    order.save()
    order.pizzas.set(pizzas)
    return order


def create_test_data(dataset) -> None:
    """Fills test database with data for test purpose."""
    for ingredient in dataset['ingredient']:
        create_test_ingredient(ingredient)
    for pizza in dataset['pizza']:
        create_test_pizza(*pizza)
    for order in dataset['order']:
        create_test_order(*order)
