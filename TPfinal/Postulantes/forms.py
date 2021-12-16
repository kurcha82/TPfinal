from django import forms
import datetime

class Registro(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    contrasenia = forms.CharField(max_length=40)
    confContrasenia = forms.CharField(max_length=40)

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
