
from turtle import color
from django.urls import reverse
import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.middleware import *
from django.views.generic import CreateView
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pymysql import NULL
from encuesta.utils import get_ciudad_from_id,get_marca_from_id, get_chart,get_graph
from encuesta.funcions.funcions import filtrar,pasar_dicc
from encuesta.forms import *
from encuesta.models import Encuestas, Ciudades, MarcasTiendas
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin.html')
        else:
            return render(request,'info.html')
    else:    
        response = redirect('../../accounts/login')
        return response


class crearEncuesta(CreateView):
    model = Encuestas
    form_class = EncuestaForm
    template_name = 'formEncuesta.html'
    initial = {'fecha': datetime.date.today() }
    
    def get_success_url(self):
        return reverse('encuesta:inicio')


@login_required
def registrarEncuesta(request):
    user_id=int(request.session.get('_auth_user_id'))
    if request.method=="POST":
        miEncuesta = EncuestaForm(request.POST)
        if miEncuesta.is_valid():
            encuesta = miEncuesta.save(commit=False)
            encuesta.user_id = user_id
            miEncuesta.save()
            messages.success(request, 'Tu Respuesta fue enviada')
            return render(request, 'info.html')
        else:
            messages.error(request, 'Algo ocurrió, vuelve a intentarlo!!')
            return render(request, 'info.html')

@login_required
def estadisticas(request):
    user_id=int(request.session.get('_auth_user_id'))
    titulos=['RH_Contratación','RH_Nomina','Contac_center','Gerencia_Administrativa','Finanzas_Cpp','Finanzas_Vposs','Finanzas_tes' ,'Sac_supli_chain','Sac_supli_chain_AX','Sac_supli_chain_CP','Marketing','Hseq','Legal','Tecnologia','Auditoria']  
    form = FiltrarResultados()
    locales = Encuestas.objects.only('tienda').distinct('tienda')
    cargos = Encuestas.objects.only('cargo').distinct('cargo')
    ciudades= Ciudades.objects.all()
    tiendas = MarcasTiendas.objects.all()
    df1 = None
    df2 = [None]*14
    prom = [None]*14
    chart= [None]*14
    enc_sep=[]
    encuestas=None
    if request.user.is_superuser:
        if request.method=="POST":

            chart_type = request.POST.get('Grafica')
            if request.POST['ciudad'] or request.POST['tienda'] or request.POST['cargo'] or request.POST['marca']:
                filtros = {
                    'ciudad':request.POST['ciudad'],
                    'tienda':request.POST['tienda'],
                    'cargo':request.POST['cargo'],
                    'marca': request.POST['marca']
                }
                print(filtros)            
                encuestas = filtrar(filtros)
                
            else:
                encuestas = Encuestas.objects.all()      
            
            #encuestas = filtrar(filtros)        
            
            if len(encuestas)>0:
                obj= pasar_dicc(encuestas)
                df1 = pd.DataFrame(encuestas.values())  
                df1['marca_id'] = df1['marca_id'].apply(get_marca_from_id)
                df1['ciudad_id'] = df1['ciudad_id'].apply(get_ciudad_from_id)
                df1.rename({'marca_id':'marca','ciudad_id':'ciudad'},axis=1, inplace=True)

                for i in range(len(obj)):
                    enc_sep.append(None)
                    enc_sep[i]= pd.DataFrame(obj[i])
                    prom[i] = enc_sep[i].mean()
                    chart[i] = get_chart(chart_type, prom[i],titulos[i])
                    

                for i in range(len(obj)):
                    #print(enc_sep[i])
                    print(prom[i])
                    df2[i] = enc_sep[i].style.set_table_attributes('class="table-wrapper-scroll-y mi-table", id= "dtVerticalScrollExample"').set_caption(titulos[i]).render()
                
                df1 = df1.to_html()

                
            else:
                print("no data")
                
        context = {
            'datos':df1,
            'datos2':df2,
            'prom':prom,
            'encuestas': encuestas,
            'locales': locales,
            'cargos':cargos,
            'ciudades':ciudades,
            'tiendas':tiendas,
            'form':form,
            'chart':chart,
            }
        return render(request,'modEstadisticas.html', context)
    else:
        return render(request, 'info.html')
