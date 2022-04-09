from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Reporte(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.FileField(upload_to='reports',default="")  
    comentario = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre