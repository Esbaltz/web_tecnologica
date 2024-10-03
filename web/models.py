from django.db import models

# Create your models here.

class Computadora(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)  
    marca = models.CharField(max_length=50) 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='computadoras/', blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre  