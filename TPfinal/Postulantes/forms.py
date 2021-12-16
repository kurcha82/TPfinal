from django import forms
import datetime

class RegistroForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    contrasenia = forms.CharField(label="Contraseña")
    confContrasenia = forms.CharField(label="Confirmar Contraseña")

class PostFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.CharField()
    telefono = forms.IntegerField()
    presentacion = forms.CharField(label="Presentacion Personal")
    formacion = forms.CharField()


class ReqFormulario(forms.Form):
    posicion = forms.CharField()
    sector = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=400)
    formacionReq = forms.CharField(label="Formacion Requerida")
    deLaEmpresa = forms.BooleanField(required=False, label="Interno Empresa")
    propMonetaria = forms.IntegerField(label="Propuesta Monetaria")
    fechaPublicacion = forms.DateField(initial=datetime.date.today(), label="Fecha Publicación")
