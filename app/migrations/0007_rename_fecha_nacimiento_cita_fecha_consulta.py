# Generated by Django 4.1.3 on 2022-11-19 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_cita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='fecha_nacimiento',
            new_name='fecha_consulta',
        ),
    ]
