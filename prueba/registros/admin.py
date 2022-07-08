from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera','turno')
    ##Daremos formato a la tabla de alumnos separando en columnas:^^
    search_fields = ('matricula','nombre','carrera','turno')
    ##Agregando un formulario de busqueda:^^
    date_hierarchy = 'created'
    ##Agregando busqueda por fecha^^
    list_filter = ('carrera','turno')
    ##Agregando filtro lateral^^

admin.site.register(Alumnos, AdministrarModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy ='created'
    readonly_fields = ('created','id')
    

admin.site.register(Comentario,AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

    
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
