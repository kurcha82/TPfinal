from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    contrasenia = forms.CharField(label="Contraseña")
    confContrasenia = forms.CharField(label="Confirmar Contraseña")

class UserRegisterform(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)