"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # Ahora la página principal es el dashboard
    path('accounts/', include('django.contrib.auth.urls')),  # Sistema de autenticación
    path('registro/', views.registro, name='registro'),
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('actividades/nueva/', views.crear_actividad, name='crear_actividad'),
    path('actividades/editar/<int:actividad_id>/', views.editar_actividad, name='editar_actividad'),
    path('actividades/eliminar/<int:actividad_id>/', views.eliminar_actividad, name='eliminar_actividad'),
    path('api/notas/', views.obtener_notas, name='obtener_notas'),
    path('api/agregar_nota/', views.agregar_nota, name='agregar_nota'),
    path('calendario/', views.calendario, name='calendario'),
    path('videos/', views.lista_videos, name='lista_videos'),
]


