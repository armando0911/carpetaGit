from turtle import ondrag, update
from django.db import models

# Create your models here.

class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat") #texto corto
    nombre = models.TextField() #texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
        #el menos indica que se ordenara del mas reciente al mas viejo
    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla
    

