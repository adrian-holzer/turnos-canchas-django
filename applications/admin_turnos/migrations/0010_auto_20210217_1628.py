# Generated by Django 3.1.6 on 2021-02-17 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_turnos', '0009_auto_20210217_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 2, 17, 16, 28, 21, 897258), verbose_name='time'),
        ),
    ]
