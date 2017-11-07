from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext
from .forms import AsignacionForm, VehiculoForm, RepuestoForm
from .models import Vehiculo, Repuesto, Asignacion
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

#-------------------------- Vista de vehiculo-----------------------------------

def vehiculo_lista(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'repuestosapp/vehiculo_lista.html', {'vehiculos':vehiculos})

def vehiculo_detalle(request, pk):
    vehiculos = get_object_or_404(Vehiculo, pk=pk)
    return render(request, 'repuestosapp/vehiculo_detalle.html', {'vehiculos': vehiculos})

def vehiculo_nuevo(request):
    if request.method == "POST":
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            vehiculo = Vehiculo(marca = formulario.cleaned_data['marca'], duenio = formulario.cleaned_data['duenio'], anio = formulario.cleaned_data['anio'])
            vehiculo.save()
        return redirect('repuestosapp.views.vehiculo_lista')
    else:
        formulario = VehiculoForm()
    return render(request, 'repuestosapp/vehiculo_nuevo.html', {'formulario': formulario})

def vehiculo_editar(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == "POST":
        formulario = VehiculoForm(request.POST, instance=vehiculo)
        if formulario.is_valid():
            vehiculo = formulario.save(commit=False)
            vehiculo.save()
        return redirect('repuestosapp.views.vehiculo_lista')
    else:
        formulario = VehiculoForm(instance=vehiculo)
    return render(request, 'repuestosapp/vehiculo_editar.html', {'formulario': formulario})

def vehiculo_del(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    vehiculo.delete()
    return redirect('repuestosapp.views.vehiculo_lista')

#-------------------------- Vista de Repuestos -----------------------------------

def repuesto_lista(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'repuestosapp/repuesto_lista.html', {'repuestos':repuestos})

def repuesto_detalle(request, pk):
    repuestos = get_object_or_404(Repuesto, pk=pk)
    return render(request, 'repuestosapp/repuesto_detalle.html', {'repuestos': repuestos})

def repuesto_nuevo(request):
    if request.method == "POST":
        formulario = RepuestoForm(request.POST)
        if formulario.is_valid():
            repuesto = formulario.save(commit=False)
            repuesto = RepuestoForm(nombre= formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'],cantidad = formulario.cleaned_data['cantidad'])
            repuesto.save()
        return redirect('repuesto_lista')
    else:
        formulario = RepuestoForm()
    return render(request, 'repuestosapp/repuesto_nuevo.html', {'formulario': formulario})


def repuesto_editar(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    if request.method == "POST":
        formulario = RepuestoForm(request.POST, instance=repuesto)
        if formulario.is_valid():
            repuesto = formulario.save(commit=False)
            repuesto.save()
        return redirect('repuestosapp.views.repuesto_lista')
    else:
        formulario = RepuestoForm(instance=repuesto)
    return render(request, 'repuestosapp/repuesto_editar.html', {'formulario': formulario})

def repuesto_del(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    repuesto.delete()
    return redirect('repuestosapp.views.repuesto_lista')


##------------------Asignacion--------------------------------------

def asignacion_lista(request):
    asignaciones = Asignacion.objects.all()
    return render(request, 'repuestosapp/asignacion_lista.html', {'asignaciones':asignaciones})

def asignacion_detalle(request, pk):
    asignaciones = get_object_or_404(Asignacion, pk=pk)
    return render(request, 'repuestosapp/asignacion_detalle.html', {'asignaciones': asignaciones})

def asignacion_nueva(request):
    if request.method == "POST":
        formulario = AsignacionForm(request.POST)
        if formulario.is_valid():
            asignacion = formulario.save(commit=False)
            for vehiculo_id in request.POST.getlist('vehiculo'):
                for repuesto_id in request.POST.getlist('repuesto'):
                    asignacion = Asignacion(vehiculo_id=vehiculo_id, repuesto_id = repuesto_id)
                    asignacion.save()
        return redirect('repuestosapp.views.asignacion_lista')
    else:
        formulario = AsignacionForm()
    return render(request, 'repuestosapp/asignacion_nueva.html', {'formulario': formulario})

def asignacion_editar(request, pk):
    asignacion = get_object_or_404(Asignacion, pk=pk)
    if request.method == "POST":
        formulario = AsignacionForm(request.POST, instance=asignacion)
        if formulario.is_valid():
            asignacion = formulario.save(commit=False)
            for vehiculo_id in request.POST.getlist('vehiculo'):
                for repuesto_id in request.POST.getlist('repuesto'):
                    asignacion.save()
        return redirect('repuestosapp.views.asignacion_lista')
    else:
        formulario = AsignacionForm(instance=asignacion)
    return render(request, 'repuestosapp/asignacion_editar.html', {'formulario': formulario})

def asignacion_del(request, pk):
    asignacion = get_object_or_404(Asignacion, pk=pk)
    asignacion.delete()
    return redirect('repuestosapp.views.asignacion_lista')
