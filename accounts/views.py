from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
from .forms import ExtendedUserCreationForm, UserProfileForm


def login(request):
    
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
        
    else:
        context = { 'title':'Login' }
        return render(request, 'accounts/login.html', context)


def userprofile(request):
    context = { 'title':'User Profile' }
    return render(request, 'accounts/userprofile.html', context)

def userslist(request):
    context = { 'title':'Users List' }
    return render(request, 'accounts/userslist.html', context)

def registation(request):

    if request.method == 'POST':
        print("We got the view")
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST) 

        if form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            # username = 'LSG'+ form.cleaned_data.get('username') +'OperatorID'
            # # email = form.cleaned_data.get('email')
            # password= form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)

            return redirect('home')
        else:
            print('Error: Form invalid.')


        

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form, 'title':'Register'}
    return render(request, 'accounts/register.html', context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        # username = request.POST['username']
        username = 'LSG'+ request.POST["last_name"] +'OperatorID'
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                print('Username already taken.')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                print('Email already taken.')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,last_name=last_name,)

                user.save()

                print('Data submitted successfully')
                # messages.info('success', 'You have succesfully registered.')
                return redirect('login')

        else:
            messages.info(request, 'Password does not match.')
            return redirect('register')

    else:
        context = {'title':'Register'}
        return render(request, 'accounts/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login')