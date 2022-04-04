
from distutils.command.upload import upload
from pickle import TRUE
from re import A
from tkinter import CASCADE
from django.db import models
from django.db.models import Avg
from django.forms import CharField
from django.contrib.auth.models import User
from django.db.models.functions import Round

# Create your models here.
CALIFICACION = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

    )

class EncuestasManager(models.Manager):
        
    
            
    def get_by_all(self, ciudad,tienda,cargo,marca):
        return self.filter(ciudad_id=ciudad).filter(tienda__icontains=tienda).filter(cargo__icontains=cargo).filter(marca_id=marca)

    def get_by_three(self, ciudad,tienda,cargo):
        return self.filter(ciudad_id=ciudad).filter(tienda__icontains=tienda).filter(cargo__icontains=cargo)
    def get_by_three2(self, ciudad,tienda,marca):
        return self.filter(ciudad_id=ciudad).filter(tienda__icontains=tienda).filter(marca_id=marca)
    def get_by_three3(self,tienda,cargo,marca):
        return self.filter(marca_id=marca).filter(tienda__icontains=tienda).filter(cargo__icontains=cargo)
    def get_by_three4(self, ciudad,cargo,marca):
        return self.filter(ciudad_id=ciudad).filter(cargo__icontains=cargo).filter(marca_id=marca)

    def get_by_two(self, ciudad,tienda):
        return self.filter(ciudad_id=ciudad).filter(tienda__icontains=tienda)

    def get_by_two2(self, ciudad,cargo):
        return self.filter(ciudad_id=ciudad).filter(cargo__icontains=cargo)

    def get_by_two3(self, ciudad,marca):
        return self.filter(ciudad_id=ciudad).filter(marca_id=marca)

    def get_by_two4(self, tienda,cargo):
        return self.filter(tienda__icontains=tienda).filter(cargo__icontains=cargo)
    def get_by_two5(self, tienda,marca):
        return self.filter(tienda__icontains=tienda).filter(marca_id=marca)

    def get_by_two6(self, cargo,marca):
        return self.filter(cargo__icontains=cargo).filter(marca_id=marca)


    def get_by_marca(self, marca):
        return self.filter(marca_id=marca)

    def get_by_cargo(self, cargo):
        return self.filter(cargo__icontains=cargo)

    def get_by_tienda(self, tienda):
        return self.filter(tienda__icontains=tienda)

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


class Encuestas(models.Model):
    
    nombre = models.CharField(max_length=55)
    cargo= models.CharField(max_length=55)
    marca = models.ForeignKey(MarcasTiendas,null=False, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudades,null=False, on_delete=models.CASCADE)
    tienda = models.CharField(max_length=55)
    fecha = models.DateField()

    soporteRHC = models.IntegerField(choices=CALIFICACION,default='1',      blank=False, help_text='(Contratación)')
    amabilidadRHC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadRHC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteRHN = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Nomina)')
    amabilidadRHN = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadRHN = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteCC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Trasferencia de ordenes y servicio al usuario final)')
    amabilidadCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Trasferencia...)')
    efectividadCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteGA = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Arriendos y vigilancia)')
    amabilidadGA = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadGA = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteFC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Cuentas por pagar)')
    amabilidadFC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadFC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteFV = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Ventas POS y Cuentas por cobrar)')
    amabilidadFV = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadFV = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteFT = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Tesorería: Pago de cajas menores y recolección de dinero PROSEGUR)')
    amabilidadFT = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Tesorería: Pago de cajas menores y...)')
    efectividadFT = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Tesorería: Pago de cajas menores y...)')

    soporteSSCE = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Entrega de insumos por parte de proveedores; NO AXIONLOG)')
    amabilidadSSCE = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Entrega de insumos por parte de proveedores ...)')
    efectividadSSCE = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='(Entrega de insumos ...)')

    soporteSSCA = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(AXIONLOG)')
    amabilidadSSCA = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadSSCA = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteSSCC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Compras)')
    amabilidadSSCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadSSCC = models.IntegerField( choices=CALIFICACION, blank=True, default='1') 

    soporteMC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Comunicación de campañas...)')
    amabilidadMC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadMC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteHSEQ = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='')
    amabilidadHSEQ = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='')
    efectividadHSEQ = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='')

    soporteLEGAL = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='')
    amabilidadLEGAL = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='')
    efectividadLEGAL = models.IntegerField( choices=CALIFICACION, blank=True, default='1', help_text='')

    soporteTEC = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Sistema de venta POS...')
    amabilidadTEC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadTEC = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    soporteAUD = models.IntegerField( choices=CALIFICACION,      blank=True, default='1', help_text='(Mesa de ayuda)')
    amabilidadAUD = models.IntegerField( choices=CALIFICACION, blank=True, default='1')
    efectividadAUD = models.IntegerField( choices=CALIFICACION, blank=True, default='1')

    comentario = models.CharField(max_length=100)

    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    

    objects = models.Manager()
    encuestas_objects= EncuestasManager()

