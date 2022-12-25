from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Fact
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from django.http import HttpResponse
import json

# Create your views here.

#@login_required(login_url='signin')
def index(request):
    response = requests.get('https://catfact.ninja/fact?max_length=140')
    data = response.json()
    dataToDict = json.dumps(data)

    Fact = json.dumps(dataToDict[10:])

    return render(request, 'index.html', {'facts': Fact})

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("signin")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'signup.html' , context={"register_form":form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']

        user = auth.authenticate(username=username)

        auth.login(request, user)
        return redirect('index')
        
    else:    
        return render(request, 'signin.html')


#@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

