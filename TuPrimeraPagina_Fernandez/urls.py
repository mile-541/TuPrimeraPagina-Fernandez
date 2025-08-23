"""
URL configuration for TuPrimeraPagina_Fernandez project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from miapp.views import index, dueños, mascotas, turnos, get_mascotas_by_dueño, get_turnos_by_mascota

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('dueños/', dueños, name="dueños"),
    path('mascotas/', mascotas, name="mascotas"),
    path('turnos/', turnos, name="turnos"),
    path('api/mascotas/<int:dueño_id>/', get_mascotas_by_dueño, name="get_mascotas_by_dueño"),
    path('api/turnos/<int:mascota_id>/', get_turnos_by_mascota, name="get_turnos_by_mascota"),
]