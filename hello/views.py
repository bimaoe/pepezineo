from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os
from .models import Card
from .models import MyCard
from .models import User
import json

def index(request):
  """Main page. """
  return render(request, 'index.html')

def test(request):
  print request.POST
  return HttpResponse('<pre>' + 'hello' + '</pre>')

def acquire_cards(request):
  """Card acquisition (purchase or receiving).

  Functionalities:
    Increase the quantity of cards.
  """
  # TODO(bimaoe, catita): Remove this gambiarra when sessions are implemented.
  handle = 'pepezineo'
  user = User.objects.filter(handle=handle)
  request_data = json.loads(request.body)
  request_type = request_data['type']
  card_dict = request_data['cards']


  cards = Card.objects.filter(name__in=card_dict.keys())
  my_cards = MyCard.objects.filter(user=user, card__in=cards)
  cards_to_save = []
  for my_card in my_cards:
    my_card.quantity += int(card_dict[my_card.card.name])
    my_card.save()
  return HttpResponse(status=200)

def create_cards(request):
  """Card creation page.

  Functionalities:
    Insert a new card into database.
  """
  return render(request, 'create-cards.html')

def dashboard(request):
  """User dashboard page. 

  Functionalities:
    Show user's card collection.
    Upgrade the level of a card.
  """
  # TODO(bimaoe, catita): Remove this gambiarra when sessions are implemented.
  handle = 'pepezineo'
  user = User.objects.filter(handle=handle)
  my_card_list = MyCard.objects.filter(user=user)
  return render(request, 'dashboard.html', {'my_card_list': my_card_list})

def db(request):
  cards = Card.objects.all()
  return render(request, 'db.html', {'cards': cards})

def donate_cards(request):
  """Card donation.

  Functionalities:
    Decrease the quantity of cards.
  """
  # TODO(bimaoe, catita): Remove this gambiarra when sessions are implemented.
  handle = 'pepezineo'
  user = User.objects.filter(handle=handle)
  cards = Card.objects.filter(name__in=request.POST.keys())
  my_cards = MyCard.objects.filter(user=user, card__in=cards)
  cards_to_save = []
  for my_card in my_cards:
    my_card.quantity -= int(request.POST[my_card.card.name])
    if my_card.quantity < 0:
      raise ValueError('You do not have enough cards.')
    cards_to_save.append(my_card)
  # Save everything afterwards because if there is an error, we do not want any
  # changes to be made.
  for my_card in cards_to_save:
    my_card.save()
  return HttpResponse(status=200)

def insert_cards_into_db(request):
  """Card insertion into database. 

  Functionalities:
    Insert a new card into database.

  Redirects to: main page.
  """
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
  """ User card insertion or update. 

  Functionalities:
    Add new card to user's card collection.
    Update level or quantity of a card of the card collection.

  Redirects to: main page.
  """
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
  """Update card page. 

  Functionalities:
    Add card to user's card collection.
    Update card's attributes if it was already in the collection.
  """
  existing_cards = Card.objects.all()
  existing_cards = sorted(existing_cards, key=lambda x: x.name)
  return render(request, 'update-card.html', {'existing_cards': existing_cards})

def upgrade_card(request):
  """Upgrade card. 

  Functionalities:
    Increase the level of the card by one.
  
  Raises:
    Error: There are not enough cards to upgrade.
    Error: The card has reached the maximum level.
  """
  # TODO(bimaoe, catita): Remove this gambiarra when sessions are implemented.
  user = User(handle='pepezineo')
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
