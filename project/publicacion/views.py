from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import PublicacionFilterForm

from . import models, forms

def home(request):
    return render(request, "publicacion/index.html")

# *** PUBLICACION

# LIST
class PublicacionList(ListView):
    model = models.Publicacion

#    def get_queryset(self) -> QuerySet:
#        if self.request.GET.get("consulta"):
#            consulta = self.request.GET.get("consulta")
#            object_list = models.Publicacion.objects.filter(nombre__icontains=consulta)
#        else:
#            object_list = models.Publicacion.objects.all()
#        return object_list
    
    def get_queryset(self):
        queryset = super().get_queryset()

        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = queryset.filter(nombre__icontains=consulta)

        self.filter_form = PublicacionFilterForm(self.request.GET)
        if self.filter_form.is_valid():
            if self.filter_form.cleaned_data.get('pais'):
                queryset = queryset.filter(ciudad__pais=self.filter_form.cleaned_data['pais'])
            if self.filter_form.cleaned_data.get('ciudad'):
                queryset = queryset.filter(ciudad=self.filter_form.cleaned_data['ciudad'])
            if self.filter_form.cleaned_data.get('concepto'):
                queryset = queryset.filter(concepto=self.filter_form.cleaned_data['concepto'])
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        return context

# CREAR
class PublicacionCreate(LoginRequiredMixin, CreateView):
    model = models.Publicacion
    form_class = forms.PublicacionForm
    success_url = reverse_lazy("publicacion:publicacion_list")

# DETAIL
class PublicacionDetail(DetailView):
    model = models.Publicacion

# DELETE
class PublicacionDelete(LoginRequiredMixin, DeleteView):
    model = models.Publicacion
    success_url = reverse_lazy("publicacion:publicacion_list")

# UPDATE
class PublicacionUpdate(LoginRequiredMixin, UpdateView):
    model = models.Publicacion
    form_class = forms.PublicacionForm
    success_url = reverse_lazy("publicacion:publicacion_list")


# *** CIUDAD

# LIST
class CiudadList(ListView):
    model = models.Ciudad

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Ciudad.objects.filter(ciudad__icontains=consulta)
        else:
            object_list = models.Ciudad.objects.all()
        return object_list

# CREAR
class CiudadCreate(LoginRequiredMixin, CreateView):
    model = models.Ciudad
    form_class = forms.CiudadForm
    success_url = reverse_lazy("publicacion:ciudad_list")

# UPDATE
class CiudadUpdate(LoginRequiredMixin, UpdateView):
    model = models.Ciudad
    form_class = forms.CiudadForm
    success_url = reverse_lazy("publicacion:ciudad_list")

# DETAIL
class CiudadDetail(DetailView):
    model = models.Ciudad

# DELETE
class CiudadDelete(LoginRequiredMixin, DeleteView):
    model = models.Ciudad
    success_url = reverse_lazy("publicacion:ciudad_list")


# *** PAIS

# LIST
class PaisList(ListView):
    model = models.Pais

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Pais.objects.filter(pais__icontains=consulta)
        else:
            object_list = models.Pais.objects.all()
        return object_list

# CREAR
class PaisCreate(LoginRequiredMixin, CreateView):
    model = models.Pais
    form_class = forms.PaisForm
    success_url = reverse_lazy("publicacion:pais_list")

# UPDATE
class PaisUpdate(LoginRequiredMixin, UpdateView):
    model = models.Pais
    form_class = forms.PaisForm
    success_url = reverse_lazy("publicacion:pais_list")

# DETAIL
class PaisDetail(DetailView):
    model = models.Pais

# DELETE
class PaisDelete(LoginRequiredMixin, DeleteView):
    model = models.Pais
    success_url = reverse_lazy("publicacion:pais_list")