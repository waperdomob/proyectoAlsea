from distutils.command.upload import upload
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.

class Marca(models.Model):
    marca = models.CharField(max_length=45)

    def __str__(self):
        return self.marca

class Solicitudes(models.Model):
    rutNit = models.CharField(max_length=45, primary_key=CharField)
    ticket= models.IntegerField()
    nombre = models.CharField(max_length=45)
    razonSocial = models.CharField(max_length=45)
    numProveedor = models.CharField(max_length=45)
    fecha = models.DateField()
    vinculacion = models.CharField(max_length=45)
    marca_id = models.ForeignKey(Marca,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.rutNit

class Documentos(models.Model):
    
    upload = models.FileField(upload_to='file/%Y/%m/%d/')
    nombre = models.CharField(max_length=45)
    solicitudes_rutNit = models.ForeignKey(Solicitudes,null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


    
