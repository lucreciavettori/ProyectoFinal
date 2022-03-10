from django import forms
from ckeditor.fields import RichTextField


# Creamos el formulario para la calse "Mensaje"
class MensajeFormulario(forms.Form):

    mensaje=forms.CharField(widget=forms.Textarea(attrs= {
        "class": "formulario_ms",
        "placeholder":"Escribe tu mensaje"
    }))
