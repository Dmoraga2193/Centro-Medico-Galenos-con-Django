from django.db import models

# Create your models here.
class Prevision_Salud(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    prevision_salud = models.ForeignKey(Prevision_Salud, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    especialidad = models.TextField()

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

opciones_previsiones = [
    [0, "Fonasa"],
    [1, "Isapre"]
]

opciones_areas_medicas = [
    [0, "Cardeologia Adulto"],
    [1, "Cardeologia Infantil"],
    [2, "Cirugia Cardiaca"],
    [3, "Cirugia General Adulto"],
    [4, "Cirugia General Infantil"],
    [5, "Cirugia Vascular"],
    [6, "Dental"],
    [7, "Fonoaudiologia"],
    [8, "Ginecologia General"],
    [9, "Medicina General Adulto"],
    [10, "Medicina General Infantil"],
    [11, "Neurocirugia"],
    [12, "Nutricionista"],
    [13, "Odontologia"],
    [14, "Psicologia"],
    [15, "Traumatologia"]
]


class Cita(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    fecha_consulta = models.DateField()
    correo = models.EmailField()
    prevision_salud = models.IntegerField(choices=opciones_previsiones)
    area_medica = models.IntegerField(choices=opciones_areas_medicas)

    def __str__(self):
        return self.nombre