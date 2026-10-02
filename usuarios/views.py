from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import LoginForm, PerfilForm, RegistroForm, UsuarioForm
from .models import Perfil


def registro(request):
    if request.user.is_authenticated:
        return redirect('blog:lista')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            messages.success(request, f'¡Hola, {usuario.username}! Tu cuenta ya está creada.')
            return redirect('blog:lista')
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})


class IniciarSesionView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_redirect_url(self):
        # Si "next" apunta al propio login, con la sesión ya iniciada Django lo toma como un bucle y da error 500
        url = super().get_redirect_url()
        return '' if url == self.request.path else url

    def form_valid(self, form):
        messages.success(self.request, f'Hola de nuevo, {form.get_user().username}.')
        return super().form_valid(form)


class CerrarSesionView(LogoutView):
    # Desde Django 5 el logout solo acepta POST, por eso en la barra de navegación es un formulario
    def post(self, request, *args, **kwargs):
        tenia_sesion = request.user.is_authenticated
        respuesta = super().post(request, *args, **kwargs)
        if tenia_sesion:
            messages.info(request, 'Sesión cerrada. ¡Hasta la próxima!')
        return respuesta


@login_required
def perfil(request):
    # get_or_create por si el usuario no pasó por el registro (por ejemplo, un superusuario creado con createsuperuser)
    perfil_usuario, _ = Perfil.objects.get_or_create(usuario=request.user)
    contexto = {
        'perfil': perfil_usuario,
        'posts': request.user.posts.all(),
    }
    return render(request, 'usuarios/perfil.html', contexto)


@login_required
def editar_perfil(request):
    perfil_usuario, _ = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST, instance=request.user)
        form_perfil = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('usuarios:perfil')
    else:
        form_usuario = UsuarioForm(instance=request.user)
        form_perfil = PerfilForm(instance=perfil_usuario)

    contexto = {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil,
    }
    return render(request, 'usuarios/editar_perfil.html', contexto)
