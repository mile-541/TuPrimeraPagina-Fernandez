from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Dueño, Mascota, Turno
import json
from datetime import datetime

def index(request):
    """Vista principal que muestra el dashboard de la veterinaria"""
    context = {
        "mensaje": 'Bienvenido a Veterinaria "Las patitas"',
        "alumna": "Milena Fernández",
        "total_dueños": Dueño.objects.count(),
        "total_mascotas": Mascota.objects.count(),
        "total_turnos": Turno.objects.count(),
        "turnos_pendientes": Turno.objects.filter(fecha__gt=datetime.now()).count()
    }
    return render(request, "miapp/index.html", context)

@csrf_exempt
def dueños(request):
    """Vista para mostrar y gestionar dueños"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_dueño = Dueño.objects.create(
                nombre=data['nombre'],
                apellido=data['apellido'],
                telefono=data['telefono'],
                email=data['email']
            )
            return JsonResponse({'success': True, 'id': nuevo_dueño.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    # Búsqueda
    query = request.GET.get('q', '')
    if query:
        dueños = Dueño.objects.filter(
            nombre__icontains=query
        ) | Dueño.objects.filter(
            apellido__icontains=query
        )
    else:
        dueños = Dueño.objects.all()
    
    context = {'dueños': dueños, 'query': query}
    return render(request, 'miapp/dueños.html', context)

@csrf_exempt
def mascotas(request):
    """Vista para mostrar y gestionar mascotas"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dueño = get_object_or_404(Dueño, id=data['dueño_id'])
            nueva_mascota = Mascota.objects.create(
                dueño=dueño,
                nombre=data['nombre'],
                especie=data['especie'],
                sexo=data['sexo'],
                edad=data['edad']
            )
            return JsonResponse({'success': True, 'id': nueva_mascota.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    # Búsqueda
    query = request.GET.get('q', '')
    if query:
        mascotas = Mascota.objects.filter(
            nombre__icontains=query
        ) | Mascota.objects.filter(
            especie__icontains=query
        )
    else:
        mascotas = Mascota.objects.all()
    
    context = {
        'mascotas': mascotas, 
        'query': query,
        'dueños': Dueño.objects.all()
    }
    return render(request, 'miapp/mascotas.html', context)

@csrf_exempt
def turnos(request):
    """Vista para mostrar y gestionar turnos"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dueño = get_object_or_404(Dueño, id=data['dueño_id'])
            mascota = get_object_or_404(Mascota, id=data['mascota_id'])
            
            # Convertir string de fecha a datetime
            fecha = datetime.fromisoformat(data['fecha'].replace('Z', '+00:00'))
            
            nuevo_turno = Turno.objects.create(
                dueño=dueño,
                mascota=mascota,
                fecha=fecha,
                motivo=data['motivo']
            )
            return JsonResponse({'success': True, 'id': nuevo_turno.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    # Búsqueda
    query = request.GET.get('q', '')
    if query:
        turnos = Turno.objects.filter(
            motivo__icontains=query
        ) | Turno.objects.filter(
            mascota__nombre__icontains=query
        )
    else:
        turnos = Turno.objects.all().order_by('fecha')
    
    context = {
        'turnos': turnos, 
        'query': query,
        'dueños': Dueño.objects.all(),
        'mascotas': Mascota.objects.all()
    }
    return render(request, 'miapp/turnos.html', context)

def get_mascotas_by_dueño(request, dueño_id):
    """API para obtener mascotas de un dueño específico"""
    try:
        dueño = get_object_or_404(Dueño, id=dueño_id)
        mascotas = Mascota.objects.filter(dueño=dueño)
        mascotas_data = [{'id': m.id, 'nombre': m.nombre} for m in mascotas]
        return JsonResponse({'success': True, 'mascotas': mascotas_data})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def get_turnos_by_mascota(request, mascota_id):
    """API para obtener turnos de una mascota específica"""
    try:
        mascota = get_object_or_404(Mascota, id=mascota_id)
        turnos = Turno.objects.filter(mascota=mascota).order_by('-fecha')
        turnos_data = []
        
        for turno in turnos:
            turnos_data.append({
                'id': turno.id,
                'fecha': turno.fecha.strftime('%d/%m/%Y %H:%M'),
                'motivo': turno.motivo,
                'dueño': f"{turno.dueño.nombre} {turno.dueño.apellido}",
                'es_pendiente': turno.es_pendiente
            })
        
        return JsonResponse({'success': True, 'turnos': turnos_data})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})