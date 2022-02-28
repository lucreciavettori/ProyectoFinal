from django import froms

# Creamos el formulario para la calse "Usuario"
class UsuarioFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    nickname=forms.CharField(max_length=30)
    email=forms.EmailField()
    ciudad=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    alta=forms.DateField()

# Creamos el formulario para la calse "Blog"
class UsuarioFormulario(forms.Form):

    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=30)
    imagen=forms.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

# Creamos el formulario para la calse "Mensaje"
class UsuarioFormulario(forms.Form):

    titulo=forms.CharField(max_length=30)
    contenido=forms.TextField(max_length=100)
    fecha=forms.DateField()
    deNombre=forms.CharField(max_length=30)
    deEmail=forms.EmailField()
    paraNombre=forms.CharField(max_length=30)
    paraEmail=forms.EmailField()