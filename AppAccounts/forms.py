from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from ckeditor.fields import RichTextField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ('username','email')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        model = Profile
        fields = ('web','descripcion')

class UserProfileForm(UserCreationForm):
    first_name=forms.CharField(max_length=120)
    last_name=forms.CharField(max_length=120)
    email=forms.EmailField()
    web=forms.URLField(max_length=200)
    descripcion=forms.CharField(max_length=350)
#    foto=forms.ImageField()


