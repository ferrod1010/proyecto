from django.contrib import admin
from repuestosapp.models import Repuesto, RepuestoAdmin, Vehiculo, VehiculoAdmin, Asignacion

#Registramos nuestras clases principales.
admin.site.register(Repuesto, RepuestoAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Asignacion)
