# -*- coding: utf-8 -*-

from __future__ import unicode_literals  # noqa: WPS422

from django.contrib import admin

from yumpi.models import Ingredient, Order, Pizza

admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Order)
