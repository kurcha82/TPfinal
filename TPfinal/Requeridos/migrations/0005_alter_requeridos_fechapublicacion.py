# Generated by Django 3.2.9 on 2022-01-10 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requeridos', '0004_alter_requeridos_fechapublicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requeridos',
            name='fechaPublicacion',
            field=models.DateField(default=datetime.date(2022, 1, 10), verbose_name='Fecha de publicación'),
        ),
    ]
