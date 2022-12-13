from django.shortcuts import render, get_object_or_404 # <----- Nuevo import
from ejemplo.models import Familiar, Auto, Mascota
from ejemplo.forms import BuscarFamiliar, FamiliarForm, BuscarAuto, AutoForm, MascotaForm, BuscarMascota  #<--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT

# Create your views here.

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_autos(request):
    lista_autos = Auto.objects.all()
    return render(request, "ejemplo/autos.html", {"lista_autos": lista_autos})

def mostrar_mascota(request):
    lista_mascotas = Mascota.objects.all()
    return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})


class BuscarFamiliar(View):
    form_class = BuscarFamiliar
    template_name = "ejemplo/buscar.html"
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {"form":form, 
                                                        "lista_familiares":lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = "ejemplo/alta_familiar.html"
    initial = {"nombre":"", "dni":"", "fecha_nac":"", "direccion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f'se cargo con éxito el familiar {form.cleaned_data.get("nombre")}'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {"form":form, 
                                                        "msg_exito": msg_exito})
        
        return render(request, self.template_name, {"form": form})

class BuscarAuto(View):
    form_class = BuscarAuto
    template_name = "ejemplo/buscar_auto.html"
    initial = {"marca":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            marca = form.cleaned_data.get("marca")
            lista_autos = Auto.objects.filter(marca__icontains=marca).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {"form":form, 
                                                        "lista_autos":lista_autos})
        return render(request, self.template_name, {"form": form})

class AltaAuto(View):

    form_class = AutoForm
    template_name = "ejemplo/alta_auto.html"
    initial = {"marca":"", "modelo":"", "anio":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f'se cargo con éxito el auto {form.cleaned_data.get("marca")}'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {"form":form, 
                                                        "msg_exito": msg_exito})
        
        return render(request, self.template_name, {"form": form})

class BuscarMascota(View):
    form_class = BuscarMascota
    template_name = "ejemplo/buscar_mascota.html"
    initial = {"especie":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            especie = form.cleaned_data.get("especie")
            lista_mascotas = Mascota.objects.filter(especie__icontains=especie).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {"form":form, 
                                                        "lista_mascotas":lista_mascotas})
        return render(request, self.template_name, {"form": form})

class AltaMascota(View):
    form_class = MascotaForm
    template_name = "ejemplo/alta_mascota.html"
    initial = {"especie":"", "nombre":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f'se cargo con éxito la mascota {form.cleaned_data.get("especie")}'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {"form":form, 
                                                        "msg_exito": msg_exito})
        
        return render(request, self.template_name, {"form": form})