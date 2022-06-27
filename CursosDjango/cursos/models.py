from django.db import models

# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True, verbose_name="Identificador") #id
    nombre = models.TextField(max_length=40, verbose_name="Nombre del curso") #Texto corto
    descripcion = models.TextField() #Texto largo
    duracion_hrs = models.PositiveIntegerField(verbose_name="Horas de duración")
    instructor = models.TextField(max_length=30)
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
        #el menos indica que se ordenara del más viejo al mas reciente

    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla

    