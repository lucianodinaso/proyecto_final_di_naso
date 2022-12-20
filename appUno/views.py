from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    return render(request, "appUno/index.html")

def jugadores(request):
    return render(request, "appUno/jugadores.html")

def partidos(request):
    return render(request, "appUno/partidos.html")

def goles(request):
    return render(request, "appUno/goles.html")

def tecnicos(request):
    return render(request, "appUno/tecnicos.html")
