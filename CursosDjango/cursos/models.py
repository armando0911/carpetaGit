from turtle import ondrag, update
from django.db import models
from tabnanny import verbose
from ckeditor.fields import RichTextField

# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True, verbose_name="Identificador") #id
    nombre = models.TextField(max_length=40, verbose_name="Nombre del curso") #Texto corto
    descripcion = models.TextField() #Texto largo
    duracion_hrs = models.PositiveIntegerField(verbose_name="Horas de duración")
    instructor = models.TextField(max_length=30)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    #agregamos el atributo
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

class Actividad(models.Model):
    id_act=models.AutoField(primary_key=True,verbose_name="Clave")
    curso = models.ForeignKey(Cursos,on_delete=models.CASCADE,verbose_name="Curso")
    descripcion_act = RichTextField(verbose_name="Actividad")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    # coment = RichTextField(verbose_name="Comentario")
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):
        return self.descripcion_act

class Registro(models.Model):
    id_registro = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre_u = models.TextField(verbose_name="Nombre")
    apellido_p = models.TextField(verbose_name="Apellido paterno")
    apellido_m = models.TextField(verbose_name="Apellido materno")
    correo = models.CharField(max_length=70, verbose_name="Correo")
    curso_u = models.ForeignKey(Cursos,on_delete=models.CASCADE,verbose_name="Curso")
    mensaje_u = models.TextField() #Texto largo
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ["-created"]
        def __str__(self):
            return self.mensaje_u
            #Indica que se mostrára el mensaje como valor en la tabla

