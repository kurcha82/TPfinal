from django import forms
import datetime

class PostFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.CharField()
    telefono = forms.IntegerField()
    presentacion = forms.CharField()
    formacion = forms.CharField()


class ReqFormulario(forms.Form):
    posicion = forms.CharField()
    sector = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=400)
    formacionReq = forms.CharField()
    deLaEmpresa = forms.BooleanField(required=False)
    propMonetaria = forms.IntegerField()
    fechaPublicacion = forms.DateField(initial=datetime.date.today())
