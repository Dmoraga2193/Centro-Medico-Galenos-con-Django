from django.urls import path
from .views import index,contact,about,registro, listar_pacientes, modificar_cita

urlpatterns = [
    path('', index, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('registro/',registro,name="registro"),
    path('listar-pacientes/',listar_pacientes,name="listar_pacientes"),
    path('modificar-cita/<id>/',modificar_cita,name="modificar_cita"),
]