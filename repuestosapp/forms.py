from django import forms
from .models import Vehiculo, Repuesto, Asignacion

class AsignacionForm(forms.ModelForm):
#todos los campos de Bodega
    class Meta:
        model = Asignacion
        fields = ('repuesto', 'vehiculo')

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.

def __init__ (self, *args, **kwargs):
        super(AsignacionForm, self).__init__(*args, **kwargs)
#ModelChoiceField(queryset=Books.objects.all().order_by('name'))
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["repuesto"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["repuesto"].queryset = Repuesto.objects.all()
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["vehiculo"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["vehiculo"].queryset = Vehiculo.objects.all()


class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ('marca', 'duenio','anio')


class RepuestoForm(forms.ModelForm):

    class Meta:
        model = Repuesto
        fields = ('nombre', 'descripcion','cantidad',)
