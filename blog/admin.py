from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'creado')
    list_filter = ('autor', 'creado')
    search_fields = ('titulo', 'contenido')
