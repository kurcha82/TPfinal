# Generated by Django 3.2.9 on 2021-12-16 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Postulantes', '0002_alter_postulante_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requeridos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.CharField(max_length=40)),
                ('sector', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=400)),
                ('formacionReq', models.CharField(max_length=40)),
                ('deLaEmpresa', models.BooleanField()),
                ('propMonetaria', models.IntegerField()),
                ('fechaPublicacion', models.DateField()),
            ],
        ),
    ]
