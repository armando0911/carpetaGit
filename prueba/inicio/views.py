import html
from html.entities import html5
from tkinter import Menu
from django.shortcuts import render, HttpResponse

# Create your views here git.
def principal(request):
    return render(request,"inicio/principal.html")

def contacto(request):
    return render(request,"inicio/contacto.html")

def formulario(request):
    return render(request,"inicio/formulario.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")


# menu="""
#     <a href="/">Home</a>
#     <a href="/contacto">Contactanos</a>
#     """

# def principal(request):
#     contenido="<h1>Holaaa Django<h1>"
#     return HttpResponse(menu+contenido)

# def contacto(request):
#     contenido="""<h2>Contacto<h2>
#     <p>Nombre: <input type="text" name="nombre"></p>
#     <p>Mensaje: </p><p><textarea cols="50" rows="10"></textarea></p>
#     <p><input type="Button" name="enviar" value="enviar"/></p>"""
#     return HttpResponse(contenido)