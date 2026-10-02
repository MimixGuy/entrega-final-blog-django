from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
