from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil


class EstiloBootstrapMixin:
    """Le pone la clase form-control de Bootstrap a todos los campos del formulario."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'


class RegistroForm(EstiloBootstrapMixin, UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email']


class LoginForm(EstiloBootstrapMixin, AuthenticationForm):
    pass


class UsuarioForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PerfilForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }
