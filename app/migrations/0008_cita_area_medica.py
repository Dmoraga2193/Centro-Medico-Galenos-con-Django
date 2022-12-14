# Generated by Django 4.1.3 on 2022-11-20 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_fecha_nacimiento_cita_fecha_consulta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='area_medica',
            field=models.IntegerField(choices=[[0, 'Cardeologia Adulto'], [1, 'Cardeologia Infantil'], [2, 'Cirugia Cardiaca'], [3, 'Cirugia General Adulto'], [4, 'Cirugia General Infantil'], [5, 'Cirugia Vascular'], [6, 'Dermatologia'], [7, 'Fonoaudiologia'], [8, 'Ginecologia General'], [9, 'Medicina General Adulto'], [10, 'Medicina General Infantil'], [11, 'Neurocirugia'], [12, 'Nutricionista'], [13, 'Odontologia'], [14, 'Psicologia'], [15, 'Traumatologia']], default=1),
            preserve_default=False,
        ),
    ]
