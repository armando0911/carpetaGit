from tkinter import Widget
from django import forms
from .models import ComentarioContacto
from .models import Alumnos
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario','mensaje']

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['matricula','nombre','carrera','turno']


##Archivos 
class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_idar)s">%(clear_checkbox_label)s</label>%(clear)s'
    ##ClearableFileInput: Widget de los campos FileField, permite que al subir un archivo a un formulario
    # y luego se edita se visualizarán dos campos más. El primero un checkbox de nombre clear, que se
    # encarga de borrar de la base de datos el archivo, y el segundo campo es un input file que permite
    # modificar el archivo que uno subió.

class FormArchivos (ModelForm):
    class Meta:
        model = Archivos
        fields = ('titulo','descripcion','archivo')
        widgets = {
            'archivo': CustomClearableFileInput
        }



