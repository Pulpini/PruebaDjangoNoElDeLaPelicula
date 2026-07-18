"""
==============================================================
Rutas de la aplicación Blog.

Aquí se encuentran tanto las vistas HTML tradicionales
como las rutas de la API protegidas con JWT.
==============================================================
"""

from django.urls import path

from . import views

urlpatterns = [

    # ==========================================================
    # VISTAS HTML
    # ==========================================================

    # Página principal
    path(
        "",
        views.lista_articulos,
        name="lista_articulos"
    ),

    # Ver detalle de un artículo
    path(
        "articulo/<int:pk>/",
        views.detalle_articulo,
        name="detalle_articulo"
    ),

    # Crear artículo
    path(
        "crear/",
        views.crear_articulo,
        name="crear_articulo"
    ),

    # Editar artículo
    path(
        "editar/<int:pk>/",
        views.editar_articulo,
        name="editar_articulo"
    ),

    # Eliminar artículo
    path(
        "eliminar/<int:pk>/",
        views.eliminar_articulo,
        name="eliminar_articulo"
    ),

    # ==========================================================
    # API REST + JWT
    # ==========================================================

    # Ruta pública
    path(
        "api/publica/",
        views.api_publica,
        name="api_publica"
    ),

    # Registro de usuarios
    path(
        "api/registro/",
        views.registrar_usuario,
        name="registrar_usuario"
    ),

    # Obtener todos los artículos del usuario autenticado
    path(
        "api/articulos/",
        views.api_articulos,
        name="api_articulos"
    ),

    # Obtener un artículo
    path(
        "api/articulos/<int:pk>/",
        views.api_articulo,
        name="api_articulo"
    ),

    # Crear artículo
    path(
        "api/articulos/crear/",
        views.api_crear,
        name="api_crear"
    ),

    # Editar artículo
    path(
        "api/articulos/editar/<int:pk>/",
        views.api_editar,
        name="api_editar"
    ),

    # Eliminar artículo
    path(
        "api/articulos/eliminar/<int:pk>/",
        views.api_eliminar,
        name="api_eliminar"
    ),
]