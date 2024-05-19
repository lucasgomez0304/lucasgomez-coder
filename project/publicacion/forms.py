from django import forms

from . import models

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = models.Publicacion
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
        }


class CiudadForm(forms.ModelForm):
    class Meta:
        model = models.Ciudad
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),   
        }

class PaisForm(forms.ModelForm):
    class Meta:
        model = models.Pais
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),   
        }