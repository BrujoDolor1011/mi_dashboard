from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

@login_required  # Solo usuarios autenticados pueden ver el dashboard
def dashboard(request):
    return render(request, 'mi_app/dashboard.html')  # ✅ Esto busca en templates/mi_app/

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('dashboard')  # Redirigir al dashboard tras registrarse
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Actividad
from .forms import ActividadForm

@login_required
def lista_actividades(request):
    actividades = Actividad.objects.filter(usuario=request.user)
    return render(request, 'mi_app/lista_actividades.html', {'actividades': actividades})

@login_required
def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.usuario = request.user
            actividad.save()
            return redirect('lista_actividades')
    else:
        form = ActividadForm()
    return render(request, 'mi_app/form_actividad.html', {'form': form})

@login_required
def editar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id, usuario=request.user)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'mi_app/form_actividad.html', {'form': form})

@login_required
def eliminar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id, usuario=request.user)
    if request.method == 'POST':
        actividad.delete()
        return redirect('lista_actividades')
    return render(request, 'mi_app/confirmar_eliminar.html', {'actividad': actividad})

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NotaCalendario
from django.contrib.auth.decorators import login_required

@login_required
def obtener_notas(request):
    notas = NotaCalendario.objects.filter(usuario=request.user)
    eventos = [{"title": nota.contenido, "start": nota.fecha.strftime("%Y-%m-%d")} for nota in notas]
    return JsonResponse(eventos, safe=False)

@csrf_exempt
@login_required
def agregar_nota(request):
    if request.method == "POST":
        data = json.loads(request.body)
        fecha = data.get("fecha")
        contenido = data.get("contenido")

        nota, created = NotaCalendario.objects.get_or_create(usuario=request.user, fecha=fecha)
        nota.contenido = contenido
        nota.save()

        return JsonResponse({"mensaje": "Nota guardada con éxito"})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def calendario(request):
    return render(request, 'mi_app/calendario.html')

from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

def lista_videos(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_videos')  # Redirige después de agregar un video
    else:
        form = VideoForm()

    videos = Video.objects.all()
    return render(request, 'mi_app/lista_videos.html', {'form': form, 'videos': videos})

