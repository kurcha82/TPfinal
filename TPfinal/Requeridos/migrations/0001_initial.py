# Generated by Django 3.2.9 on 2021-12-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('deLaEmpresa', models.BooleanField(null=True)),
                ('propMonetaria', models.IntegerField()),
                ('fechaPublicacion', models.DateField()),
            ],
        ),
    ]
