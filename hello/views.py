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
  # TODO(bimaoe, catita): Remove this gambiarra when sessions are implemented.
  user = User(handle='pepezineo')
  card = Card.objects.filter(name=request.POST['name'])[0]
  my_card = MyCard.objects.filter(user=user, card=card)
  if my_card:
    my_card.update(level=request.POST['level'], 
        quantity=request.POST['quantity'])
  else:
    my_card = MyCard(user=user,
      card=card, 
      level=request.POST['level'], 
      quantity=request.POST['quantity'])
    my_card.save()
  return HttpResponseRedirect('/')

def update_card(request):
  existing_cards = Card.objects.all()
  existing_cards = sorted(existing_cards, key=lambda x: x.name)
  return render(request, 'update-card.html', {'existing_cards': existing_cards})

def upgrade_card(request):
  # TODO(bimaoe, catita): Remove this gambiarra when sessions are implemented.
  user = User(handle='pepezineo')
  print request.POST['card']
  card = Card.objects.filter(name=request.POST['card'])[0]

  my_card = MyCard.objects.filter(user=user, card=card)[0]
  if my_card.quantity < Card.CARDS_REQUIRED_TO_UPGRADE[my_card.level-1]:
    # There are not enough cards.
    # TODO(bimaoe, catita): Show error message when there are not enough cards.
    raise
  elif my_card.level == Card.MAX_LEVEL[my_card.card.type-1]:
    # It has reached the maximum level.
    # TODO(bimaoe, catita): Show error message when the card cannot be upgraded.
    raise
  else:
    my_card.quantity -= Card.CARDS_REQUIRED_TO_UPGRADE[my_card.level-1]
    my_card.level += 1
    my_card.save()
  return HttpResponseRedirect('/dashboard')
