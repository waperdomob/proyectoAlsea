
import datetime 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import redirect, render
from solicitudes.models import Documentos, Marca, Solicitudes

from solicitudes.forms import FormularioDocs, FormularioDocs2, FormularioSolicitud
from solicitudes.funcions.funcions import handle_uploaded_file,subirDocs


def index(request):    
    response = redirect('/accounts/login')
    return response

@login_required
def documentos(request):    
    return render(request,"documentos.html")

@login_required
def registrarS(request):
    
    miFormulario1=FormularioSolicitud()
    miFormulario2=FormularioDocs()
    form3=FormularioDocs2()
    return render(request,"registrarS.html",{"form1":miFormulario1,"form2":miFormulario2,'form3':form3})

@login_required
def consultarS(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"consultarS.html",{"fecha":fecha_actual})

@login_required
def registrarSolicitud(request):
    if request.method=="POST":
        miFormulario1 = FormularioSolicitud(request.POST)
        miFormulario2 = FormularioDocs(request.POST, request.FILES)
        miFormulario3 = FormularioDocs2(request.POST, request.FILES)
        
        if miFormulario1.is_valid():
            infForm = Solicitudes(
                rutNit = miFormulario1.cleaned_data['rutNit'],
                ticket = miFormulario1.cleaned_data['ticket'],
                nombre = miFormulario1.cleaned_data['nombre'],
                razonSocial = miFormulario1.cleaned_data['razonSocial'],
                numProveedor = miFormulario1.cleaned_data['numProveedor'],
                fecha = miFormulario1.cleaned_data['fecha'],
                vinculacion = miFormulario1.cleaned_data['vinculacion'],
                marca = Marca.objects.get(marca=miFormulario1.cleaned_data['marca'])
            
            )
            data = [
            subirDocs(request.FILES['inscripcion_actualizacion']),
            subirDocs(request.FILES['camaraComercio']),
            subirDocs(request.FILES['certificacionesBancarias']),
            subirDocs(request.FILES['Rut_Nit']),
            subirDocs(request.FILES['cedula']),
            subirDocs(request.FILES['cuestionario_LAFT']),
            subirDocs(request.FILES['consulta_listas']),
            subirDocs(request.FILES['compromiso_adhesion']),
            subirDocs(request.FILES['certificado_anticorr'])]
            
            infForm.save()
            for i in data:
                
                infForm2 = Documentos(
                    nombre = i[0],
                    doc_file = i[1],
                    solicitudes_rutNit = Solicitudes.objects.get(rutNit=miFormulario1.cleaned_data['rutNit'])
                )
                infForm2.save()
            
            return render(request,"solicitud.html",{"datos":infForm})
        else:
            
            miFormulario1 = FormularioSolicitud()
            miFormulario2 = FormularioDocs()
            miFormulario3 = FormularioDocs2()
            return render(request,"registrarS.html",{'form1':miFormulario1,'form2':miFormulario2,'form3':miFormulario3})

@login_required
def consultarSolicitud(request):
    if request.method=="POST":
        rut= request.POST["rutNit"]
        try:
            solicitud = Solicitudes.objects.get(rutNit=rut)
            Docs = Documentos.objects.filter(solicitudes_rutNit_id = rut)
            print (Docs)
            return render(request,"solicitud.html",{"datos":solicitud,"docs": Docs})
        except Solicitudes.DoesNotExist:
            return HttpResponseRedirect('/consultarS/')

  

