from django import forms
from .models import Cliente, Finca

class RegistroCombinadoForm(forms.Form):
    # Campos del modelo Cliente
    cliente_nombre = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese su nombre'})
    )
    cliente_apellido = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese su apellido'})
    )
    cliente_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese su correo electrónico'})
    )
    cliente_telefono = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese su número de teléfono'})
    )

    # Campos del modelo Finca
    finca_nombre = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese nombre de la finca'})
    )
    finca_ubicacion = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese ubicación de la finca'})
    )
    finca_cliente = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese su id'})
    )

     # Nuevo campo para el select
    opciones = forms.ChoiceField(
        choices=[],  # Se llenará dinámicamente en la vista.
        widget=forms.Select(attrs={'class': 'form-control campo'})
    )

  # Campos para mostrar los datos dinámicamente    
    tipo_planta = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control campo', 'readonly': 'readonly'})
    )
    
    tiempo_crecimiento = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control campo', 'readonly': 'readonly'})
    )

    def guardar(self):
        # Crear instancia del modelo Cliente
        cliente = Cliente(
            nombre=self.cleaned_data['cliente_nombre'],
            apellido=self.cleaned_data['cliente_apellido'],
            email=self.cleaned_data['cliente_email'],
            telefono=self.cleaned_data['cliente_telefono'],
        )
        cliente.save()

        # Crear instancia del modelo Finca
        finca = Finca(
            cliente=cliente,
            nombre=self.cleaned_data['finca_nombre'],
            ubicacion=self.cleaned_data['finca_ubicacion']
        )
        finca.save()

        return cliente, finca
