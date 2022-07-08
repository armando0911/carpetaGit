from django import forms
from .models import Registro

class RegistroCursoForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre_u','apellido_p','apellido_m','correo','curso_u','mensaje_u']
