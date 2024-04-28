from django.shortcuts import render, redirect

from . import models, forms

def home(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Publicacion.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Publicacion.objects.all()
    context = {"publicaciones": query}
    return render(request, "publicacion/index.html", context)

def publicacion_crear(request):
    if request.method == "POST":
        form = forms.PublicacionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("publicacion:home")
    else:  # request.method == "GET"
        form = forms.PublicacionForm()
    return render(request, "publicacion/publicacion_crear.html", context={"form": form})
