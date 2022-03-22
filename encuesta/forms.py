from dataclasses import field, fields
from django.utils.translation import gettext_lazy as _
from random import choices
from tkinter import HIDDEN
from xml.dom.minidom import Attr
from django import forms
import datetime

from .models import Encuestas, MarcasTiendas, Ciudades

class MarcasForm(forms.ModelForm):
    class Meta:
        model: MarcasTiendas
        fields = ('marca',)

class CiudadesForm(forms.ModelForm):
    class Meta:
        model: Ciudades
        fields = ('ciudad',)

class EncuestaForm(forms.ModelForm):
    #required_css_class = 'textLabel'
    class Meta:
        model = Encuestas
        exclude = ['id']

        labels = {     
            'nombre':'Por favor ingrese su nombre completo',
            'cargo':'¿Qué cargo tiene en la compañía?',
            'marca':'¿A qué marca perteneces?',
            'ciudad':'¿En qué ciudad está hubicado?',
            'tienda':'Nombre de la tienda donde labora',
            'fecha':'Fecha Actual',
            'soporteRHC':'Soporte del área de RECURSOS HUMANOS (Contratación)',
            'amabilidadRHC':'Amabilidad y cordialidad del área de RECURSOS HUMANOS (Contratación)',
            'efectividadRHC':'Efectividad de la solución brindada del área de RECURSOS HUMANOS (Contratación).',
            'soporteRHN':'Soporte del área de RECURSOS HUMANOS (Nomina).',
            'amabilidadRHN':'Amabilidad y cordialidad del área de RECURSOS HUMANOS (Nomina). ',
            'efectividadRHN':'Efectividad de la solución brindada del área de RECURSOS HUMANOS (Nomina). ', 
            'soporteCC':'Soporte del área de CONTACT CENTER (Trasferencia de ordenes y servicio al usuario final)',
            'amabilidadCC':'Amabilidad y cordialidad del área de CONTACT CENTER (Trasferencia de ordenes y servicio al usuario final)',
            'efectividadCC':'Efectividad de la solución brindada del área de CONTACT CENTER (Trasferencia de ordenes y servicio al usuario final)', 
            'soporteGA':'Soporte del área de GERENCIA ADMINISTRATIVA (Arriendos y vigilancia)',
            'amabilidadGA':'Amabilidad y cordialidad del área de GERENCIA ADMINISTRATIVA (Arriendos y vigilancia)',
            'efectividadGA':'Efectividad de la solución brindada del área de GERENCIA ADMINISTRATIVA (Arriendos y vigilancia)', 
            'soporteFC':'Soporte del área de FINANZAS (Cuentas por pagar)',
            'amabilidadFC':'Amabilidad y cordialidad del área de FINANZAS (Cuentas por pagar)',
            'efectividadFC':'Efectividad de la solución brindada del área de FINANZAS (Cuentas por pagar)', 
            'soporteFV':'Soporte del área de FINANZAS (Ventas POS y Cuentas por cobrar)',
            'amabilidadFV':'Amabilidad y cordialidad del área de FINANZAS (Ventas POS y Cuentas por cobrar)',
            'efectividadFV':'Efectividad de la solución brindada del área de FINANZAS (Ventas POS y Cuentas por cobrar)', 
            'soporteFT':'Soporte del área de FINANZAS (Tesorería: Pago de cajas menores y recolección de dinero PROSEGUR)',
            'amabilidadFT':'Amabilidad y cordialidad del área de FINANZAS (Tesorería: Pago de cajas menores y recolección de dinero PROSEGUR)',
            'efectividadFT':'Efectividad de la solución brindada del área de FINANZAS (Tesorería: Pago de cajas menores y recolección de dinero PROSEGUR)',              
            'soporteSSCE':'Soporte del área de SAC SUPPLY CHAIN (Entrega de insumos por parte de proveedores; NO AXIONLOG)',
            'amabilidadSSCE':'Amabilidad y cordialidad del área de SAC SUPPLY CHAIN (Entrega de insumos por parte de proveedores; NO AXIONLOG)',
            'efectividadSSCE':'Efectividad de la solución brindada del área de SAC SUPPLY CHAIN (Entrega de insumos por parte de proveedores; NO AXIONLOG)',
            'soporteSSCA':'Soporte del área de SAC SUPPLY CHAIN (AXIONLOG)',
            'amabilidadSSCA':'Amabilidad y cordialidad del área de SAC SUPPLY CHAIN (AXIONLOG)',
            'efectividadSSCA':'Efectividad de la solución brindada del área de SAC SUPPLY CHAIN (AXIONLOG)',
            'soporteSSCC':'Soporte del área de SAC SUPPLY CHAIN (Compras)',
            'amabilidadSSCC':'Amabilidad y cordialidad del área de SAC SUPPLY CHAIN (Compras)',
            'efectividadSSCC':'Efectividad de la solución brindada del área de SAC SUPPLY CHAIN (Compras)',
            'soporteMC':'Soporte del área de MARKETING (Comunicación de campañas, entrega instructivos, materiales e informes).',
            'amabilidadMC':'Amabilidad y cordialidad del área de MARKETING (Comunicación de campañas, entrega instructivos, materiales e informes)',
            'efectividadMC':'Efectividad de la solución brindada del área de MARKETING (Comunicación de campañas, entrega instructivos, materiales e informes)', 
            'soporteHSEQ':'Soporte del área de HSEQ',
            'amabilidadHSEQ':'Amabilidad y cordialidad del área de HSEQ',
            'efectividadHSEQ':'Efectividad de la solución brindada del área de HSEQ',
            'soporteLEGAL':'Soporte del área LEGAL',
            'amabilidadLEGAL':'Amabilidad y cordialidad del área LEGAL',
            'efectividadLEGAL':'Efectividad de la solución brindada del área LEGAL',
            'soporteTEC':'Soporte del área TECNOLOGIA (Sistema de venta POS, internet y telefonia, aplicaciones CORE. ej:Humanet )',
            'amabilidadTEC':'Amabilidad y cordialidad del área TECNOLOGIA (Sistema de venta POS, internet y telefonia, aplicaciones CORE. ej:Humanet )',
            'efectividadTEC':'Efectividad de la solución brindada del área TECNOLOGIA (Sistema de venta POS, internet y telefonia, aplicaciones CORE. ej:Humanet )',
            'soporteAUD':'Soporte del área AUDITORIA (Mesa de ayuda)',
            'amabilidadAUD':'Amabilidad y cordialidad del área AUDITORIA (Mesa de ayuda)',
            'efectividadAUD':'Efectividad de la solución brindada del área AUDITORIA (Mesa de ayuda)',
            'comentario':'¿tiene algun comentario, sugerencia o aporte para alguna de las areas de soporte?',
                
        }
        widgets = {
	        'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'tienda':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.TextInput(attrs={'class':'form-control'}),
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