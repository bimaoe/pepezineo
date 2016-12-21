from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os
from .models import Card

def test(request):
  print request.POST
  return HttpResponse('<pre>' + 'hello' + '</pre>')

def insert_cards_into_db(request):
  i = 0
  while 'name' + str(i) in request.POST:
    cname = 'name' + str(i)
    ctype = 'type' + str(i)
    celixir = 'elixir' + str(i)
    carena = 'arena' + str(i)
    card = Card(name=request.POST[cname], 
        type=Card.get_type(request.POST[ctype]), 
        elixir=request.POST[celixir],
        arena=request.POST[carena])
    card.save()
    i += 1
  return HttpResponseRedirect('/')


# Create your views here.
def index(request):
  return render(request, 'index.html')

def create_cards(request):
  return render(request, 'create-cards.html')

def db(request):
  cards = Card.objects.all()

  return render(request, 'db.html', {'cards': cards})

