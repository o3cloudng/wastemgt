from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# from django.contrib.auth import authenticate, login
from django.contrib import messages

# from .forms import ClientForm
# Create your views here.
# from .forms import ExtendedUserCreationForm, UserProfileForm

def client(request):
    print('View Client')
    # form = ClientForm()
    return render(request, 'client/client_register.html')

def home(request):
    context = {'title':'Home'}
    return render(request, 'client/index.html', context)

def register(request):
    context = {'title':'Register'}
    # form = ClientForm()
    return render(request, 'client/client_register.html', context)

def login(request):
    context = {'title':'Login'}
    # form = ClientForm()
    return render(request, 'client/client_login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/login')
