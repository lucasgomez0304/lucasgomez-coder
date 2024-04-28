from django.shortcuts import render

from . import models

def home(request):
    busqueda = models.Publicacion.objects.all()
    context = {"publicaciones": busqueda}
    return render(request, "publicacion/index.html", context)