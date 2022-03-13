from django import forms
from AppViajes.models import Mensaje

# formulario para la enviar mensaje a post

class MensajeFormulario(forms.ModelForm):
	class Meta: 
		model = Mensaje
		fields = ['mensaje']       

