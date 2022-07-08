from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404


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
     comentario = get_object_or_404(ComentarioContacto, id=id)
     return render(request,"registros/formEditarComentario.html")
    #Indicamos el lugar donde se renderizará el resultado de esta vista

    # comentario = get_object_or_404(ComentarioContacto, id=id)
    # if request.method=='POST':
    #     comentario.delete()
    #     comentarios=ComentarioContacto.objects.all()
    #     return render(request,"registros/comentarios.html",{'comentarios':comentarios})
    # return render(request, confirmacion, {'object':comentario})