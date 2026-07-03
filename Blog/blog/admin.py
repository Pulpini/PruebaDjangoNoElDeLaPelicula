from django.contrib import admin
from .models import Articulo

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'publicado', 'fecha_creacion']
    list_filter = ['publicado', 'autor']
    search_fields = ['titulo', 'contenido']

