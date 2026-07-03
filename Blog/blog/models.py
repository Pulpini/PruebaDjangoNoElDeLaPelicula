from django.db import models
from django.contrib.auth.models import User  # type: ignore


# ==========================================================
# Modelo Articulo
# ----------------------------------------------------------
# Representa una publicación creada por un usuario.
#
# Cada artículo posee:
# - un título
# - un contenido
# - un autor
# - un estado (publicado o borrador)
# - fecha de creación
# - fecha de modificación
# ==========================================================

class Articulo(models.Model):

    # Título del artículo
    titulo = models.CharField(max_length=200)

    # Contenido principal
    contenido = models.TextField()

    # Usuario propietario del artículo
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articulos"
    )

    # Indica si el artículo es público
    publicado = models.BooleanField(default=False)

    # Fecha de creación automática
    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    # Fecha de actualización automática
    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    # Texto que aparecerá en el panel administrador
    def __str__(self):
        return self.titulo

    # Configuración adicional del modelo
    class Meta:

        # Ordenar desde el más reciente
        ordering = ["-fecha_creacion"]

        # Nombre singular
        verbose_name = "Artículo"

        # Nombre plural
        verbose_name_plural = "Artículos"