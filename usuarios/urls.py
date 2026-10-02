from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.IniciarSesionView.as_view(), name='login'),
    path('logout/', views.CerrarSesionView.as_view(), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
