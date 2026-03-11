from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Perfil, Mensaje

# --- Autenticación ---

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')

# --- Perfil y Mensajería ---

@login_required
def editar_perfil(request):
    usuario = request.user
    perfil, created = Perfil.objects.get_or_create(user=usuario)
    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.email = request.POST.get('email')
        usuario.save()
        if request.FILES.get('avatar'):
            perfil.avatar = request.FILES.get('avatar')
        perfil.bio = request.POST.get('bio')
        perfil.save()
        return redirect('inicio')
    return render(request, 'accounts/editar_perfil.html', {'perfil': perfil})

@login_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    return render(request, 'accounts/mensajes.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    usuarios = User.objects.exclude(username=request.user.username)
    if request.method == "POST":
        receptor_id = request.POST.get('receptor')
        contenido = request.POST.get('contenido')
        receptor = User.objects.get(id=receptor_id)
        Mensaje.objects.create(emisor=request.user, receptor=receptor, contenido=contenido)
        return redirect('lista_mensajes')
    return render(request, 'accounts/enviar_mensaje.html', {'usuarios': usuarios})