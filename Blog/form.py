from django import forms
from .models import Consulta


class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta

        fields = [
            'nombre_paciente',
            'edad',
            'motivo_consulta',
            'observaciones',
            'estado_emocional'
        ]