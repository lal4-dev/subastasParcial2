from django import forms

from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo',
                  'descripcion',
                  'precioInicial',
                  'imagen',
                  'fechaPublicacion',
                  'fechaInicio',
                  'fechaFin',
                  'activo',
                  'categorias',
                  'publicadoPor',
                  'ofertaGanadora']
        
        widgtes={}

        labels={}