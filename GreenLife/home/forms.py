from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Cliente, Finca, Parcela, Estacion, EventoSoporte, Usuario, Equipo, Mantenimiento, Proveedor, Plaga, Insumo, Tratamiento, Enfermedad

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

    parcela_ubicacion = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese ubicación de la parcela'})
    )
    parcela_tamaño = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese tamaño de la parcela (mts)'})
    )
    parcela_cliente = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'placeholder': 'Ingrese su id'})
    )

    estacion_nombre = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo', 'readonly': 'readonly', 'placeholder': 'Estación 1'})
    )

    estacion_ubicacion = forms.CharField(
        max_length=1,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form_input campo','readonly': 'readonly', 'placeholder': 'Ubicación Parcela'})
    )

    TIPOS_ESTACION = [
    ('Suelo', 'Medidor de Suelo'),
    ('Agua', 'Medidor de Agua'),
    ('Ambiente', 'Medidor de Ambiente'),
    ('Completo', 'Medidor completo'),
    ]

    estacion_tipo = forms.ChoiceField(
        choices=TIPOS_ESTACION,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control form_input campo'})
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
        
        parcela = Parcela(
            cliente=cliente,
            ubicacion=self.cleaned_data['parcela_ubicacion'],
            tamaño=self.cleaned_data['parcela_tamaño']
        )
        parcela.save()

        estacion = Estacion(
            nombre=self.cleaned_data['estacion_nombre'],
            ubicacion=self.cleaned_data['estacion_ubicacion'],
            tipo_estacion=self.cleaned_data['estacion_tipo']
        )
        estacion.save()

        return cliente, finca, parcela, estacion

class EventoSoporteForm(forms.ModelForm):
    # Aquí definimos el diccionario dentro de la clase
    TIPOS_SOPORTE_CATEGORIZADOS = {
        "Hardware": [
            {"clave": "instalacion_configuracion", "nombre": "Instalación y configuración"},
            {"clave": "mantenimiento_preventivo", "nombre": "Mantenimiento preventivo"},
            {"clave": "reparacion_hardware", "nombre": "Reparación de hardware"},
            {"clave": "actualizacion_firmware", "nombre": "Actualización de firmware"},
            {"clave": "calibracion_sensores", "nombre": "Calibración de sensores"},
            {"clave": "revision_infraestructura", "nombre": "Revisión de infraestructura eléctrica"}
        ],
        "Software": [
            {"clave": "errores_software", "nombre": "Errores en el software"},
            {"clave": "actualizacion_software", "nombre": "Actualización de software"},
            {"clave": "integracion_plataformas", "nombre": "Integración con otras plataformas"},
            {"clave": "personalizacion_sistema", "nombre": "Personalización del sistema"},
        ],
        "Datos": [
            {"clave": "conectividad_datos", "nombre": "Conectividad de datos"},
            {"clave": "analisis_datos", "nombre": "Análisis de datos"},
            {"clave": "backup_recuperacion", "nombre": "Backup y recuperación de datos"},
        ],
        "General": [
            {"clave": "resolucion_dudas", "nombre": "Resolución de dudas"},
        ]
    }

    TIPOS_MANTENIMIENTO = {
        "Preventivo": [
            {"clave": "revision_periodica", "nombre": "Revisión periódica"},
            {"clave": "limpieza", "nombre": "Limpieza general"},
            {"clave": "actualizacion_software", "nombre": "Actualización de software"},
            {"clave": "calibracion_equipos", "nombre": "Calibración de equipos"}
        ],
        "Correctivo": [
            {"clave": "reparacion_componente", "nombre": "Reparación de componentes"},
            {"clave": "sustitucion_pieza", "nombre": "Sustitución de piezas"},
            {"clave": "resolucion_errores", "nombre": "Resolución de errores críticos"}
        ],
        "Predictivo": [
            {"clave": "monitoreo_estado", "nombre": "Monitoreo de estado"},
            {"clave": "analisis_datos", "nombre": "Análisis de datos históricos"},
            {"clave": "deteccion_anomalias", "nombre": "Detección de anomalías"}
        ],
        "General": [
            {"clave": "otro", "nombre": "Otro tipo de mantenimiento"}
        ]
    }


    TIPO_SOPORTE_CHOICES = [
        (categoria, [(opcion["clave"], opcion["nombre"]) for opcion in opciones])
        for categoria, opciones in TIPOS_SOPORTE_CATEGORIZADOS.items()
    ]

    tipo_evento = forms.ChoiceField(
        choices=TIPO_SOPORTE_CHOICES,
        label="Tipo de soporte técnico",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Nuevo campo para estado
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('resuelto', 'Resuelto')
    ]
    estado = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        label="Estado del soporte",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

      # Campos adicionales para el modelo Mantenimiento
    equipo = forms.ModelChoiceField(
        queryset=Equipo.objects.all(),
        required=False,
        label="Equipo relacionado",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fecha_mantenimiento = forms.DateField(
        required=False,
        label="Fecha del mantenimiento",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    TIPO_MANTENIMIENTO_CHOICES = [
        (categoria, [(opcion["clave"], opcion["nombre"]) for opcion in opciones])
        for categoria, opciones in TIPOS_MANTENIMIENTO.items()
    ]

    tipo_mantenimiento = forms.ChoiceField(
        choices=TIPO_MANTENIMIENTO_CHOICES,
        label="Tipo de mantenimiento",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    descripcion_mantenimiento = forms.CharField(
        required=False,
        label="Descripción del mantenimiento",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    class Meta:
        model = EventoSoporte
        fields = ['usuario', 'tipo_evento', 'descripcion', 'estado']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar el queryset del campo usuario
        self.fields['usuario'].queryset = Usuario.objects.all()

    def guardar(self):
        evento_soporte = EventoSoporte(
            usuario=self.cleaned_data['usuario'],
            tipo_evento=self.cleaned_data['tipo_evento'],
            descripcion=self.cleaned_data['descripcion'],
            estado=self.cleaned_data['estado'],
            fecha_evento=timezone.now()
        )
        evento_soporte.save()

         # Si se llenaron los campos relacionados con Mantenimiento, crearlo
        if self.cleaned_data.get('equipo') and self.cleaned_data.get('tipo_mantenimiento'):
            mantenimiento = Mantenimiento(
                equipo=self.cleaned_data['equipo'],
                fecha_mantenimiento=self.cleaned_data['fecha_mantenimiento'],
                tipo_mantenimiento=self.cleaned_data['tipo_mantenimiento'],
                descripcion=self.cleaned_data['descripcion_mantenimiento']
            )
            mantenimiento.save()

        return evento_soporte
    

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'registro__item form_input form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'registro__item form_input form-control'}), label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'registro__item form_input form-control'}),
            'email': forms.EmailInput(attrs={'class': 'registro__item form_input form-control'}),
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirm



class PrediccionForm(forms.Form):
    fecha_riego = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tiempo_riego = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Días'}))

    fecha_cosecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tiempo_cosecha = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Días'}))

    fecha_siembra = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tiempo_siembra = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Días'}))

    fecha_insumo = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tiempo_insumo = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Días'}))

        

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }

class PlagaForm(forms.ModelForm):
    class Meta:
        model = Plaga
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la plaga'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
        }

class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la enfermedad'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
        }

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['siembra', 'tipo', 'fecha_tratamiento', 'descripcion']
        widgets = {
            'siembra': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de tratamiento'}),
            'fecha_tratamiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'tipo', 'fecha_adquisicion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del equipo'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo del equipo'}),
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'tipo', 'fecha_insumo', 'tiempo_insumo', 'unidad_medida']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del insumo'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo del insumo'}),
            'fecha_insumo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tiempo_insumo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo (días)'}),
            'unidad_medida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unidad de medida'}),
        }
