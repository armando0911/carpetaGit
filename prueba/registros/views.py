from urllib import request
from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
from .forms import AlumnosForm, ComentarioContactoForm
from django.shortcuts import get_object_or_404
##Archivos
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

import datetime
# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/principal.html",{'alumnos':alumnos})
    #Indicamos el lugar donde se renderizará el resultado de
    #esta vista
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados

def verComentarioContacto(request):
    comentarios=ComentarioContacto.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/comentarios.html",{'comentarios':comentarios})
    #Indicamos el lugar donde se renderizará el resultado de
    #esta vista
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
                form.save() #inserta
                comentarios=ComentarioContacto.objects.all()
                return render(request,"registros/comentarios.html", {'comentarios':comentarios})
                    # return render(request,'registros/contacto.html')
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form}) 

def contacto(request):
    return render(request,"registros/contacto.html")
    #Indicamos el lugar donde se renderizará el resultado de esta vista


def eliminarComentarioContacto(request, id,confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})


def verFormEditarComentario(request,id):
    comentario = ComentarioContacto.objects.get(id=id)
#  return render(request,"registros/formEditarComentario.html")
#Indicamos el lugar donde se renderizrá el resultado de esta vista
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})
    # comentario = get_object_or_404(ComentarioContacto, id=id)
    # if request.method=='POST':
    #     comentario.delete()
    #     comentarios=ComentarioContacto.objects.all()
    #     return render(request,"registros/comentarios.html",{'comentarios':comentarios})
    # return render(request, confirmacion, {'object':comentario})

def editarComentario(request,id):
    comentario = get_object_or_404(ComentarioContacto,id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #referenciamos que el elemento del formulario pertenece al comentario ya existente
    if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/comentarios.html", {'comentarios':comentarios})
                    # return render(request,'registros/contacto.html')
    return render(request,'registros/formEditarComentario.html',{'comentario': comentario}) 

##funciones de Alumnos

def eliminarAlumno(request, id_a,confirmacion='registros/confirmarEliminacionAlumno.html'):
    alumno = get_object_or_404(Alumnos, id_a=id_a)
    if request.method=='POST':
        alumno.delete()
        alumnos=Alumnos.objects.all()
        return render(request,"registros/principal.html",{'alumnos':alumnos})
    return render(request, confirmacion, {'object':alumno})

def verFormEditarAlumno(request,id_a):
    alumno = Alumnos.objects.get(id_a=id_a)
#  return render(request,"registros/formEditarComentario.html")
#Indicamos el lugar donde se renderizrá el resultado de esta vista
    return render(request,"registros/formEditarAlumno.html",
    {'alumno':alumno})

def editarAlumno(request,id_a):
    alumno = get_object_or_404(Alumnos,id_a=id_a)
    form = AlumnosForm(request.POST, instance=alumno)
    #referenciamos que el elemento del formulario pertenece al comentario ya existente
    if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            alumnos=Alumnos.objects.all()
            return render(request,"registros/principal.html", {'alumnos':alumnos})
                    # return render(request,'registros/contacto.html')
    return render(request,'registros/formEditarAlumno.html',{'alumno': alumno}) 


def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/consultas.html",{'alumnos':alumnos})
    

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio= datetime.date(2022,7,12)
    fechaFin=datetime.date(2022,7,14)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='ooo')
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/consultas.html",{'alumnos':alumnos})


##Archivos-----

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request,"Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})


##consultasSQL

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id_a,matricula,nombre,carrera,turno,imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request,"registros/consultas.html",{'alumnos':alumnos})

##Ejemplo de seguridad 
# def seguridad(request):
#     return render(request,"registros/seguridad.html")

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html",{'nombre':nombre})

