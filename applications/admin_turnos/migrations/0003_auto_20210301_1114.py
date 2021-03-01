# Generated by Django 3.1.6 on 2021-03-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_turnos', '0002_cancha_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='status',
            field=models.CharField(choices=[('pendiente', 'El turno se encuentra pendiente'), ('finalizado', 'El turno se encuentra finalizado')], default='pendiente', max_length=32),
        ),
    ]
