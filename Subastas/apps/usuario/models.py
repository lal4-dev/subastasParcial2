from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser): #Aca redefino el usuario  que esta basado en abstract User
    documentoIdentidad = models.CharField(max_length=15,unique=True,verbose_name='Numero de documento') # Aca defini el atributo documento con 15 letras de longitud y que es unico, el verbose es al pedo solo sirve en el admin de django
    domiciolio = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.username}'
    
    def obtenerNombreCompleto(self):
        if self.last_name and self.first_name:
            nombreCompleto = f'{self.last_name}, {self.first_name}'
            return nombreCompleto.strip()
        
    obtenerNombreCompleto.short_description = 'Nombre completo' #el short descripcion ta al pedo  solo sirve en el admin de django