from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model): #Aca defino la clase Categoria
    nombre = models.CharField(max_length=200, unique=True) #Aca defino el atributo nombre de tipo char equivalente a un textinput en html

    def __str__(self): #defino el mensaje de la clase, cuando invoco a la clase me devuelve esto
        return self.nombre # el mensaje o campo que me devuelve


class Anuncio(models.Model): #Aca defino la clase Anuncio
    titulo = models.CharField(max_length=200) #Aca defino el atributo titulo de tipo char equivalente a un textinput en html
    descripcion = models.TextField(blank=True) #Aca defino el atributo descripcion de tipo text equivalente a un textArea en html, black true me dice que tenga el campo vacio ''
    precioInicial = models.DecimalField(decimal_places=2, max_digits=10) #Aca defino el atributo precioInicial de tipo decimal equivalente a un numerInput en html, decimal_places digitos despues de la coma y max digits la cantidad de numeros como entrada es decir 8 numeros antes de la coma
    imagen = models.FileField() #Aca defino el atributo imagen de tipo field equivalente a un field en html
    fechaPublicacion = models.DateTimeField(auto_now_add=True) #Aca defino el atributo fechaPublicacion de tipo date equivalente a un date en html, establece automaticamente la fecha cuando se crea en base a la hora del servidor, no se cambia
    fechaInicio = models.DateTimeField(default=timezone.now) #Aca defino el atributo fechaInicio de tipo date equivalente a un date en html, timezone devuelve la fecha en base a la zona horaria de la persona que publico , se puede cambiar
    fechaFin = models.DateTimeField(blank=True, null=True) #Aca defino el atributo fechaFin de tipo date equivalente a un date en html
    activo = models.BooleanField(default=True)  #Aca defino el atributo activo de tipo char equivalente a un checkBox en html
    categorias = models.ManyToManyField(Categoria) #Aca defino el atributo categorias que es una relacion con categoria de muchos a muchos va en cualquiera de las dos, genera una nueva tabla en la base de datos
    publicadoPor = models.ForeignKey('usuario.Usuario',on_delete=models.CASCADE, related_name='anunciosPublicados') #Aca defino el atributo publicadoPor qeu es una relacion 1 a n esto va en el n de la relacion, el on delete me dice que se se borrar el usuario borro los anuncios es decir la n partes, el related es el nombre de la relacion asi usuario puede acceder atravez de este nombre al atributo
    ofertaGanadora = models.OneToOneField('OfertaAnuncio',on_delete=models.SET_NULL, related_name='ofertaGanadora', blank=True, null=True) #Aca defino el atributo oferta ganadora es una relacion 1 a 1, en donde ambos son igual de importantes, el delete set null me dice si elimino la oferta anuncio el campo oferta ganadora queda vacio

    class Meta:
        ordering = ('fechaInicio',) #controla los meta datos, en este caso el ordering me dice como se van ordernas los datos

    def __str__(self):
        return f'{self.titulo} - {'Activo' if self.activo else 'Inactivo'}' #Cuando tú (o Django) necesiten "convertir" una instancia de tu modelo (un objeto) en un simple texto, se llamará a este método.


class SeguimientoAnuncio(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE,related_name='seguimientos')
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='seguimientosUsuario')

    def __str__ (self):
        return f'Anuncio: {self.anuncio.titulo} - Usuiario:{self.usuario}'
    

class OfertaAnuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name='ofertas')
    fechaOferta = models.DateTimeField(auto_now_add=True)
    precioOferta = models.DecimalField(decimal_places=2, max_digits=10)
    esGanador = models.BooleanField(default=True)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='ofertas')