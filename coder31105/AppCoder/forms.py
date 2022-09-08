from django import forms

class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    nickname = forms.CharField(max_length=50)

class StaffForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50)
    area_control = forms.CharField(max_length=50)

class ServidorForm(forms.Form):
    canal_1= forms.CharField(max_length=50)
    canal_2= forms.CharField(max_length=50)
    canal_3= forms.CharField(max_length=50)