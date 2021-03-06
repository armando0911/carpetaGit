"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
##importar 
from inicio import views
from django.conf import settings
#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que
#almacenan la ubicación de nuestras imagenes
from registros import views as views_registros
#Importamos la nueva vista de app registros para
#poder asignar las rutas de acceso a sus vistas 

urlpatterns = [
    path('admin/', admin.site.urls),
    ##agregar la vista
    # path('',views.principal, name="Principal"),
    path('',views_registros.registros, name="Principal"),
    #Indicamos que ahora la ruta de principal.html se
    #encuentra en la view de registros
    #path('contacto/',views.contacto, name="Contacto"),
    path('contacto/',views_registros.contacto,name="Contacto"),
    path('formulario/',views.formulario, name="Formulario"),
    path('comentarios',views_registros.verComentarioContacto, name="Comentario"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('ejemplo/',views.ejemplo, name="Ejemplo"),

    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('verFormEditarComentario/<int:id>/',views_registros.verFormEditarComentario,name='Editar'),
    path('editandoComentario/<int:id>/',views_registros.editarComentario,name='editarComentario'),

    path('eliminarAlumno/<int:id_a>/',views_registros.eliminarAlumno,name='Eliminar_a'),
    path('verFormEditarAlumno/<int:id_a>/',views_registros.verFormEditarAlumno,name='Editar_a'),
    path('editandoAlumno/<int:id_a>/',views_registros.editarAlumno,name='editarAlumno'),
    #Consultas >
    path('consulta/',views_registros.consultar1,name='Consultas'),
    path('consulta2/',views_registros.consultar2,name='Consultas'),
    path('consulta3/',views_registros.consultar3,name='Consultas'),
    path('consulta4/',views_registros.consultar4,name='Consultas'),
    path('consulta5/',views_registros.consultar5,name='Consultas'),
    path('consulta6/',views_registros.consultar6,name='Consultas'),
    path('consulta7/',views_registros.consultar7,name='Consultas'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)


