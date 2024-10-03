from django.shortcuts import render
from .models import Computadora

# Create your views here.

def login (request):
    return render(request, 'index.html')

def tienda (request):
    computadores = Computadora.objects.all()
    return render(request, 'tienda.html', {'computadores': computadores})