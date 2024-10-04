from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import tienda, registro, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name='login'),  
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('tienda/', tienda, name='tienda'),
    path('registro/', registro, name='registro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
