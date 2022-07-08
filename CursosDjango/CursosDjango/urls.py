"""CursosDjango URL Configuration

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
from contenido import views
from django.conf import settings
#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que
#almacenan la ubicación de nuestras imagenes 
from cursos import views as views_cursos
#Importamos la nueva vista de app registros para
#poder asignar las rutas de acceso a sus vistas


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views_cursos.cursos, name="Principal"),
    #Indicamos que ahora la ruta de principal.html se
    #encuentra en la view de registros
    # path('contacto/',views.contacto, name="Contacto"),
    path('contacto/',views_cursos.contacto,name="Contacto"),
    path('registrar/',views_cursos.registrar,name="Registrar"),
    path('cursos/',views.cursos, name="Cursos"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
