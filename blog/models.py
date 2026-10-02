from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    titulo = models.CharField('título', max_length=200)
    subtitulo = models.CharField('subtítulo', max_length=200, blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/', blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo
