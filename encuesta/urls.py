from unicodedata import name
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path,include
from encuesta import views

urlpatterns = [
       
    path('inicio/',views.index, name='inicio'),
    path('encuesta/',views.crearEncuesta.as_view(), name='encuesta'),
    path('estadisticas/',views.estadisticas, name='estadisticas'),
    path('eliminarReporte/<int:pk>',views.eliminarReporte, name='eliminarReporte'),
    path('reportes/',views.reportListView.as_view(), name='reportes'),
    path('registrarEncuesta/', views.registrarEncuesta, name='registrarEncuesta'),    
    #path('success/', views.SuccessView.as_view(), name='success')
]