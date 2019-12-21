# -*- coding: utf-8 -*-

from datetime import date
from typing import List

from yumpi.models import Ingredient, Order, Pizza

test_date = str(date.today())


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
    order_date: str = test_date,
) -> Order:
    """Creates :term:`Order` object for test purpose."""
    order = Order(
        delivery_address=delivery_address,
        customer_email=customer_email,
        order_date=order_date,
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
