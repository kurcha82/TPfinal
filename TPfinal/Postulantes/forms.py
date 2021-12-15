from django import forms

class PostFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.CharField()
    telefono = forms.IntegerField()
    presentacion = forms.CharField()
    formacion = forms.CharField()


class ReqFormulario(forms.Form):
    posicion = forms.CharField()
    descripcion = forms.CharField(max_length=400)
    formacionReq = forms.CharField()
    interno = forms.BooleanField()
    propMonetaria = forms.IntegerField()