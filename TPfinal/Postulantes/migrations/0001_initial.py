# Generated by Django 3.2.9 on 2022-01-06 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Requeridos', '0002_alter_requeridos_fechapublicacion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('mail', models.CharField(max_length=40)),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('presentacion', models.CharField(max_length=100, verbose_name='Presentación')),
                ('formacion', models.CharField(max_length=100, verbose_name='Formación')),
                ('requerido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Requeridos.requeridos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
