
import datetime
from faulthandler import disable
import os
from django import forms 
from django.conf import settings
from django.views.generic import CreateView,ListView, FormView, DetailView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.middleware import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import default_storage, FileSystemStorage
from django.urls import reverse, reverse_lazy

from solicitudes.models import Documentos, Marca, Solicitudes

from solicitudes.forms import FormularioDocs, FormularioDocs2, FormularioUpdate,SolicitudForm
from solicitudes.funcions.funcions import subirDocs, subirDocs2

def handle_not_found(request,exception):
    return render(request,'not-found.html')

def index(request):   
    if request.user.is_authenticated:
        return redirect('registrarS')

    else:    
        response = redirect('/accounts/login')
        return response

class Proveedores(ListView):
    model = Solicitudes
    template_name = 'consultarS.html'

    def get_queryset(self):
        user_id=int(self.request.session.get('_auth_user_id'))
        return self.model.objects.filter(user_id=user_id)
    
    def get_context_data(self,*args, **kwargs):        
        context = {}
        context['datos'] = self.get_queryset()
        return context
 
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

class detalleProveedor(DetailView):

    model = Solicitudes
    template_name='solicitud.html'
    def get_queryset(self):
        qs = super(detalleProveedor, self).get_queryset()
        return qs.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        Docs = Documentos.objects.filter(solicitudes_rutNit_id = self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['docs'] = Docs
        return context

@login_required
def documentos(request):    
    return render(request,"documentos.html")

@login_required
def registrarS(request):
    miFormulario1=SolicitudForm(initial={'fecha':datetime.date.today})
    miFormulario2=FormularioDocs()
    form3=FormularioDocs2()
    return render(request,"registrarS.html",{"form1":miFormulario1,"form2":miFormulario2,'form3':form3})


@login_required
def registrarSolicitud(request):
    user_id=int(request.session.get('_auth_user_id'))
    if request.method=="POST":
        miFormulario1 = SolicitudForm(request.POST)
        miFormulario2 = FormularioDocs(request.POST, request.FILES)
        miFormulario3 = FormularioDocs2(request.POST, request.FILES)
        files = request.FILES.getlist('otrosDocs')
        if miFormulario1.is_valid():
            solicitud = miFormulario1.save(commit=False)
            solicitud.user_id = user_id
            solicitud.save()

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

            miFormulario1=SolicitudForm(initial={'fecha':datetime.date.today})
            miFormulario2 = FormularioDocs()
            miFormulario3 = FormularioDocs2()
            messages.success(request, 'Tu Solicitud ha sido creada. Para verla y editarla dar click en el enlace Consultar Solicitudes')

            return render(request,"registrarS.html",{'form1':miFormulario1,'form2':miFormulario2,'form3':miFormulario3})
        else:
            messages.error(request, "Hubo un error al guardar la solicitud, intenta nuevamente")

            miFormulario1=SolicitudForm(initial={'fecha':datetime.date.today})
            miFormulario2 = FormularioDocs()
            miFormulario3 = FormularioDocs2()
            return render(request,"registrarS.html",{'form1':miFormulario1,'form2':miFormulario2,'form3':miFormulario3})
    

@login_required
def consultarSolicitud(request, pk):
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
def editar(request,pk):  
    user_id=int(request.session.get('_auth_user_id'))
    if request.method=="POST":
        solicitud_id= pk 
        solicitud = Solicitudes.objects.filter(rutNit=solicitud_id).first()
        if user_id == solicitud.user_id:
                Docs = Documentos.objects.filter(solicitudes_rutNit_id = solicitud_id)                
                miFormulario1 = SolicitudForm(instance=solicitud)
                miFormulario1.fields["rutNit"].widget = forms.HiddenInput()
                return render(request,"editar.html",{"form1":miFormulario1,"form2":Docs,"pk":pk})
        else:
            return HttpResponseRedirect('/consultarS/')  
                 

@login_required
def actualizar(request,pk):

    user_id=int(request.session.get('_auth_user_id'))
    if request.method=="POST":
        solicitud = Solicitudes.objects.get(rutNit=pk)
        Docs = Documentos.objects.filter(solicitudes_rutNit_id = pk)
        idsDocs = []
        nombresDocs= []
        doc_file=[]
        for object in Docs:
            nombresDocs.append(object.nombre)
            idsDocs.append(object.id)
            doc_file.append("C:/Alsea/Alsea1"+str(object.doc_file))
        
        if user_id == solicitud.user_id:
            miFormulario1 = SolicitudForm(request.POST or None, instance=solicitud)
            miFormulario2 =   request.FILES or None

            if miFormulario1.is_valid():
                if miFormulario2:
                    miFormulario1.save() 
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
                    miFormulario1.save() 
                Docs = Documentos.objects.filter(solicitudes_rutNit_id = pk)
                solicitud = get_object_or_404(Solicitudes, rutNit= pk)
                return render(request,"solicitud.html",{"datos":solicitud,"docs": Docs, "pk":pk })
        else:
            
            messages.error(request, "Hubo un error al consultar la solicitud")
            return HttpResponseRedirect('/consultarS/')

