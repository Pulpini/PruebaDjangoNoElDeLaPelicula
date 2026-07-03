"""
==============================================================
Archivo principal de URLs del proyecto Django.

Este archivo recibe todas las peticiones realizadas
por el navegador.

Luego deriva esas peticiones hacia la aplicación Blog.
==============================================================
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [

    # ==========================================================
    # PANEL ADMINISTRADOR
    # ==========================================================
    #
    # Acceso:
    #
    # http://127.0.0.1:8000/admin/
    #
    path(
        "admin/",
        admin.site.urls
    ),

    # ==========================================================
    # LOGIN
    # ==========================================================
    #
    # Utiliza la vista incorporada de Django.
    #
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html"
        ),
        name="login"
    ),

    # ==========================================================
    # LOGOUT
    # ==========================================================
    #
    # Cierra la sesión del usuario y vuelve
    # al listado principal.
    #
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(
            next_page="lista_articulos"
        ),
        name="logout"
    ),

    # ==========================================================
    # BLOG
    # ==========================================================
    #
    # Todas las URLs del Blog serán cargadas
    # desde blog/urls.py
    #
    path(
        "",
        include("blog.urls")
    ),

]