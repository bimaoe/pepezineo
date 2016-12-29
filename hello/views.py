from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os
from .models import Card
from .models import MyCard
from .models import User

def index(request):
  return render(request, 'index.html')

def test(request):
  print request.POST
  return HttpResponse('<pre>' + 'hello' + '</pre>')

def create_cards(request):
  return render(request, 'create-cards.html')

def dashboard(request):
  handle = 'pepezineo'
  user = User.objects.filter(handle=handle)
  my_card_list = MyCard.objects.filter(user=user)
  return render(request, 'dashboard.html', {'my_card_list': my_card_list})

def db(request):
  cards = Card.objects.all()
  return render(request, 'db.html', {'cards': cards})

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

def insert_or_update_my_card_into_db(request):
  # TODO(bimaoe, catita): Remove this gambiarra when creation of users is 
  #     implemented.
  pepezineo = User(handle='pepezineo')
  pepezineo.save()

  # TODO(bimaoe, catita): Remove this gambiarra when sessions are implemented.
  user = 'pepezineo'
  card = Card.objects.filter(name=request.POST['name'])[0]
  my_card = MyCard.objects.filter(user=pepezineo, card=card)
  if my_card:
    my_card.update(level=request.POST['level'], quantity=request.POST['quantity'])
  else:
    my_card = MyCard(user=pepezineo,
      card=card, 
      level=request.POST['level'], 
      quantity=request.POST['quantity'])
    my_card.save()
  return HttpResponseRedirect('/')

def update_card(request):
  existing_cards = Card.objects.all()
  existing_cards = sorted(existing_cards, key=lambda x: x.name)
  return render(request, 'update-card.html', {'existing_cards': existing_cards})



