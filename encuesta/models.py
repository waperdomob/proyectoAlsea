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
    
    nombre = models.CharField(max_length=55)
    cargo= models.CharField(max_length=55)
    marca = models.ForeignKey(MarcasTiendas,null=False, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudades,null=False, on_delete=models.CASCADE)
    tienda = models.CharField(max_length=55)
    fecha = models.DateField()

    soporteRHC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Contratación)')
    amabilidadRHC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadRHC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteRHN = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Nomina)')
    amabilidadRHN = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadRHN = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteCC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Trasferencia de ordenes y servicio al usuario final)')
    amabilidadCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='(Trasferencia...)')
    efectividadCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteGA = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Arriendos y vigilancia)')
    amabilidadGA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadGA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteFC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Cuentas por pagar)')
    amabilidadFC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadFC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteFV = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Ventas POS y Cuentas por cobrar)')
    amabilidadFV = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadFV = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteFT = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Tesorería: Pago de cajas menores y recolección de dinero PROSEGUR)')
    amabilidadFT = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='(Tesorería: Pago de cajas menores y...)')
    efectividadFT = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='(Tesorería: Pago de cajas menores y...)')

    soporteSSCE = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Entrega de insumos por parte de proveedores; NO AXIONLOG)')
    amabilidadSSCE = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='(Entrega de insumos por parte de proveedores ...)')
    efectividadSSCE = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='(Entrega de insumos ...)')

    soporteSSCA = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(AXIONLOG)')
    amabilidadSSCA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadSSCA = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteSSCC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Compras)')
    amabilidadSSCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadSSCC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1') 

    soporteMC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Comunicación de campañas...)')
    amabilidadMC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadMC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteHSEQ = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='')
    amabilidadHSEQ = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='')
    efectividadHSEQ = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='')

    soporteLEGAL = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='')
    amabilidadLEGAL = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='')
    efectividadLEGAL = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1', help_text='')

    soporteTEC = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Sistema de venta POS...')
    amabilidadTEC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadTEC = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    soporteAUD = models.CharField(max_length=1, choices=CALIFICACION,      blank=True, default='1', help_text='(Mesa de ayuda)')
    amabilidadAUD = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')
    efectividadAUD = models.CharField(max_length=1, choices=CALIFICACION, blank=True, default='1')

    comentario = models.CharField(max_length=100)

    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    