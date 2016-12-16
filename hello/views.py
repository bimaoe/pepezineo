from django.shortcuts import render
from django.http import HttpResponse

from .models import Card

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    card = Card(name='Knight', type=Card.COMMON)
    card.save()

    cards = Card.objects.all()

    return render(request, 'db.html', {'cards': cards})

