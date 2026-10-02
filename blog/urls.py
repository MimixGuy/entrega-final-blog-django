from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ListaPostsView.as_view(), name='lista'),
    path('posts/<int:pk>/', views.DetallePostView.as_view(), name='detalle'),
]
