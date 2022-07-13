from unicodedata import name
from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id_a','matricula', 'nombre', 'carrera','turno','created')
    ##Daremos formato a la tabla de alumnos separando en columnas:^^
    search_fields = ('matricula','nombre','carrera','turno')
    ##Agregando un formulario de busqueda:^^
    date_hierarchy = 'created'
    ##Agregando busqueda por fecha^^
    list_filter = ('carrera','turno')
    ##Agregando filtro lateral^^

    def get_readonly_fields(self, request, obj=None):
        #si pertenece al grupo de permisis "usuario"
        if request.user.groups.filter(name="usuarios").exists():
            #bloquea los campos
            return('matricula','carrera','turno')
            #'created','updated',cualquier otro usuario que no pertenesca al grupo "usuario"
        else:
            #bloquea de los campos
            return('created','updated')

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
