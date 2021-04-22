from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Incidencia
from .filters import IncidenciaFilter
from .forms import IncidenciaForm, AccionesForm, CambioEstatusForm


def index(request):
    incidencias = Incidencia.objects.all()
    filtro = IncidenciaFilter(request.GET, queryset=incidencias)
    incidencias = filtro.qs
    return render(request, "registro/index.html", {
        "incidencias": incidencias,
        "filtro": filtro
    })

def nuevaIncidencia(request):
    if request.method == "POST":
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "registro/nuevaIncidencia.html", {
            "formIncidencia": IncidenciaForm()
        })
        
def editarAcciones(request,incidencia_id):
    incidencia = Incidencia.objects.get(pk=incidencia_id)
    if request.method == "POST":
        form = AccionesForm(request.POST)
        if form.is_valid():
            incidencia.acciones = form.cleaned_data["acciones"]
            incidencia.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AccionesForm() 
        form.fields["acciones"].initial = incidencia.acciones
        return render(request, "registro/editarAcciones.html", {
            "formAcciones": form,
            "incidencia_id": incidencia_id
        })

def cambiarEstatus(request,incidencia_id):
    incidencia = Incidencia.objects.get(pk=incidencia_id)
    if request.method == "POST":
        form = CambioEstatusForm(request.POST)
        if form.is_valid():
            incidencia.estatus = form.cleaned_data["estatus"]
            incidencia.cambioEstatus = form.cleaned_data["cambioEstatus"]
            incidencia.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CambioEstatusForm()
        form.fields["estatus"].initial = incidencia.estatus
        form.fields["cambioEstatus"].initial = ""
        return render(request, "registro/cambiarEstatus.html", {
            "formCambioEstatus": form,
            "incidencia_id": incidencia_id
        })

def eliminar(request,incidencia_id):
    incidencia = Incidencia.objects.get(pk=incidencia_id)
    incidencia.delete()
    return HttpResponseRedirect(reverse("index"))


