
import datetime 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
#from django.urls import reverse_lazy
#from django.contrib.auth.views import PasswordResetView
#from django.contrib.messages.views import SuccessMessageMixin

from solicitudes.models import Documentos, Marca, Solicitudes

from solicitudes.forms import FormularioDocs, FormularioDocs2, FormularioSolicitud
from solicitudes.funcions.funcions import handle_uploaded_file,subirDocs

""" lass ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')
 """
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
                marca = Marca.objects.get(marca=miFormulario1.cleaned_data['marca']),
                user_id=request.session.get('_auth_user_id')
            
            )
            data = [
            subirDocs(request.POST['nombre1'],request.FILES['inscripcion_actualizacion']),
            subirDocs(request.POST['nombre2'],request.FILES['camaraComercio']),
            subirDocs(request.POST['nombre3'],request.FILES['certificacionesBancarias']),
            subirDocs(request.POST['nombre4'],request.FILES['Rut_Nit']),
            subirDocs(request.POST['nombre5'],request.FILES['cedula']),
            subirDocs(request.POST['nombre6'],request.FILES['cuestionario_LAFT']),
            subirDocs(request.POST['nombre7'],request.FILES['consulta_listas']),
            subirDocs(request.POST['nombre8'],request.FILES['compromiso_adhesion']),
            subirDocs(request.POST['nombre9'],request.FILES['certificado_anticorr'])]
            

            infForm.save()
            for i in data:
                
                infForm2 = Documentos(
                    nombre = i[0],
                    doc_file = i[1],
                    solicitudes_rutNit = Solicitudes.objects.get(rutNit=miFormulario1.cleaned_data['rutNit'])
                )
                infForm2.save()
            
            return render(request,"consultarS.html")
        else:
            
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
                return HttpResponseRedirect('/consultarS/')

        except Solicitudes.DoesNotExist:
            return HttpResponseRedirect('/consultarS/')

@login_required
def editar(request):    
    if request.method=="POST":
        solicitud_id= request.POST["rutNit"] 
        solicitud = Solicitudes.objects.get(rutNit=solicitud_id)        
        miFormulario1 = FormularioSolicitud(initial={'rutNit':solicitud.rutNit,'ticket':solicitud.ticket,'nombre':solicitud.nombre,'razonSocial':solicitud.razonSocial,'numProveedor':solicitud.numProveedor,'fecha':solicitud.fecha,'vinculacion':solicitud.vinculacion, 'marca':solicitud.marca})
        return render(request,"editar.html",{"form1":miFormulario1})

@login_required
def actualizar(request):
    user_id=int(request.session.get('_auth_user_id'))

    if request.method=="POST":
        solicitud = Solicitudes.objects.get(rutNit=request.POST['rutNit']) 
        if user_id == solicitud.user_id:
            miFormulario1 = FormularioSolicitud(request.POST)
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
                infForm.save()
                Docs = Documentos.objects.filter(solicitudes_rutNit_id = request.POST['rutNit'])
                return render(request,"solicitud.html",{"datos":infForm,"docs": Docs})
        else:
                return HttpResponseRedirect('/consultarS/')
