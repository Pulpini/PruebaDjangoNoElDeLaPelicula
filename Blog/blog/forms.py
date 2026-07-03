from django import forms
from .models import Articulo


# ==========================================================
# Formulario basado en el modelo Articulo
#
# ModelForm permite generar automáticamente un formulario
# utilizando los campos definidos en models.py
# ==========================================================

class ArticuloForm(forms.ModelForm):

    class Meta:

        # Modelo asociado
        model = Articulo

        # Campos que aparecerán en pantalla
        fields = [
            "titulo",
            "contenido",
            "publicado"
        ]

        # Personalización visual
        widgets = {

            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el título"
                }
            ),

            "contenido": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Escriba aquí el contenido..."
                }
            ),

            "publicado": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            )
        }

        # Etiquetas visibles
        labels = {

            "titulo": "Título",

            "contenido": "Contenido",

            "publicado": "Publicar artículo"
        }
