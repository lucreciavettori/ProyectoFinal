from django.shortcuts import render, redirect
import django

#para el log in, log out y register
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.models import User


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
                
                return redirect('AppViajes:Inicio')
           
            else:
                return redirect('AppViajes:Login')

        else:
            return redirect('AppViajes:Login')
        
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

            return redirect('AppViajes:Login')
    
    else:
        form=UserRegisterForm(request.POST)

    return render(request, 'AppAccounts/register.html', {'form': form})