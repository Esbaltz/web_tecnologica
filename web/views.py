from django.shortcuts import render
from .models import Computadora

# Create your views here.

def login (request):
    return render(request, 'index.html')

def tienda(request):
    computadores = Computadora.objects.all()  

    # Filtrar por rango de precio
    precio_minimo = request.GET.get('precio_minimo')
    precio_maximo = request.GET.get('precio_maximo')
    
    if precio_minimo and precio_maximo:
        computadores = computadores.filter(precio__gte=precio_minimo, precio__lte=precio_maximo)

    # Filtrar por marcas
    marcas_seleccionadas = request.GET.getlist('marcas')
    if marcas_seleccionadas:
        computadores = computadores.filter(marca__in=marcas_seleccionadas)

    return render(request, 'tienda.html', {'computadores': computadores})