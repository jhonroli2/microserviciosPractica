from django.contrib import admin
from django.urls import path
from inventario.views.productos import productos_view

inventario_urls = [
    path('productos',productos_view),
]
