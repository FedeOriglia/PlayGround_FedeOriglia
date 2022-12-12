"""mtv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function viewsp
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
from ejemplo.views import (mostrar_familiares, BuscarFamiliar, AltaFamiliar, mostrar_autos, AltaAuto, BuscarAuto, mostrar_mascota, AltaMascota, BuscarMascota)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-familia/familia', mostrar_familiares),
    path('mi-familia/autos', mostrar_autos),
    path('mi-familia/mascotas', mostrar_mascota),
    path('mi-familia/buscar_familiar', BuscarFamiliar.as_view()),
    path('mi-familia/alta_familiar', AltaFamiliar.as_view()),
    path('mi-familia/buscar_auto', BuscarAuto.as_view()),
    path('mi-familia/alta_auto', AltaAuto.as_view()),
    path('mi-familia/buscar_mascota', BuscarMascota.as_view()),
    path('mi-familia/alta_mascota', AltaMascota.as_view()),
    ]
