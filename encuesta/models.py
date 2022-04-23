
from distutils.command.upload import upload
from pickle import TRUE
from re import A
from tkinter import CASCADE
from django.db import models
from django.forms import CharField, DateField
from django.contrib.auth.models import User

# Create your models here.
CALIFICACION = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),

    )
Area_choices = (
    ('2','Customer Service'),
    ('1','Centro de soporte'),

)
class EncuestasManager(models.Manager):
        
    
            
    def get_by_all(self, ciudad,tienda,cargo,marca):
        return self.filter(ciudad_id=ciudad).filter(tienda=tienda).filter(cargo_id=cargo).filter(marca_id=marca)

    def get_by_three(self, ciudad,tienda,cargo):
        return self.filter(ciudad_id=ciudad).filter(tienda=tienda).filter(cargo_id=cargo)
    def get_by_three2(self, ciudad,tienda,marca):
        return self.filter(ciudad_id=ciudad).filter(tienda=tienda).filter(marca_id=marca)
    def get_by_three3(self,tienda,cargo,marca):
        return self.filter(marca_id=marca).filter(tienda=tienda).filter(cargo_id=cargo)
    def get_by_three4(self, ciudad,cargo,marca):
        return self.filter(ciudad_id=ciudad).filter(cargo_id=cargo).filter(marca_id=marca)

    def get_by_two(self, ciudad,tienda):
        return self.filter(ciudad_id=ciudad).filter(tienda=tienda)

    def get_by_two2(self, ciudad,cargo):
        return self.filter(ciudad_id=ciudad).filter(cargo_id=cargo)

    def get_by_two3(self, ciudad,marca):
        return self.filter(ciudad_id=ciudad).filter(marca_id=marca)

    def get_by_two4(self, tienda,cargo):
        return self.filter(tienda=tienda).filter(cargo_id=cargo)
    def get_by_two5(self, tienda,marca):
        return self.filter(tienda=tienda).filter(marca_id=marca)

    def get_by_two6(self, cargo,marca):
        return self.filter(cargo_id=cargo).filter(marca_id=marca)


    def get_by_marca(self, marca):
        return self.filter(marca_id=marca)

    def get_by_cargo(self, cargo):
        return self.filter(cargo_id=cargo)

    def get_by_tienda(self, tienda):
        return self.filter(tienda=tienda)

    def get_by_ciudad(self, ciudad): 
        return self.filter(ciudad_id=ciudad)

class MarcasTiendas(models.Model):
    marca = models.CharField(max_length=45)

    def __str__(self):
        return self.marca
class Ciudades(models.Model):
    ciudad = models.CharField(max_length=45)

    def __str__(self):
        return self.ciudad

class Areas(models.Model):
    area = models.CharField(max_length=45, choices=Area_choices)

    def __str__(self):
        return self.area

class Cargos(models.Model):
    cargo = models.CharField(max_length=45)
    area = models.ForeignKey(Areas,null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.cargo


class Encuestas(models.Model):
    
    nombre = models.CharField(max_length=55)
    cargo= models.ForeignKey(Cargos,null=False, on_delete=models.CASCADE)
    marca = models.ForeignKey(MarcasTiendas,null=False, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudades,null=False, on_delete=models.CASCADE)
    tienda = models.CharField(max_length=55)
    fecha = models.DateField(auto_now_add=True)
    soporteRHC = models.IntegerField(choices=CALIFICACION,default='1',blank=False, help_text='(Soporte)')
    amabilidadRHC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadRHC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteRHN = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadRHN = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadRHN = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteCC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1',help_text='(Efectividad)')

    soporteGA = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadGA = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadGA = models.IntegerField( choices=CALIFICACION, blank=True, default='1',help_text='(Efectividad)')

    soporteFC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadFC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadFC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteFV = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadFV = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadFV = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteFT = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadFT = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadFT = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteSSCE = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadSSCE = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadSSCE = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteSSCA = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadSSCA = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadSSCA = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteSSCC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadSSCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadSSCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)') 

    soporteMC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadMC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadMC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteHSEQ = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadHSEQ = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadHSEQ = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteLEGAL = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadLEGAL = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadLEGAL = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteTEC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadTEC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadTEC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    soporteAUD = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Soporte)')
    amabilidadAUD = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Amabilidad)')
    efectividadAUD = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Efectividad)')

    comentario = models.CharField(max_length=100)

    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    

    objects = models.Manager()
    encuestas_objects= EncuestasManager()

