from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from accounts.models import Perfil

# --- Vistas de Funciones (Para ver contenido) ---

def inicio(request):
    posts = Post.objects.all()
    perfil = Perfil.objects.first() 
    return render(request, 'blog/inicio.html', {'posts': posts, 'perfil': perfil})

def about(request):
    perfil = Perfil.objects.first() 
    return render(request, 'blog/about.html', {'perfil': perfil})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    perfil = Perfil.objects.first()
    return render(request, 'blog/detalle.html', {'post': post, 'perfil': perfil})

# --- Vistas de Clases (CBV) con Mixins (Requisito de la consigna) ---

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor']
    success_url = reverse_lazy('inicio')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('inicio')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('inicio')