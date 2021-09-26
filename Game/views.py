from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Guess
# Create your views here.


def game(request):
    a = Guess()
    a.savegraph()
    path=a.distance
    tracepath=a.tracepath()
    return render(request, 'game.html', {'title': "Game", 'path':path,'tracepath':tracepath})
