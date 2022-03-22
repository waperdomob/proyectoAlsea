
from audioop import reverse
import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.middleware import *
from django.views.generic import CreateView
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from flask import request

from encuesta.forms import *
from encuesta.models import *
# Create your views here.

def index(request):
    #if request.user.is_authenticated:
            return render(request,'info.html')


    #else:    
        #response = redirect('/accounts/login')
        #return response
class crearEncuesta(CreateView):
    model = Encuestas
    form_class = EncuestaForm
    template_name = 'formEncuesta.html'
    initial = {'fecha': datetime.date.today() }
    

    def get_success_url(self):
        return reverse('encuesta:index')

