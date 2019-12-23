# -*- coding: utf-8 -*-

"""Django URL Routing entry point for pizzapp project."""

from django.contrib import admin
from django.urls import include, path

from yumpi import urls as yumpi_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(yumpi_urls)),
]
