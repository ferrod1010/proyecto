from django.db import models
from django.contrib import admin


class Repuesto(models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion  =   models.CharField(max_length=70)
    cantidad     = models.IntegerField()

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    marca    = models.CharField(max_length=30)
    duenio    = models.CharField(max_length=30)
    anio      = models.IntegerField()
    def __str__(self):
        return self.marca

class Asignacion (models.Model):
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    def __str__(self):
        return self.vehiculo.duenio

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class RepuestoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class VehiculoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
