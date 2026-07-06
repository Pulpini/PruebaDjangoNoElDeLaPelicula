from django import forms

from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:

        model = Articulo

        fields = [
            "titulo",
            "contenido",
            "publicado",
        ]

        labels = {
            "titulo": "Título",
            "contenido": "Contenido",
            "publicado": "Publicado",
        }

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el título del artículo",
                }
            ),
            "contenido": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Escriba aquí el contenido del artículo...",
                }
            ),
            "publicado": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
