from distutils.command.upload import upload
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca,null=True, on_delete=models.CASCADE)
    

class Documentos(models.Model):
    
    nombre = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to='media/',default="")    
    solicitudes_rutNit = models.ForeignKey(Solicitudes,null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


    
