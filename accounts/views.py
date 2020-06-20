from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    pass


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        # username = request.POST['username']
        username = 'LSG'+ request.POST["last_name"] +'OperatorID'
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,last_name=last_name,)

        user.save()

        print('Data submitted successfully')
        # messages.info('success', 'You have succesfully registered.')
        return redirect('/')

    else:
        return render(request, 'accounts/register.html', { 'title':'Register' })


