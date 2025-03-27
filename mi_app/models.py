from django.db import models
from django.contrib.auth.models import User

class Actividad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.titulo

from django.db import models
from django.contrib.auth.models import User

class NotaCalendario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    contenido = models.TextField()

    def __str__(self):
        return f'Nota de {self.usuario} para {self.fecha}'

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    def get_embed_url(self):
        if "youtube.com" in self.url or "youtu.be" in self.url:
            video_id = self.url.split("v=")[-1].split("&")[0] if "v=" in self.url else self.url.split("/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.url  # En caso de que no sea un video de YouTube

    def __str__(self):
        return self.title

