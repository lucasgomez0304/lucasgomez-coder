from django.shortcuts import render

from . import models

def home(request):
    publicaciones = models.Publicacion.objects.all()
    context = {"publicacion": publicaciones}
    return render(request, "publicacion/index.html", context)