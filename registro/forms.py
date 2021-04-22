from django import forms
from .models import Incidencia

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['autor','descripcion','acciones','estatus']
        labels = {
            'autor': 'Autor',
            'descripcion': 'Descripción',
            'acciones': 'Acciones',
            'estatus': 'Estatus'
        }
        opciones = [
            ('Abierto', 'Abierto'),
            ('Cerrado', 'Cerrado'),
        ]
        widgets = {
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'acciones': forms.Textarea(attrs={'class':'form-control'}),
            'estatus': forms.Select(choices=opciones, attrs={'class':'form-control'})
        }

class AccionesForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['acciones']
        labels = {
            'acciones': 'Acciones',
        }
        widgets = {
            'acciones': forms.Textarea(attrs={'class':'form-control'})
        }

class CambioEstatusForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['estatus','cambioEstatus']
        labels = {
            'estatus': "Estatus",
            'cambioEstatus': 'Motivo del cambio de estatus'
        }
        opciones = [
            ('Abierto', 'Abierto'),
            ('Cerrado', 'Cerrado'),
        ]
        widgets = {
            'estatus': forms.Select(choices=opciones, attrs={'class':'form-control'}),
            'cambioEstatus': forms.TextInput(attrs={'class':'form-control'})
        }