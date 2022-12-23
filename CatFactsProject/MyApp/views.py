from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method =='POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Este nombre de usuario ya existe')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username)
            user.save()
    else:
        return render(request, 'signup.html')