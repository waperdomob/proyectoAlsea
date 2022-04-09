from django.contrib import admin
from solicitudes.models import Marca,Documentos,Solicitudes
from encuesta.models import MarcasTiendas, Ciudades, Encuestas
from reporte.models import Reporte


class solicitudesAdmin(admin.ModelAdmin):
    list_display=("rutNit","ticket","nombre")

class documentosAdmin(admin.ModelAdmin):
    list_display=("nombre","doc_file","solicitudes_rutNit_id")

class marcaAdmin(admin.ModelAdmin):
    list_display=("marca",)

class marcaTiendaAdmin(admin.ModelAdmin):
    list_display=("marca",)

class CiudadesAdmin(admin.ModelAdmin):
    list_display=("ciudad",)

class EncuestasAdmin(admin.ModelAdmin):
    list_display=("id","nombre","cargo","tienda","user_id")

class ReportesAdmin(admin.ModelAdmin):
    list_display=("id","nombre","documento","user_id")

admin.site.register(Solicitudes,solicitudesAdmin)
admin.site.register(Marca,marcaAdmin)
admin.site.register(Documentos,documentosAdmin)
admin.site.register(Encuestas,EncuestasAdmin)
admin.site.register(MarcasTiendas,marcaTiendaAdmin)
admin.site.register(Ciudades,CiudadesAdmin)
admin.site.register(Reporte,ReportesAdmin)
