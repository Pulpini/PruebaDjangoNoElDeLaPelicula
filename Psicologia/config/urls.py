"""
Archivo principal de rutas del proyecto.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # Panel administrador
    path(
        "admin/",
        admin.site.urls
    ),

    # Rutas del blog
    path(
        "",
        include("blog.urls")
    ),

    # Login HTML
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html"
        ),
        name="login"
    ),

    # Logout HTML
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    # ==========================
    # JWT
    # ==========================

    # Obtener Access Token y Refresh Token
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    # Renovar Access Token
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]