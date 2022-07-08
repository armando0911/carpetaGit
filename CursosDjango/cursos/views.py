from django.shortcuts import render
from .models import Cursos
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
from .forms import RegistroCursoForm
# Create your views here.


def cursos(request):
    cursos=Cursos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "cursos/principal.html",{'cursos':cursos})
    #Indicamos el lugar donde se renderizará el resultado de
    #esta vista

def contacto(request):
    cursos=Cursos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "cursos/contacto.html",{'cursos':cursos})
    #Indicamos el lugar donde se renderizará el resultado de
    #esta vista

def registrar(request):
    if request.method == 'POST':
        form = RegistroCursoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
                form.save() #inserta
                return render(request,'cursos/contacto.html') 
    form = RegistroCursoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'cursos/contacto.html',{'form':form})  

# def contacto(request):
#     return render(request,"cursos/contacto.html")
#     #Indicamos el lugar donde se renderizará el resultado de esta vista
