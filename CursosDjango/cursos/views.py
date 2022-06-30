from django.shortcuts import render
from .models import Cursos
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.

# Create your views here.


def cursos(request):
    cursos=Cursos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "cursos/principal.html",{'cursos':cursos})
    #Indicamos el lugar donde se renderizará el resultado de
    #esta vista

