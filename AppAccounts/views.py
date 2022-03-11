from django.shortcuts import render, redirect
import django

#para el log in, log out y register
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages


def login_request (request):

    if request.method=='POST':
        #validar el usuario
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.data.get ('username')
            passwd = form.data.get ('password')

            user = authenticate(username=usuario, password=passwd)

            if user:
                login(request,user)
                
                return redirect('http://127.0.0.1:8000/AppViajes/inicio')
           
            else:
                return redirect('http://127.0.0.1:8000/AppViajes/account/login')

        else:
            return redirect('http://127.0.0.1:8000/AppViajes/account/login')
        
    form = AuthenticationForm()

    return render(request,'AppAccounts/login.html', {'form': form})

def register(request):
    if request.method=='POST':

        form=UserRegisterForm(request.POST)

        if form.is_valid():

            username=form.data['username']
            try:
                user_new=User.objects.get(username=username)
            except django.contrib.auth.models.User.DoesNotExist:
                user_new=None

            if not user_new:
                
                form.save()

            return redirect('http://127.0.0.1:8000/AppViajes/account/login')
    
    else:
        form=UserRegisterForm(request.POST)

    return render(request, 'AppAccounts/register.html', {'form': form})

def profile (request):

    if request.method == 'POST':
        
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
	    
        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Tu perfil fue actualizado!')
        else:
            messages.error(request,'No se pudo completar el requerimiento')
        return redirect ('http://127.0.0.1:8000/AppViajes/account/perfiles/')
    
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'AppAccounts/profile.html', {"user":request.user, "user_form":user_form, "profile_form":profile_form})