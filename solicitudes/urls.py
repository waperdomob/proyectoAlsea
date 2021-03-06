from unicodedata import name
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path,include
from solicitudes import views 

urlpatterns = [
       
    path('',views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset_form.html')),
    path('registrarS/',views.registrarS, name='registrarS'),
    path('registrarSolicitud/',views.registrarSolicitud, name='registrarSolicitud'),
    path('proveedores/',login_required(views.Proveedores.as_view()), name='solicitudes'),
    path('detalleProveedor/<int:pk>',login_required(views.detalleProveedor.as_view()), name='detalleProveedor'),
    path('documentos/',views.documentos, name='documentos'),
    path('detalleProveedor/editar/<int:pk>',views.editar, name='editar'),
    path('actualizar/<int:pk>',views.actualizar, name='actualizar'),

]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
