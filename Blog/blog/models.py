from django.db import models
from django.contrib.auth.models import User


class Consulta(models.Model):

    psicologo = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    nombre_paciente = models.CharField(max_length=100)
    edad = models.IntegerField()

    motivo_consulta = models.TextField()
    observaciones = models.TextField(blank=True, null=True)

    ESTADOS = [
        ('Ansiedad', 'Ansiedad'),
        ('Estrés', 'Estrés'),
        ('Autoestima', 'Autoestima'),
        ('Depresión', 'Depresión'),
    ]

    estado_emocional = models.CharField(max_length=30, choices=ESTADOS)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_paciente} - {self.estado_emocional}"