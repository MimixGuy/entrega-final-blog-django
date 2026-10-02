from django.views.generic import DetailView, ListView

from .models import Post


class ListaPostsView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    paginate_by = 6


class DetallePostView(DetailView):
    model = Post
    template_name = 'blog/detalle_post.html'
