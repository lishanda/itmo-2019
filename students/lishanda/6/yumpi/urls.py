# -*- coding: utf-8 -*-

"""Django URL Routing for yumpi application."""

from django.urls import include, path
from rest_framework import routers

from yumpi.views import (
    IngredientViewSet,
    OrderViewSet,
    PizzaViewSet,
    get_statistics,
    post_order,
)

router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet)
router.register('ingredient', IngredientViewSet)
router.register('admin_order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order/', post_order),
    path('statistics/pizza', get_statistics),
]
