import datetime
from django import forms

# Creamos el formulario para la calse "Mensaje"
class MensajeFormulario(forms.Form):

    #autor_mensaje=forms.CharField(max_length=30)
    mensaje=forms.CharField(widget=forms.Textarea(attrs= {
        "class": "formulario_ms",
        "placeholder":"Escribe tu mensaje"
    }))

