# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers

from .views import (
    IngredientViewSet,
    OrderViewSet,
    PizzaViewSet,
    get_statistics,
)

router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet)
router.register('ingredient', IngredientViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/pizza', get_statistics)
]
