from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Please, login to gain access')
        return redirect('accounts/login')
    else:
        return render(request, 'home.html', { 'title':'Dashboard' })