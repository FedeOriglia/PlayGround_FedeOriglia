from django.db import models

# Create your models here.

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField()
    fecha_nac =models.DateField(default=True)
    direccion = models.CharField(max_length=200)
        
    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.dni}, {self.fecha_nac}, {self.direccion}"

class Auto(models.Model):
    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
        
    def __str__(self):
        return f"{self.id}, {self.marca}, {self.modelo}, {self.anio}"

class Mascota(models.Model):
    
    especie = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
        
    def __str__(self):
        return f"{self.id}, {self.especie}, {self.nombre}, {self.edad}"