from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("nuevaIncidencia", views.nuevaIncidencia, name="nuevaIncidencia"),
	path("editarAcciones/<int:incidencia_id>", views.editarAcciones, name="editarAcciones"),
	path("eliminar/<int:incidencia_id>", views.eliminar, name="eliminar"),
	path("cambiarEstatus/<int:incidencia_id>", views.cambiarEstatus, name="cambiarEstatus")
]