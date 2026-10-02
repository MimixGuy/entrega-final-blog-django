from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 12}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        help_texts = {
            'imagen': 'Opcional.',
        }
