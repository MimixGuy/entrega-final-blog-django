from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to='avatares/', blank=True)
    biografia = models.TextField('biografía', max_length=500, blank=True)

    class Meta:
        verbose_name_plural = 'perfiles'

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
