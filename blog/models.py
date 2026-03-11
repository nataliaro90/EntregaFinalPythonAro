from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=200)       # 1er CharField
    subtitulo = models.CharField(max_length=200)    # 2do CharField
    cuerpo = RichTextField()                        # Texto enriquecido (Ckeditor)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True) # Campo de fecha
    imagen = models.ImageField(upload_to='blog_images', null=True, blank=True) # Campo de imagen

    def __str__(self):
        return f"{self.titulo} - {self.autor}"