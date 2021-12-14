from django import forms

class PostFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.CharField()
    telefono = forms.IntegerField()
    presentacion = forms.CharField()
    formacion = forms.CharField()