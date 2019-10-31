# -*- coding: utf-8 -*-

from __future__ import unicode_literals  # noqa: WPS422

from datetime import date
from enum import Enum

from django.db import models

CHAR_LENGTH = 64


class Ingredient(models.Model):
    """A model that defines :term:`Ingredient` object."""

    title = models.CharField(max_length=CHAR_LENGTH)

    def as_dict(self):
        """Returns :term:`Ingredient` model dict representation."""
        return {
            'id': self.pk,
            'title': self.title,
        }

    def __str__(self):
        """Returns string representation of :term:`Ingredient`."""
        return self.title


class Pizza(models.Model):
    """A model that defines :term:`Pizza` object."""

    title = models.CharField(max_length=CHAR_LENGTH)
    price = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)

    def as_dict(self):
        """Returns :term:`Pizza` model dict representation."""
        ingr_list = self.ingredients.all()
        return {
            'id': self.pk,
            'title': self.title,
            'price': self.price,
            'ingredients': [ingredient.as_dict() for ingredient in ingr_list],
        }

    def __str__(self):
        """Returns string representation of :term:`Pizza`."""
        return self.title


class OrderType(Enum):
    """A model that represents status of :term:`Order` object."""
    Accepted = 'Accepted'
    Cooking = 'COOKING'
    Delivery = 'DELIVERY'
    Finished = 'FINISHED'

    def __str__(self):
        """Returns OrderType string representation."""
        return self.value


class Order(models.Model):
    """A model that defines :term:`Order` object."""

    order_date = models.DateField(default=date.today)
    pizzas = models.ManyToManyField(Pizza)
    delivery_address = models.CharField(max_length=2 * CHAR_LENGTH)
    customer_email = models.CharField(max_length=CHAR_LENGTH)
    status = models.CharField(
        max_length=int(CHAR_LENGTH / 4),
        choices=[(st.value, st.value) for st in OrderType],
    )

    def as_dict(self):
        """Returns :term:`Order` model dict representation."""
        return {
            'order_date': self.order_date,
            'pizzas': [pizza.as_dict() for pizza in self.pizzas.all()],
            'delivery_address': self.delivery_address,
            'customer_email': self.customer_email,
            'status': str(self.status[1]),
        }

    def __str__(self):
        """Returns string representation of :term:`Order`."""
        return 'Ordered {0}. Status: {1}'.format(self.order_date, self.status)
