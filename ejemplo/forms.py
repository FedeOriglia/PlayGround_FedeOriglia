from django import forms
from ejemplo.models import Familiar, Auto, Mascota

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'placeholder':'Escribir un Nombre'}))

class BuscarAuto(forms.Form):
    marca = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'placeholder':'Escribir Marca'}))

class BuscarMascota(forms.Form):
    especie = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'placeholder':'Escribir Especie'}))
    
class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'dni', 'fecha_nac', 'direccion']

class AutoForm(forms.ModelForm):
  class Meta:
    model = Auto
    fields = ['marca', 'modelo', 'anio']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['especie', 'nombre', 'edad']