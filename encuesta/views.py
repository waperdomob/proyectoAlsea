
from django.urls import reverse
import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.middleware import *
from django.views.generic import CreateView
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render


from encuesta.forms import *
from encuesta.models import *
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