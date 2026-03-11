from django.urls import path
from .views import (
    login_view, 
    register_view, 
    logout_view, 
    lista_mensajes, 
    enviar_mensaje, 
    editar_perfil
)

urlpatterns = [
    # Autenticación
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
    # Perfil
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    
    # Mensajería
    path('mensajes/', lista_mensajes, name='lista_mensajes'),
    path('mensajes/enviar/', enviar_mensaje, name='enviar_mensaje'),
]