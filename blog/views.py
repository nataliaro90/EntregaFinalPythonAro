from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from accounts.models import Perfil

# --- Vistas de Funciones ---
def inicio(request):
    posts = Post.objects.all().order_by('-fecha')
    perfil = Perfil.objects.first() 
    return render(request, 'blog/inicio.html', {'posts': posts, 'perfil': perfil})

def about(request):
    perfil = Perfil.objects.first() 
    return render(request, 'blog/about.html', {'perfil': perfil})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    perfil = Perfil.objects.first()
    return render(request, 'blog/detalle.html', {'post': post, 'perfil': perfil})

# --- Vistas de Clases (CBV) ---
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen'] # 'autor' NO va aquí
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.autor = self.request.user # Asigna el usuario logueado automáticamente
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('inicio')

    def test_func(self): # Seguridad: Solo el autor edita
        post = self.get_object()
        return self.request.user == post.autor

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('inicio')

    def test_func(self): # Seguridad: Solo el autor borra
        post = self.get_object()
        return self.request.user == post.autor