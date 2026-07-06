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

# Panel de administración
path(
    "admin/",
    admin.site.urls
),

# CRUD del blog
path(
    "",
    include("blog.urls")
),

# Login
path(
    "login/",
    auth_views.LoginView.as_view(
        template_name="blog/login.html"
    ),
    name="login"
),

# Logout
path(
    "logout/",
    auth_views.LogoutView.as_view(),
    name="logout"
),


]
