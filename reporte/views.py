from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files import File
from .utils import get_report_image

from .models import Reporte
from .forms import ReporteForm
import cv2
import os
import img2pdf
from os import remove

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def create_report(request):
    form = ReporteForm(request.POST or None)
    imgs = [None]*15
    imagenes= [None]*15
    if is_ajax(request=request):
        user_id = int(request.session.get('_auth_user_id'))
        nombre = request.POST.get('name')
        comentario = request.POST.get('remark')

        for i in range(len(imgs)):
            imagenes[i] = request.POST.get('imagen'+str(i))
        for i in range(len(imgs)):
            get_report_image(imagenes[i],i)
            imgs[i] =cv2.imread("imagen"+str(i)+".png")

        imagenes_png = [archivo for archivo in os.listdir('C:/Alsea/Alsea1') if archivo.endswith(".png")]
        with open("Estadisticas"+str(nombre)+".pdf", "wb") as document:
            document.write(img2pdf.convert(imagenes_png))

        for i in range(len(imagenes)):                
            remove("imagen"+str(i)+".png")
        
        documentoPDF =  File(open("Estadisticas"+str(nombre)+".pdf", 'rb'))

        Reporte.objects.create(nombre=nombre, comentario=comentario, user_id=user_id, documento=documentoPDF)
        documentoPDF.close()

        remove("C:\Alsea\Alsea1\Estadisticas"+str(nombre)+".pdf")
        
        return JsonResponse({'msg':'send'})
    return JsonResponse({})
    