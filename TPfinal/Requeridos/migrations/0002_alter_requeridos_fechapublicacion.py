# Generated by Django 3.2.9 on 2022-01-06 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requeridos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requeridos',
            name='fechaPublicacion',
            field=models.DateField(default=datetime.date(2022, 1, 5), verbose_name='Fecha de publicación'),
        ),
    ]
