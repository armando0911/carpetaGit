from django.contrib import admin
from .models import Alumnos

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
