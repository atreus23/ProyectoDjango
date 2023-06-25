from django import forms

class UserForm(forms.Form):
    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=10)
    edad  = forms.IntegerField()
    email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    
class MostrarUsuarios(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)