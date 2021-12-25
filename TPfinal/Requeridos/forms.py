from django import forms
import datetime

class ReqFormulario(forms.Form):
    posicion = forms.CharField()
    sector = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=400)
    formacionReq = forms.CharField(label="Formacion Requerida")
    deLaEmpresa = forms.BooleanField(required=False, label="Interno Empresa")
    propMonetaria = forms.IntegerField(label="Propuesta Monetaria")
    fechaPublicacion = forms.DateField(initial=datetime.date.today(), label="Fecha Publicación")