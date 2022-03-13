from django.shortcuts import render, redirect
import django

#para el log in, log out y register
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserForm, UserProfileForm
from django.contrib.auth.models import User

#para el profile
from .models import Profile



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

    usuario=request.user

    if request.method == 'POST':
        
        user_form = UserProfileForm(request.POST, instance=request.user)
        	    
        if user_form.is_valid():
            informacion = user_form.data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']        
            usuario.last_name = informacion['last_name']      
            usuario.first_name = informacion['first_name'] 
            usuario.save()
            
            if Profile.objects.filter(user=usuario):
                profile = Profile.objects.get(user=usuario)
            #    profile.foto = informacion['foto']
                profile.descripcion = informacion['descripcion']
                profile.web = informacion['web']
            else:
                profile=Profile(
                    user=usuario,
            #        foto=informacion['foto'],
                    descripcion=informacion['descripcion'],
                    web=informacion['web']
                    )

            profile.save()

            return redirect ('AppViajes:profile_view')
    else:
        user_form = UserProfileForm(initial={'username':usuario.username, 'email':usuario.email,'first_name':usuario.first_name,'last_name':usuario.last_name})

    return render(request, 'AppAccounts/profile_form.html', {"user":request.user, "user_form":user_form})

def profile_view (request):

    usuario=request.user

    if request.method == 'POST':
        
        user_form = UserProfileForm(request.POST, instance=request.user)
        	    
        if user_form.is_valid():
            informacion = user_form.data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']        
            usuario.last_name = informacion['last_name']      
            usuario.first_name = informacion['first_name'] 
            
            profile = Profile.objects.get(user=usuario)
        #    profile.foto = informacion['foto']
            profile.descripcion = informacion['descripcion']
            profile.web = informacion['web']

    else:
        user_form = UserProfileForm(initial={'username':usuario.username, 'email':usuario.email,'first_name':usuario.first_name,'last_name':usuario.last_name})

    return render(request, 'AppAccounts/profile.html', {"user":request.user, "user_form":user_form})


