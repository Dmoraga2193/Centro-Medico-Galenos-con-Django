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
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    prevision_salud = models.ForeignKey(Prevision_Salud, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    especialidad = models.TextField()

    def __str__(self):
        return self.nombre
