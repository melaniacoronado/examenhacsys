from django.db import models

class Incidencia(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField(max_length=100)
    autor = models.CharField(max_length=50)
    acciones = models.TextField(max_length=200)
    estatus = models.CharField(max_length=20)
    cambioEstatus = models.CharField(max_length=30, null=True, default="Sin cambio")

def __str__(self):
    return f"{self.autor} {self.descripcion} {self.fecha}"

