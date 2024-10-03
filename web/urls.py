from django.urls import path
from .views import login, tienda

urlpatterns = [
    path('', login, name='login'),
    path('tienda/', tienda, name='tienda'),
]