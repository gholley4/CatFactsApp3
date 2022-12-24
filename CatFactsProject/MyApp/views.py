from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile

# Create your views here.

#@login_required(login_url='signin')
def index(request):
    response = requests.get('https://catfact.ninja/fact')
    facts = response.json()
    return render(request, 'index.html', {'facts': facts})

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Este nombre de usuario ya existe')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username)
            user.save()
            return redirect('signin')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']

        user = auth.authenticate(username=username)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User does not exist')
            return redirect('signin')
    else:    
        return render(request, 'signin.html')


#@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

