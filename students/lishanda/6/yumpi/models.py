# -*- coding: utf-8 -*-

from datetime import date, datetime
from enum import Enum

from django.db import models

from yumpi.logic.order_time import (
    calculate_delivery_time,
    order_during_working_hours,
)

CHAR_LENGTH = 64


class Ingredient(models.Model):
    """A model that defines :term:`Ingredient` object."""

    title = models.CharField(max_length=CHAR_LENGTH)

    def __str__(self):
        """Returns string representation of :term:`Ingredient`."""
        return self.title


class Pizza(models.Model):
    """A model that defines :term:`Pizza` object."""

    title = models.CharField(max_length=CHAR_LENGTH)
    price = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        """Returns string representation of :term:`Pizza`."""
        return self.title


class OrderType(Enum):
    """A model that represents status of :term:`Order` object."""

    def __str__(self):
        """Returns OrderType string representation."""
        return self.value


class Order(models.Model):
    """A model that defines :term:`Order` object."""

    order_date = models.DateField(default=date.today)
    pizzas = models.ManyToManyField(Pizza)
    delivery_address = models.CharField(max_length=2 * CHAR_LENGTH)
    customer_email = models.EmailField(max_length=CHAR_LENGTH)
    email_sent = models.BooleanField(default=False)
    status = models.CharField(
        max_length=CHAR_LENGTH // 4,
        choices=[
            ('ACCEPTED', 'ACCEPTED'),
            ('COOKING', 'COOKING'),
            ('DELIVERY', 'DELIVERY'),
            ('FINISHED', 'FINISHED'),
        ],
        default='ACCEPTED',
    )

    @property
    def delivery_time(self):
        """Calculates delivery time for :term:`Order`."""
        working_hours = order_during_working_hours(datetime.now().hour)
        number_of_pizzas = len(self.pizzas)
        return calculate_delivery_time(number_of_pizzas, working_hours)

    def __str__(self):
        """Returns string representation of :term:`Order`."""
        return 'Ordered {0}. Status: {1}'.format(self.order_date, self.status)
