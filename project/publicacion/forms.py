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

from .models import Ciudad, Pais, Concepto

class PublicacionFilterForm(forms.Form):
    ciudad = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        required=False,
        label='Ciudad',
        widget=forms.Select(attrs={'placeholder': 'Ciudad'})
    )
    concepto = forms.ModelChoiceField(
        queryset=Concepto.objects.all(),
        required=False,
        label='Concepto',
        widget=forms.Select(attrs={'placeholder': 'Concepto'})
    )

    def __init__(self, *args, **kwargs):
        super(PublicacionFilterForm, self).__init__(*args, **kwargs)
        self.fields['ciudad'].empty_label = "Ciudad"
        self.fields['concepto'].empty_label = "Concepto"