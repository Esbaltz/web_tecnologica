from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import login, tienda

urlpatterns = [
    path('', login, name='login'),
    path('tienda/', tienda, name='tienda'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)