from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_signup_view(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST['username'].strip() 
            email = request.POST['email'].strip()
            password = request.POST['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save() 

                authenticated_user = authenticate(request, username=username, password=password)
                if authenticated_user:
                    login(request, authenticated_user)  
                    return redirect('home')
                else:
                    messages.error(request, 'Failed to log you in. Please log in manually.')

        elif 'login' in request.POST:
            username = request.POST['username'].strip()  
            password = request.POST['password']

            if not username or not password:
                messages.error(request, 'Username and password are required.')
                return render(request, 'users/login_signup.html')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'users/login_signup.html')


def user_logout(request):
    logout(request)
    return redirect('login')
