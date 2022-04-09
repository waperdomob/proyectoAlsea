from dataclasses import field, fields
from django.utils.translation import gettext_lazy as _
from random import choices
from tkinter import HIDDEN
from xml.dom.minidom import Attr
from django import forms
import datetime

from .models import Encuestas, MarcasTiendas, Ciudades

CHART_CHOICES = (
    ('#1','Bar chart'),
    ('#2','Pie chart'),
    ('#3','Line chart'),

)
class MarcasForm(forms.ModelForm):
    class Meta:
        model= MarcasTiendas
        fields = ('marca',)

class CiudadesForm(forms.ModelForm):
    class Meta:
        model= Ciudades
        fields = ('ciudad',)


class EncuestaForm(forms.ModelForm):
    #required_css_class = 'textLabel'
    class Meta:
        model = Encuestas
        exclude = ['user']

        labels = {     
            'nombre':'Por favor ingrese su nombre completo',
            'cargo':'¿Qué cargo tiene en la compañía?',
            'marca':'¿A qué marca perteneces?',
            'ciudad':'¿En qué ciudad está hubicado?',
            'tienda':'Nombre de la tienda donde labora',
            'fecha':'Fecha  Actual',
            'soporteRHC':'Soporte del área de RECURSOS HUMANOS',
            'amabilidadRHC':'Amabilidad y cordialidad del área de RH',
            'efectividadRHC':'Efectividad de la solución brindada del área de RH',
            'soporteRHN':'Soporte del área de RECURSOS HUMANOS',
            'amabilidadRHN':'Amabilidad y cordialidad del área de RH',
            'efectividadRHN':'Efectividad de la solución brindada del área de RH', 
            'soporteCC':'Soporte del área de CONTACT CENTER ',
            'amabilidadCC':'Amabilidad y cordialidad del área de CONTACT CENTER',
            'efectividadCC':'Efectividad de la solución brindada del área de CONTACT CENTER', 
            'soporteGA':'Soporte del área de GERENCIA ADMINISTRATIVA',
            'amabilidadGA':'Amabilidad y cordialidad del área de GERENCIA ADMINISTRATIVA',
            'efectividadGA':'Efectividad de la solución brindada del área de GERENCIA ADMINISTRATIVA', 
            'soporteFC':'Soporte del área de FINANZAS',
            'amabilidadFC':'Amabilidad y cordialidad del área de FINANZAS',
            'efectividadFC':'Efectividad de la solución brindada del área de FINANZAS', 
            'soporteFV':'Soporte del área de FINANZAS',
            'amabilidadFV':'Amabilidad y cordialidad del área de FINANZAS',
            'efectividadFV':'Efectividad de la solución brindada del área de FINANZAS', 
            'soporteFT':'Soporte del área de FINANZAS',
            'amabilidadFT':'Amabilidad y cordialidad del área de FINANZAS ',
            'efectividadFT':'Efectividad de la solución brindada del área de FINANZAS',              
            'soporteSSCE':'Soporte del área de SAC SUPPLY CHAIN',
            'amabilidadSSCE':'Amabilidad y cordialidad del área de SAC SUPPLY CHAIN',
            'efectividadSSCE':'Efectividad de la solución brindada del área de SAC SUPPLY CHAIN',
            'soporteSSCA':'Soporte del área de SAC SUPPLY CHAIN',
            'amabilidadSSCA':'Amabilidad y cordialidad del área de SAC SUPPLY CHAIN',
            'efectividadSSCA':'Efectividad de la solución brindada del área de SSC',
            'soporteSSCC':'Soporte del área de SAC SUPPLY CHAIN',
            'amabilidadSSCC':'Amabilidad y cordialidad del área de SAC SUPPLY CHAIN',
            'efectividadSSCC':'Efectividad de la solución brindada del área de SSC',
            'soporteMC':'Soporte del área de MARKETING',
            'amabilidadMC':'Amabilidad y cordialidad del área de MARKETING',
            'efectividadMC':'Efectividad de la solución brindada del área de MARKETING', 
            'soporteHSEQ':'__________________  Soporte del área de HSEQ',
            'amabilidadHSEQ':'Amabilidad y cordialidad del área de HSEQ',
            'efectividadHSEQ':'Efectividad de la solución brindada del área de HSEQ',
            'soporteLEGAL':'__________________ Soporte del área LEGAL',
            'amabilidadLEGAL':'Amabilidad y cordialidad del área LEGAL',
            'efectividadLEGAL':'Efectividad de la solución brindada del área LEGAL',
            'soporteTEC':'Soporte del área TECNOLOGIA ',
            'amabilidadTEC':'Amabilidad y cordialidad del área TECNOLOGIA ',
            'efectividadTEC':'Efectividad de la solución brindada del área TECNOLOGIA',
            'soporteAUD':'Soporte del área AUDITORIA',
            'amabilidadAUD':'Amabilidad y cordialidad del área AUDITORIA ',
            'efectividadAUD':'Efectividad de la solución brindada del área AUDITORIA',
            'comentario':'¿tiene algun comentario, sugerencia o aporte para alguna de las areas de soporte?',
                
        }
        widgets = {
	        'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'}),
            'ciudad':forms.Select(attrs={'class':'form-control'}),
            'tienda':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'soporteRHC': forms.Select(attrs={'class':'form-control'}),
            'amabilidadRHC': forms.Select(attrs={'class':'form-control'}),
            'efectividadRHC': forms.Select(attrs={'class':'form-control'}),
            'soporteRHN': forms.Select(attrs={'class':'form-control'}),
            'amabilidadRHN': forms.Select(attrs={'class':'form-control'}),
            'efectividadRHN': forms.Select(attrs={'class':'form-control'}),
            'soporteCC': forms.Select(attrs={'class':'form-control'}),
            'amabilidadCC': forms.Select(attrs={'class':'form-control'}),
            'efectividadCC': forms.Select(attrs={'class':'form-control'}),
            'soporteGA': forms.Select(attrs={'class':'form-control'}),
            'amabilidadGA': forms.Select(attrs={'class':'form-control'}),
            'efectividadGA': forms.Select(attrs={'class':'form-control'}),
            'soporteFC': forms.Select(attrs={'class':'form-control'}),
            'amabilidadFC': forms.Select(attrs={'class':'form-control'}),
            'efectividadFC': forms.Select(attrs={'class':'form-control'}),
            'soporteFV': forms.Select(attrs={'class':'form-control'}),
            'amabilidadFV': forms.Select(attrs={'class':'form-control'}),
            'efectividadFV': forms.Select(attrs={'class':'form-control'}),
            'soporteFT': forms.Select(attrs={'class':'form-control'}),
            'amabilidadFT': forms.Select(attrs={'class':'form-control'}),
            'efectividadFT': forms.Select(attrs={'class':'form-control'}),
            'soporteSSCE': forms.Select(attrs={'class':'form-control'}),
            'amabilidadSSCE': forms.Select(attrs={'class':'form-control'}),
            'efectividadSSCE': forms.Select(attrs={'class':'form-control'}),
            'soporteSSCA': forms.Select(attrs={'class':'form-control'}),
            'amabilidadSSCA': forms.Select(attrs={'class':'form-control'}),
            'efectividadSSCA': forms.Select(attrs={'class':'form-control'}),
            'soporteSSCC': forms.Select(attrs={'class':'form-control'}),
            'amabilidadSSCC': forms.Select(attrs={'class':'form-control'}),
            'efectividadSSCC': forms.Select(attrs={'class':'form-control'}),
            'soporteMC': forms.Select(attrs={'class':'form-control'}),
            'amabilidadMC': forms.Select(attrs={'class':'form-control'}),
            'efectividadMC': forms.Select(attrs={'class':'form-control'}),
            'soporteHSEQ': forms.Select(attrs={'class':'form-control'}),
            'amabilidadHSEQ': forms.Select(attrs={'class':'form-control'}),
            'efectividadHSEQ': forms.Select(attrs={'class':'form-control'}),
            'soporteLEGAL': forms.Select(attrs={'class':'form-control'}),
            'amabilidadLEGAL': forms.Select(attrs={'class':'form-control'}),
            'efectividadLEGAL': forms.Select(attrs={'class':'form-control'}),
            'soporteTEC': forms.Select(attrs={'class':'form-control'}),
            'amabilidadTEC': forms.Select(attrs={'class':'form-control'}),
            'efectividadTEC': forms.Select(attrs={'class':'form-control'}),
            'soporteAUD': forms.Select(attrs={'class':'form-control'}),
            'amabilidadAUD': forms.Select(attrs={'class':'form-control'}),
            'efectividadAUD': forms.Select(attrs={'class':'form-control'}),
            'comentario': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class FiltrarResultados(forms.Form):
    required_css_class = 'textLabel'
    Grafica = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=CHART_CHOICES)