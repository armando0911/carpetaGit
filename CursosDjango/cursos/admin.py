from django.contrib import admin
from .models import Cursos

# Register your models here.

class VisualizarNoVi (admin.ModelAdmin):
    readonly_fields = ('id','created','updated')

admin.site.register(Cursos,VisualizarNoVi)
# Cursos es el nombre de nuestro clase
# en el archivo models.py de la app registro
