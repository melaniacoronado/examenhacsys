import django_filters
from django_filters.filters import CharFilter, ChoiceFilter
from .models import *
from django_filters import DateFilter,DateRangeFilter,DateTimeFromToRangeFilter
from django import forms

opciones = [
            ('Abierto', 'Abierto'),
            ('Cerrado', 'Cerrado'),
        ]

class IncidenciaFilter(django_filters.FilterSet):
    fecha = DateRangeFilter(field_name='fecha')
    descripcion = CharFilter(field_name='descripcion', lookup_expr='icontains', label="Descripción:")
    autor = CharFilter(field_name='autor', lookup_expr='icontains', label="Autor:")
    acciones = CharFilter(field_name='acciones', lookup_expr='icontains', label="Acciones:")
    estatus = ChoiceFilter(field_name='estatus', choices=opciones)
    
    class Meta:
        model = Incidencia
        fields = '__all__'
        exclude = ['cambioEstatus']