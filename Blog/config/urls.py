"""
Archivo principal de rutas del proyecto.

Este archivo recibe todas las peticiones del navegador
y las deriva hacia la aplicación correspondiente.

En este caso solamente existe la aplicación Blog.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [

    # ==========================================================
    # Panel de administración de Django
    # ==========================================================
    path(
        'admin/',
        admin.site.urls
    ),

    # ==========================================================
    # Login
    # Utiliza la vista incorporada de Django.
    # ==========================================================
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='blog/login.html'
        ),
        name='login'
    ),

    # ==========================================================
    # Logout
    # Después del cierre de sesión vuelve al listado.
    # ==========================================================
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(
            next_page='lista_articulos'
        ),
        name='logout'
    ),

    # ==========================================================
    # Todas las rutas del Blog
    # ==========================================================
    path(
        '',
        include('blog.urls')
    ),

]