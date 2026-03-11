from django.contrib import admin
from .models import Perfil, Mensaje

# Registro básico del Perfil
admin.site.register(Perfil)

# Registro personalizado de Mensajes para que se vea como una tabla linda
@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    # Esto define qué columnas ves apenas entrás
    list_display = ('emisor', 'receptor', 'fecha', 'contenido')
    # Esto agrega filtros a la derecha para buscar por fecha
    list_filter = ('fecha',)
    # Esto pone un buscador por nombre de usuario o contenido
    search_fields = ('emisor__username', 'receptor__username', 'contenido')