from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Fact, Likes
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import messages
from django.http import HttpResponse
import random
import json
from functools import reduce as functools_reduce

# Create your views here.

# Esto ayuda a facilitar cambios de código
CAT_FACTS_LIMIT = 10  
CAT_FACTS_MAX_LENGTH = 140
CAT_FACTS_API_ENDPOINT = lambda mlength, limit: \
    f'https://catfact.ninja/facts?max_length={mlength}&limit={limit}'

#@login_required(login_url='signin')
def index(request):
    '''
    Aqui Es bueno explicar un poco lo que esperamos hacer aqui, hay una buena 
    convención, que es el formato de documentación de métodos de google 
    disponible acá:
    https://google.github.io/styleguide/pyguide.html#383-functions-and-methods
    Esto es válido para todo lenguaje de programación, sobretodo si nuestra
    función hace cosas muy puntuales y peculiares. Recuerda siempre que nuestros
    programas son escritos para otros programadores, que uno individualmente lo
    entienda no garantiza que es una buena documentación/explicación
    '''
    # Te Dejo aqui mi propuesta de implementación 
    def create_fact(cat_fact: str):
        fact_created = Fact.objects.create(facts=cat_fact)
        fact_created.save()

    
    
    if request.method != 'GET':
        return redirect('/')
    
    cat_facts_response = requests.get(
      CAT_FACTS_API_ENDPOINT(
        CAT_FACTS_MAX_LENGTH,
        CAT_FACTS_LIMIT
      )
    )
    if cat_facts_response.status_code != 200:
        return redirect('/')
    
    for fact in map(lambda f: f['fact'], cat_facts_response.json()['data']):
        create_fact(fact)

    return render(
      request, 
      'index.html', 
      {
        'facts': Fact.objects.all()[:5]
      }
    )

    # Aqui acaba mi propuesta de implementación

    lista = []
    for i in range (10):
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
    facts = Fact.objects.all()[:5]
    facts2 = Fact.objects.all()[5:10]
    #likedFacts = Likes.objects.filter(username__isnull=False)
    return render(request, 'index.html', {'facts':facts, 'facts2':facts2})

#@login_required(login_url='signin')
def like_post(request):
    '''
    Mismo tema del docstring del método index
    '''
    username = request.user.username
    id_facts = request.GET.get('id_facts')

    fact = Fact.objects.get(id_facts=id_facts)

    # Para que quede más legible
    like_filter = Likes.objects.filter(
      id_facts=id_facts, 
      username=username
    ).first()
    
    # Mi propuesta

    if like_filter == None:
        new_like = Likes.objects.create(id_facts=id_facts, username=username)
        new_like.save()
        fact.no_of_likes += 1
    else:
        like_filter.delete()
        fact.no_of_likes -= 1
    fact.save()
    return redirect('index')

    # Fin de mi propuesta

    if like_filter == None:
        new_like = Likes.objects.create(id_facts=id_facts, username=username)
        new_like.save()
        fact.no_of_likes += 1  # Más sucinto
        fact.save()
        return redirect('index')  # Comportamiento duplicado
    else:
        like_filter.delete()
        fact.no_of_likes -= 1  # Más sucinto
        fact.save()  # Se había escapado el paréntesis
        return redirect('index')

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

