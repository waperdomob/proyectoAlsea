from dataclasses import field
from random import choices
from tkinter import HIDDEN
from xml.dom.minidom import Attr
from django import forms
import datetime
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
class MarcasForm(forms.ModelForm):
    class Meta:
        model= Marca
        fields = ('marca',)

class SolicitudForm(forms.ModelForm):
    #required_css_class = 'textLabel'
    class Meta:
        model = Solicitudes
        exclude = ['user']
        labels = {     
            'rutNit':'Rut o Nit',
            'ticket':'Número del Ticket',
            'nombre':'Nombre',
            'razonSocial':'Razón social',
            'numProveedor':'Número de proveedor',
            'fecha':'Fecha  Actual',
            'vinculacion':'Vinculación o Actualización',
            'marca':'Marca',
            }
        widgets = {
	        'rutNit':forms.NumberInput(attrs={'class':'form-control'}),
	        'ticket':forms.NumberInput(attrs={'class':'form-control'}),
	        'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'razonSocial':forms.TextInput(attrs={'class':'form-control'}),
	        'numProveedor':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'vinculacion':forms.Select(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'}),
        }
        

 
class FormularioDocs(forms.Form):
    required_css_class = 'textLabel'
    
    nombre1=forms.CharField(initial="Formulario inscripcion_Actualizacion",widget=forms.HiddenInput())
    inscripcion_actualizacion = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    nombre2=forms.CharField(initial="Camara de comercio",widget=forms.HiddenInput())
    camaraComercio = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label="Camara de comercio")
    nombre3=forms.CharField(initial="Certificaciones bancarias",widget=forms.HiddenInput())
    certificacionesBancarias = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label="Certificaciones bancarias")
    nombre4=forms.CharField(initial="RutNit",widget=forms.HiddenInput())
    Rut_Nit = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    nombre5=forms.CharField(initial="Cedula",widget=forms.HiddenInput())
    cedula = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label="Cedula")
    nombre6=forms.CharField(initial="Cuestionario_LAFT",widget=forms.HiddenInput())
    cuestionario_LAFT = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}),label= "Cuestionario LA/FT")
    nombre7=forms.CharField(initial="Consulta listas vinculantes",widget=forms.HiddenInput())
    consulta_listas = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Consulta lista vinculantes")
    nombre8=forms.CharField(initial="Compromiso de adhesion",widget=forms.HiddenInput())
    compromiso_adhesion = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Compromiso de adhesion")
    nombre9=forms.CharField(initial="Certificado anticorrupcion",widget=forms.HiddenInput())
    certificado_anticorr = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Certificado anticorrupcion")

class FormularioDocs2(forms.Form):
    required_css_class = 'textLabel'
    
    otrosDocs = forms.FileField(label="Agregue los otros documentos",widget=forms.FileInput(attrs={'class': 'form-control','multiple': True}),disabled=True)

class FormularioUpdate(forms.Form):
    required_css_class = 'textLabel'
    rutNit = forms.CharField(widget=forms.HiddenInput())
    ticket = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Número del Ticket")
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    razonSocial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Razón social")
    numProveedor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Número de proveedor")
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}),initial=datetime.date.today,disabled = True)
    vinculacion = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),label="Vinculación o Actualización",choices=CHOICES2)
    marca = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=CHOICES)