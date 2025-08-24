# usuarios/models.py

from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    # A relação OneToOneField garante que cada PerfilUsuario seja associado a um único User
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'