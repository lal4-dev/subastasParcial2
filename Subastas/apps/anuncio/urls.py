from django.urls import path
from apps.anuncio import views

app_name = 'anuncio'

urlpatterns = [
    path('anuncio/agregar',views.crearAnuncioView,name='agregarAnuncio'),
    path('anuncio/listar',views.listarAnunciosView,name='listarAnuncios'),
    path('anuncio/modificar/<int:pk>',views.modificarAnuncioView,name='modificarAnuncios'),
    path('anuncio/eliminar/<int:pk>',views.bajaAnuncioView, name='bajaAnuncio')
]