
import datetime
import os 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.middleware import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import default_storage, FileSystemStorage

from solicitudes.models import Documentos, Marca, Solicitudes

from solicitudes.forms import FormularioDocs, FormularioDocs2, FormularioSolicitud, FormularioUpdate
from solicitudes.funcions.funcions import handle_uploaded_file,subirDocs, subirDocs2

def handle_not_found(request,exception):
    return render(request,'not-found.html')

def index(request):   
    if request.user.is_authenticated:
        return render(request,"consultarS.html")
    else:    
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
        files = request.FILES.getlist('otrosDocs')
        
        if miFormulario1.is_valid():
            infForm = Solicitudes(
                rutNit = miFormulario1.cleaned_data['rutNit'],
                ticket = miFormulario1.cleaned_data['ticket'],
                nombre = miFormulario1.cleaned_data['nombre'],
                razonSocial = miFormulario1.cleaned_data['razonSocial'],
                numProveedor = miFormulario1.cleaned_data['numProveedor'],
                fecha = miFormulario1.cleaned_data['fecha'],
                vinculacion = miFormulario1.cleaned_data['vinculacion'],
                marca = Marca.objects.get(marca=miFormulario1.cleaned_data['marca']),
                user_id=request.session.get('_auth_user_id')
            
            )            
            data = [
            subirDocs(request.POST['nombre1'],request.FILES['inscripcion_actualizacion'],request.POST['rutNit']),
            subirDocs(request.POST['nombre2'],request.FILES['camaraComercio'],request.POST['rutNit']),
            subirDocs(request.POST['nombre3'],request.FILES['certificacionesBancarias'],request.POST['rutNit']),
            subirDocs(request.POST['nombre4'],request.FILES['Rut_Nit'],request.POST['rutNit']),
            subirDocs(request.POST['nombre5'],request.FILES['cedula'],request.POST['rutNit']),
            subirDocs(request.POST['nombre6'],request.FILES['cuestionario_LAFT'],request.POST['rutNit']),
            subirDocs(request.POST['nombre7'],request.FILES['consulta_listas'],request.POST['rutNit']),
            subirDocs(request.POST['nombre8'],request.FILES['compromiso_adhesion'],request.POST['rutNit']),
            subirDocs(request.POST['nombre9'],request.FILES['certificado_anticorr'],request.POST['rutNit'])]
            

            infForm.save()
            for i in data:                
                infForm2 = Documentos(
                    nombre = i[0],
                    doc_file = i[1],
                    solicitudes_rutNit = Solicitudes.objects.get(rutNit=miFormulario1.cleaned_data['rutNit'])
                )
                infForm2.save()

            if files:                    
                    for file in files:
                        obj = Documentos(
                            nombre = 'Documentos adicionales'+str(miFormulario1.cleaned_data['rutNit']),
                            doc_file = 'media/'+str(file),
                            solicitudes_rutNit = Solicitudes.objects.get(rutNit=miFormulario1.cleaned_data['rutNit'])
                        )
                        obj.save()
                       

            miFormulario1 = FormularioSolicitud()
            miFormulario2 = FormularioDocs()
            miFormulario3 = FormularioDocs2()
            messages.success(request, 'Tu Solicitud ha sido creada. Para verla y editarla dar click en el enlace Consultar Solicitudes')

            return render(request,"registrarS.html",{'form1':miFormulario1,'form2':miFormulario2,'form3':miFormulario3})
        else:
            messages.error(request, "Hubo un error al guardar la solicitud, intenta nuevamente")

            miFormulario1 = FormularioSolicitud()
            miFormulario2 = FormularioDocs()
            miFormulario3 = FormularioDocs2()
            return render(request,"registrarS.html",{'form1':miFormulario1,'form2':miFormulario2,'form3':miFormulario3})
    

