from dataclasses import field, fields
from django.utils.translation import gettext_lazy as _m
from random import choices
from tkinter import HIDDEN
from xml.dom.minidom import Attr
from django import forms
import datetime

from .models import Areas, Encuestas, MarcasTiendas, Ciudades, Cargos

CHART_CHOICES = (
    ('#1','Bar chart'),
    ('#2','Pie chart'),

)


class AreasForm(forms.ModelForm):
    class Meta:
        model= Areas
        fields = '__all__'
        labels = {
            'area':'¿En qué área se encuentra?',
        }
        
        widgets = {
            'area':forms.Select(attrs={'class':'form-control'}),
        }

class CargosForm(forms.ModelForm):
    class Meta:
        model= Cargos
        fields = ('cargo',)

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
            'ciudad':'¿En qué ciudad está ubicado?',
            'tienda':'Nombre de la tienda donde labora',
            'fecha':'Fecha  Actual',
            'soporteRHC':'RECURSOS HUMANOS Contratación.',
            'amabilidadRHC':'RECURSOS HUMANOS Contratación',
            'efectividadRHC':'RECURSOS HUMANOS Contratación',
            'soporteRHN':'RECURSOS HUMANOS Nómina.',
            'amabilidadRHN':'RECURSOS HUMANOS Nómina',
            'efectividadRHN':'RECURSOS HUMANOS Nómina', 
            'soporteCC':'CONTACT CENTER Trasferencia.',
            'amabilidadCC':'CONTACT CENTER Trasferencia',
            'efectividadCC':'CONTACT CENTER Trasferencia', 
            'soporteGA':'GERENCIA ADMINISTRATIVA.',
            'amabilidadGA':'GERENCIA ADMINISTRATIVA',
            'efectividadGA':'GERENCIA ADMINISTRATIVA', 
            'soporteFC':'FINANZAS Cuentas por pagar.',
            'amabilidadFC':'FINANZAS Cuentas por pagar',
            'efectividadFC':'FINANZAS Cuentas por pagar', 
            'soporteFV':'FINANZAS Ventas POS.',
            'amabilidadFV':'FINANZAS Ventas POS',
            'efectividadFV':'FINANZAS Ventas POS', 
            'soporteFT':'FINANZAS Tesorería.',
            'amabilidadFT':'FINANZAS Tesorería',
            'efectividadFT':'FINANZAS Tesorería',              
            'soporteSSCE':'SAC SUPPLY CHAIN Entrega de insumos.',
            'amabilidadSSCE':'SAC SUPPLY CHAIN Entrega de insumos',
            'efectividadSSCE':'SAC SUPPLY CHAIN Entrega de insumos',
            'soporteSSCA':'SAC SUPPLY CHAIN AXIONLOG.',
            'amabilidadSSCA':'SAC SUPPLY CHAIN AXIONLOG',
            'efectividadSSCA':'SAC SUPPLY CHAIN AXIONLOG',
            'soporteSSCC':'SAC SUPPLY CHAIN Compras.',
            'amabilidadSSCC':'SAC SUPPLY CHAIN Compras',
            'efectividadSSCC':'SAC SUPPLY CHAIN Compras',
            'soporteMC':'MARKETING Comunicación.',
            'amabilidadMC':'MARKETING Comunicación ',
            'efectividadMC':'MARKETING Comunicación ', 
            'soporteHSEQ':'HSEQ.',
            'amabilidadHSEQ':'HSEQ',
            'efectividadHSEQ':'HSEQ',
            'soporteLEGAL':'LEGAL.',
            'amabilidadLEGAL':'LEGAL',
            'efectividadLEGAL':'LEGAL',
            'soporteTEC':'TECNOLOGIA Sistema de venta.',
            'amabilidadTEC':' TECNOLOGIA Sistema de venta',
            'efectividadTEC':' TECNOLOGIA Sistema de venta',
            'soporteAUD':'AUDITORIA Mesa de ayuda.',
            'amabilidadAUD':'AUDITORIA Mesa de ayuda ',
            'efectividadAUD':'AUDITORIA Mesa de ayuda',
            'comentario':'¿Comentario, sugerencia o aporte para alguna de las areas de soporte?',
                
        }
        widgets = {
	        'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.Select(attrs={'class':'form-control select2'}),            
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