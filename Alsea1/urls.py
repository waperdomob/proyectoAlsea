"""Alsea1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from solicitudes import views 

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('',views.index, name='index'),
    #path('password-reset/', ResetPasswordView.as_view(),name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registrarS/',views.registrarS, name='registrarS'),
    path('registrarSolicitud/',views.registrarSolicitud, name='registrarSolicitud'),
    path('consultarS/',views.consultarS, name='consultarS'),
    path('consultarSolicitud/',views.consultarSolicitud, name='consultarSolicitud'),
    path('documentos/',views.documentos, name='documentos'),
    path('editar/',views.editar, name='editar'),
    path('actualizar/',views.actualizar, name='actualizar'),



    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

