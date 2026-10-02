from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ListaPostsView.as_view(), name='lista'),
    path('posts/nuevo/', views.CrearPostView.as_view(), name='crear'),
    path('posts/<int:pk>/', views.DetallePostView.as_view(), name='detalle'),
    path('posts/<int:pk>/editar/', views.EditarPostView.as_view(), name='editar'),
    path('posts/<int:pk>/eliminar/', views.EliminarPostView.as_view(), name='eliminar'),
]
