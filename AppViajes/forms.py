from django import forms
from AppViajes.models import Mensaje

from AppViajes.models import Post


class MensajeFormulario(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['mensaje']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'slug', 'contenido', 'autor']
