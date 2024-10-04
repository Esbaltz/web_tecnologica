from django.shortcuts import render, redirect, get_object_or_404
from .models import Computadora
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('tienda')  
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales incorrectas.'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Formulario inválido.'})
    else:
        form = AuthenticationForm()  # Carga el formulario en caso de que sea una solicitud GET
    return render(request, 'login.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Asegúrate de usar la función de login con dos argumentos
            return redirect('tienda')  # Asume que 'tienda' es la URL a la que deseas redirigir después del registro
    else:
        form = RegisterForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def tienda(request):
    # Obtiene todos los computadores
    computadores = Computadora.objects.all()

    # Filtrar por término de búsqueda (nombre del computador)
    query = request.GET.get('search', '')  # Si no hay búsqueda, estará vacío
    if query:
        computadores = computadores.filter(nombre__icontains=query)

    # Filtrar por rango de precio
    precio_minimo = request.GET.get('precio_minimo')
    precio_maximo = request.GET.get('precio_maximo')

    if precio_minimo and precio_maximo:
        computadores = computadores.filter(precio__gte=precio_minimo, precio__lte=precio_maximo)

    # Filtrar por marcas seleccionadas
    marcas_seleccionadas = request.GET.getlist('marcas')
    if marcas_seleccionadas:
        computadores = computadores.filter(marca__in=marcas_seleccionadas)

    # Renderizar la vista con los computadores filtrados
    return render(request, 'tienda.html', {'computadores': computadores})

def detalle_computadora(request, id):
    computadora = get_object_or_404(Computadora, id=id)
    return render(request, 'detalle_computadora.html', {'computadora': computadora})