from distutils.command.upload import upload
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.
CALIFICACION = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

    )
class MarcasTiendas(models.Model):
    marca = models.CharField(max_length=45)

    def __str__(self):
        return self.marca
class Ciudades(models.Model):
    ciudad = models.CharField(max_length=45)

    def __str__(self):
        return self.ciudad

class Encuestas(models.Model):
    nombre = models.CharField(max_length=45)
    cargo= models.CharField(max_length=45)
    marca = models.ForeignKey(MarcasTiendas,null=False, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudades,null=False, on_delete=models.CASCADE)
    tienda = models.CharField(max_length=45, primary_key=CharField)
    fecha = models.DateField()

    soporteRHC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente:')

    amabilidadRHC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente:')

    efectividadRHC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente:')

    soporteRHN = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadRHN = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadRHN = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteCC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')
    
    soporteGA = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadGA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadGA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteFC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadFC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadFC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteFV = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadFV = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadFV = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteFT = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadFT = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadFT = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteSSCE = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadSSCE = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadSSCE = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteSSCA = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadSSCA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadSSCA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteSSCC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadSSCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadSSCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteMC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadMC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadMC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteHSEQ = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadHSEQ = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadHSEQ = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteLEGAL = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadLEGAL = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadLEGAL = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteTEC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    amabilidadTEC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    efectividadTEC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente')

    soporteAUD = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente:')

    amabilidadAUD = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente:')

    efectividadAUD = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='Califica de 1 a 5, siendo 1 insuficiente y 5 sobresaliente:')

    comentario = models.CharField(max_length=100)

    

    