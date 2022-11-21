from django.contrib import admin
from .models import Prevision_Salud,Paciente,Medico, Contacto, Cita

# Register your models here.

class DetalleMedico(admin.ModelAdmin):
    list_display= ["nombre","especialidad"]
    search_fields= ["nombre"]
    list_per_page= 10

class DetallePaciente(admin.ModelAdmin):
    list_display= ["nombre","prevision_salud"]
    search_fields= ["nombre"]
    list_filter= ["prevision_salud"]
    list_per_page= 10

class DetalleContactos(admin.ModelAdmin):
    list_display= ["nombre","tipo_consulta"]
    list_per_page=10

class DetalleCita(admin.ModelAdmin):
    list_display= ["nombre","fecha_consulta"]
    search_fields= ["fecha_consulta"]
    list_per_page=10


admin.site.register(Prevision_Salud)
admin.site.register(Paciente,DetallePaciente)
admin.site.register(Medico,DetalleMedico)
admin.site.register(Contacto,DetalleContactos)
admin.site.register(Cita,DetalleCita)

