from dataclasses import field
from random import choices
from tkinter import HIDDEN
from xml.dom.minidom import Attr
from django import forms
import datetime

from matplotlib import widgets
from .models import Solicitudes, Documentos, Marca
CHOICES =(
    ("0","Elija una opción"),
    ("Estrella Andina", "Estrella Andina"),
    ("Gastronomia italiana", "Gastronomia italiana"),
    ("Ambas", "Ambas"),
)
CHOICES2 =(
    ("0","Elija una opción"),
    ("vinculacion", "Vinculación"),
    ("actualizacion", "Actualización"),
    
)

class FormularioSolicitud(forms.Form):
    required_css_class = 'textLabel'
    rutNit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Rut o Nit")
    ticket = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Número del Ticket")
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    razonSocial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Razón social")
    numProveedor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Número de proveedor")
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}),initial=datetime.date.today,disabled = True)
    vinculacion = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label="Vinculación o Actualización",choices=CHOICES2)
    marca = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=CHOICES)

 
class FormularioDocs(forms.Form):
    required_css_class = 'textLabel'
    
    inscripcion_actualizacion = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    camaraComercio = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label="Camara de comercio")
    certificacionesBancarias = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label="Certificaciones bancarias")
    Rut_Nit = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    cedula = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label="Cedula")
    cuestionario_LAFT = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label= "Cuestionario LA/FT")
    consulta_listas = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Consulta lista vinculantes")
    compromiso_adhesion = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Compromiso de adhesion")
    certificado_anticorr = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Certificado anticorrupcion")

class FormularioDocs2(forms.Form):
    required_css_class = 'textLabel'
    
    otrosDocs = forms.FileField(label="Agregue los otros documentos",widget=forms.FileInput(attrs={'class': 'form-control','multiple': True}),disabled=True)
