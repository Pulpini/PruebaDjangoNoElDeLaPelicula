"""
==============================================================
Archivo principal de URLs del proyecto Django.

Este archivo recibe todas las peticiones realizadas
por el navegador.

Luego deriva esas peticiones hacia la aplicación Blog.
==============================================================

"""
from django.urls import path

from . import views

urlpatterns = [


# Página principal
path(
    "",
    views.lista_articulos,
    name="lista_articulos"
),

# Ver un artículo
path(
    "articulo/<int:pk>/",
    views.detalle_articulo,
    name="detalle_articulo"
),

# Crear un artículo
path(
    "crear/",
    views.crear_articulo,
    name="crear_articulo"
),

# Editar un artículo
path(
    "editar/<int:pk>/",
    views.editar_articulo,
    name="editar_articulo"
),

# Eliminar un artículo
path(
    "eliminar/<int:pk>/",
    views.eliminar_articulo,
    name="eliminar_articulo"
),

]
