from django import forms
from .models import Cliente

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form_input', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form_input', 'placeholder': 'Ingrese su apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form_input', 'placeholder': 'Ingrese su correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form_input', 'placeholder': 'Ingrese su número de teléfono'}),
        }
