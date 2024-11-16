from django import forms
from .models import Cliente

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']  # Reemplaza con los campos que deseas incluir
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.EmailInput(attrs={'class': 'form-control'}),
            'email': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'telefono': forms.Textarea(attrs={'class': 'form-control'}),
        }