@login_required
def consultarSolicitud(request):
    user_id=int(request.session.get('_auth_user_id'))
    
    if request.method=="POST":

        rut= request.POST["rutNit"]
        try:
            solicitud = get_object_or_404(Solicitudes, rutNit= rut)
            
            if user_id == solicitud.user_id:
                Docs = Documentos.objects.filter(solicitudes_rutNit_id = rut)
                return render(request,"solicitud.html",{"datos":solicitud,"docs": Docs})
            else:

                messages.error(request, "Hubo un error al consultar la solicitud: Solicitud no asociada al usuario")
                return render(request,'consultarS.html')
                

        except Solicitudes.DoesNotExist:

            return HttpResponseRedirect('/consultarS/')

@login_required
def editar(request):  
    user_id=int(request.session.get('_auth_user_id'))
    if request.method=="POST":
        solicitud_id= request.POST["rutNit"] 
        solicitud = Solicitudes.objects.get(rutNit=solicitud_id)  
        if user_id == solicitud.user_id:
                Docs = Documentos.objects.filter(solicitudes_rutNit_id = solicitud_id)
                miFormulario1 = FormularioUpdate(initial={'rutNit':solicitud.rutNit,'ticket':solicitud.ticket,'nombre':solicitud.nombre,'razonSocial':solicitud.razonSocial,'numProveedor':solicitud.numProveedor,'fecha':solicitud.fecha,'vinculacion':solicitud.vinculacion, 'marca':solicitud.marca})                
                
                return render(request,"editar.html",{"form1":miFormulario1,"form2":Docs})
        else:
            return HttpResponseRedirect('/consultarS/')  
                 

@login_required
def actualizar(request):

    user_id=int(request.session.get('_auth_user_id'))

    if request.method=="POST":
        solicitud_id= request.POST["rutNit"]
        solicitud = Solicitudes.objects.get(rutNit=solicitud_id)
        Docs = Documentos.objects.filter(solicitudes_rutNit_id = solicitud_id)
        idsDocs = []
        nombresDocs= []
        doc_file=[]
        for object in Docs:
            nombresDocs.append(object.nombre)
            idsDocs.append(object.id)
            doc_file.append("C:/Alsea/Alsea1"+str(object.doc_file))
        
        if user_id == solicitud.user_id:
            miFormulario1 = FormularioUpdate(request.POST or None)
            miFormulario2 =   request.FILES or None
            
            if miFormulario1.is_valid():
                infForm = Solicitudes(
                    rutNit = miFormulario1.cleaned_data['rutNit'],
                    ticket = miFormulario1.cleaned_data['ticket'],
                    nombre = miFormulario1.cleaned_data['nombre'],
                    razonSocial = miFormulario1.cleaned_data['razonSocial'],
                    numProveedor = miFormulario1.cleaned_data['numProveedor'],
                    fecha = miFormulario1.cleaned_data['fecha'],
                    vinculacion = miFormulario1.cleaned_data['vinculacion'],
                    marca = Marca.objects.get(marca=miFormulario1.cleaned_data['marca']),
                    user_id=request.session.get('_auth_user_id')            
                )
                
                if miFormulario2:
                    infForm.save()                     
                    for key in miFormulario2:
                        
                        for j in range(len(nombresDocs)):
                            
                            if nombresDocs[j] == key:
                                
                                ruta = doc_file[j]
                                print(ruta)
                                fs = FileSystemStorage()
                                default_storage.delete(ruta)
                                Documentos.objects.filter(nombre = nombresDocs[j]).delete()

                                data = [
                                subirDocs2(nombresDocs[j],request.FILES[nombresDocs[j]],request.POST['rutNit'])
                                ]
                                                       
                                for i in data:                
                                    infForm2 = Documentos(
                                    nombre = i[0],
                                    doc_file = i[1],
                                    solicitudes_rutNit = Solicitudes.objects.get(rutNit=miFormulario1.cleaned_data['rutNit'])
                                    )
                                    infForm2.save()
                else:
                    infForm.save()
                Docs = Documentos.objects.filter(solicitudes_rutNit_id = solicitud_id)
                return render(request,"solicitud.html",{"datos":infForm,"docs": Docs})
        else:
            
            messages.error(request, "Hubo un error al consultar la solicitud")
            return HttpResponseRedirect('/consultarS/')

