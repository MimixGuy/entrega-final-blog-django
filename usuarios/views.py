from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistroForm


def registro(request):
    if request.user.is_authenticated:
        return redirect('blog:lista')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
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

    def form_valid(self, form):
        messages.success(self.request, f'Hola de nuevo, {form.get_user().username}.')
        return super().form_valid(form)


class CerrarSesionView(LogoutView):
    # Desde Django 5 el logout solo acepta POST, por eso en la barra de navegación es un formulario
    def post(self, request, *args, **kwargs):
        respuesta = super().post(request, *args, **kwargs)
        messages.info(request, 'Sesión cerrada. ¡Hasta la próxima!')
        return respuesta
