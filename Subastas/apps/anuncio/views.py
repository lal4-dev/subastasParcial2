from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse

#para los reportes no tocar(de lala para belicho)
from .models import Anuncio,OfertaAnuncio, SeguimientoAnuncio, Categoria
from .forms import AnuncioForm


# Create your views here.

def listarAnunciosView(request):
    anunciosVista = Anuncio.objects.all()

    contexto = {
        'anuncios':anunciosVista
    }

    return render(request,'',contexto)


def crearAnuncioView(request):
    anuncioNuevo = None
    if request.method == 'POST':
        anuncioFormView = AnuncioForm(request.POST)
        if anuncioFormView.is_valid():
            anuncioNuevo = anuncioFormView.save(commit=False)
            anuncioNuevo.publicadoPor = request.user
            anuncioNuevo.save()
            anuncioNuevo.save_m2m()

            return redirect('')
    
    else:
        anuncioFormView = AnuncioForm()

    contexto={
        'anuncio' : anuncioFormView
    }

    return render(request, '',contexto)


def modificarAnuncioView(request, pk):
    anuncioViejo = get_object_or_404(Anuncio,pk=pk )

    if request.method == 'POST':
        anuncioNuevoFormView = AnuncioForm(request.POST, instace = anuncioViejo)
        if anuncioNuevoFormView.is_valid():
            anuncioNuevoFormView.save(commit = True)

            return redirect('')
        
    else:
        anuncioNuevoFormView = AnuncioForm(instance = anuncioViejo)

    contexto = {
        'anuncio': anuncioNuevoFormView
    }

    return render(request, '',contexto)

def bajaAnuncioView( request, pk):
    bajaAnuncio= get_object_or_404(Anuncio, pk=pk)
    bajaAnuncio.delete()

    return redirect('')