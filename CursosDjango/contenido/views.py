from django.shortcuts import render, HttpResponse

# Create your views here.

menu="""
    <a href="/">Principal</a>
    <a href="/cursos">Cursos</a>
    <a href="/contacto">Contactanos</a>
    """

def principal(request):
    contenido="""<h1>Bienvenido<h1>
    <p>Este portal es una practica para adaptarnos al Framework Django</p>"""
    return HttpResponse(menu+contenido)

def cursos(request):
    contenido="""<h1>Cursos<h1>
    <li> Base de Datos </li>
    <li> Programacion </li>
    <li> Java </li>"""
    return HttpResponse(menu+contenido)

def contacto(request):
    contenido="""<h2>Contacto<h2>
    <p>Nombre: <input type="text" name="nombre"></p>
    <p>Correo: <input type="mail" name="nombre"></p>
    <p>Cursos: 
    <select name="cursos">
     <option>Base de datos</option>
     <option>Programacion</option>
     <option>Java</option>
     <option>Phyton</option>
    </select>
    </p>
    <p>Comentarios: </p><p><textarea cols="50" rows="10"></textarea></p>
    <p><input type="Button" name="enviar" value="enviar"/></p>"""
    return HttpResponse(menu+contenido)