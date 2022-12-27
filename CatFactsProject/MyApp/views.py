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
import random
import json

# Create your views here.

#@login_required(login_url='signin')
def index(request):
    lista = []
    for i in range (4):
        if request.method == 'GET':
            response = requests.get('https://catfact.ninja/fact?max_length=140') 
            data = response.json()
            dataToDict = json.dumps(data)
            fact = json.dumps(dataToDict[10:-17])
            new_fact = Fact.objects.create(facts=fact)
            new_fact.save()
            lista.append(new_fact)
        else:
            return redirect('/')
    
    #rand = random.choice(lista)
    #print(lista)
    #print(rand)
    #Fact.save()

    #facts = Fact.objects.all
        #print(lista)        
    #rand = random.choice(lista)

    return render(request, 'index.html', {'facts1': lista[0], 'facts2':lista[1],'facts3': lista[2], 'facts4':lista[3]})

#@login_required(login_url='signin')
def like_post(request):
    pass

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

