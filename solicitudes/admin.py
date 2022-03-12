from django.contrib import admin
from solicitudes.models import Marca,Documentos,Solicitudes


class solicitudesAdmin(admin.ModelAdmin):
    list_display=("rutNit","ticket","nombre")

class documentosAdmin(admin.ModelAdmin):
    list_display=("nombre","doc_file")

class marcaAdmin(admin.ModelAdmin):
    list_display=("marca",)

admin.site.register(Solicitudes,solicitudesAdmin)
admin.site.register(Marca,marcaAdmin)
admin.site.register(Documentos,documentosAdmin)