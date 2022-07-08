from django.contrib import admin
from .models import Cursos
from .models import Actividad
from .models import Registro

# Register your models here.

class VisualizarNoVi (admin.ModelAdmin):
    readonly_fields = ('id','created','updated')
    list_display = ('nombre', 'descripcion','duracion_hrs','instructor')
    search_fields = ('nombre', 'descripcion','duracion_hrs','instructor')
    date_hierarchy = 'created'
    list_filter = ('duracion_hrs','instructor')

admin.site.register(Cursos,VisualizarNoVi)
# Cursos es el nombre de nuestro clase
# en el archivo models.py de la app registro

class AdministrarAct(admin.ModelAdmin):
    list_display = ('id_act','curso','descripcion_act','created')
    search_fields = ('id','created')
    date_hierarchy ='created'
    readonly_fields = ('created','id_act')
    

admin.site.register(Actividad,AdministrarAct)


class AdministrarRegistrosCursos(admin.ModelAdmin):
    list_display = ('id_registro', 'nombre_u', 'apellido_p','apellido_m','correo','curso_u','mensaje_u','created')
    search_fields = ('id_registro','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id_registro')

admin.site.register(Registro, AdministrarRegistrosCursos)
