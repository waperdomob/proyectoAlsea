
import datetime
from django.conf import settings
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.pyplot import get

from solicitudes.forms import FormularioDocs, FormularioDocs2, FormularioSolicitud
from solicitudes.funcions.funcions import handle_uploaded_file


def index(request):
    return render(request,"index.html")

def registrarS(request):
    miFormulario1=FormularioSolicitud()
    miFormulario2=FormularioDocs()
    form3=FormularioDocs2()
    return render(request,"registrarS.html",{"form1":miFormulario1,"form2":miFormulario2,'form3':form3})

def consultarS(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"consultarS.html",{"fecha":fecha_actual})

def login(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"login.html",{"fecha":fecha_actual})

def registrarSolicitud(request):

    if request.method=="POST":
        miFormulario1 = FormularioSolicitud(request.POST)
        miFormulario2 = FormularioDocs(request.POST, request.FILES)
        miFormulario3 = FormularioDocs2(request.POST, request.FILES)
        
        if miFormulario1.is_valid():
            infForm= miFormulario1.cleaned_data
            handle_uploaded_file(request.FILES['inscripcion_actualizacion'])
            handle_uploaded_file(request.FILES['camaraComercio'])
            handle_uploaded_file(request.FILES['certificacionesBancarias'])
            handle_uploaded_file(request.FILES['Rut_Nit'])
            handle_uploaded_file(request.FILES['cedula'])
            handle_uploaded_file(request.FILES['cuestionario_LAFT'])
            handle_uploaded_file(request.FILES['consulta_listas'])
            handle_uploaded_file(request.FILES['compromiso_adhesion'])
            handle_uploaded_file(request.FILES['certificado_anticorr'])

            return render(request,"solicitud.html",{"datos":infForm})
        else:
            
            miFormulario1 = FormularioSolicitud()
            miFormulario2 = FormularioDocs()
            miFormulario3 = FormularioDocs2()
            return render(request,"registrarS.html",{'form1':miFormulario1,'form2':miFormulario2,'form3':miFormulario3})

def consultarSolicitud(request):
    if request.method=="POST":
        rutNit= request.POST["rutNit"]

        return render(request,"solicitud.html",{"rutNit":rutNit})
    
    return render(request,"registrar.html")


