from tkinter import HIDDEN
from xml.dom.minidom import Attr
from django import forms
import datetime
GEEKS_CHOICES =(
    ("0","Elija una opción"),
    ("1", "Estrella Andina"),
    ("2", "Gastronomia italiana"),
    ("3", "Ambos"),
)
class FormularioSolicitud(forms.Form):
    required_css_class = 'textLabel'

    RutNit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Rut o Nit")
    ticket = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Número del Ticket")
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    razonSocial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Razón social")
    numProveedor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Número de proveedor")
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}),initial=datetime.date.today,disabled = True)
    vinculacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Vinculación o Actualización")
    marca = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=GEEKS_CHOICES)

    
class FormularioDocs(forms.Form):
    required_css_class = 'textLabel'
    
    inscripcion_actualizacion = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    camaraComercio = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificacionesBancarias = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    Rut_Nit = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    cedula = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    cuestionario_LAFT = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    consulta_listas = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    compromiso_adhesion = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    certificado_anticorr = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

class FormularioDocs2(forms.Form):
    required_css_class = 'textLabel'
    
    otrosDocs = forms.FileField(label="Agregue los otros documentos",widget=forms.FileInput(attrs={'class': 'form-control'}),disabled=True)
