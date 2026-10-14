from django.db import models

class cliente (models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20)
    tipo_mascota = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.nombre

class Atencion (models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    monto = models.PositiveIntegerField()
    observacion = models.TextField()
    

