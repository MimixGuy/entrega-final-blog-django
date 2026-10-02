from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


class SoloAutorMixin(UserPassesTestMixin):
    """Solo deja pasar al autor del post. A cualquier otro usuario le devuelve un 403."""

    def test_func(self):
        return self.get_object().autor == self.request.user


class ListaPostsView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    paginate_by = 6


class DetallePostView(DetailView):
    model = Post
    template_name = 'blog/detalle_post.html'


def buscar(request):
    busqueda = request.GET.get('q', '').strip()
    resultados = Post.objects.none()
    if busqueda:
        resultados = Post.objects.filter(
            Q(titulo__icontains=busqueda) | Q(contenido__icontains=busqueda)
        )
    contexto = {
        'busqueda': busqueda,
        'resultados': resultados,
    }
    return render(request, 'blog/resultados_busqueda.html', contexto)


class CrearPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/formulario_post.html'
    success_message = 'El post «%(titulo)s» se publicó correctamente.'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EditarPostView(LoginRequiredMixin, SoloAutorMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/formulario_post.html'
    success_message = 'Cambios guardados.'


class EliminarPostView(LoginRequiredMixin, SoloAutorMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/confirmar_eliminar.html'
    success_url = reverse_lazy('blog:lista')
    success_message = 'El post se eliminó.'
