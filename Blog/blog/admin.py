from django.contrib import admin
from .models import Articulo


# ==========================================================
# Configuración del panel de administración
# ==========================================================
#
# Permite visualizar, buscar y filtrar artículos.
#
# ==========================================================

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):

    # Columnas visibles
    list_display = (
        "titulo",
        "autor",
        "publicado",
        "fecha_creacion",
        "fecha_actualizacion",
    )

    # Filtros
    list_filter = (
        "publicado",
        "autor",
        "fecha_creacion",
    )

    # Buscador
    search_fields = (
        "titulo",
        "contenido",
    )

    # Orden descendente
    ordering = (
        "-fecha_creacion",
    )