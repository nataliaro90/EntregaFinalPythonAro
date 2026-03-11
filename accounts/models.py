from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Modelo para la mensajería entre usuarios
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enviados")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recibidos")
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.emisor} para {self.receptor}"