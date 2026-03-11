from django.urls import path
from .views import (
    inicio, about, detalle_post, 
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path('pages/<int:post_id>/', detalle_post, name='detalle_post'),
    
    # Rutas para CRUD de Posts (CBV)
    path('pages/create/', PostCreateView.as_view(), name='post_create'),
    path('pages/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('pages/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]