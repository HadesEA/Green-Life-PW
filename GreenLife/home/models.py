from django.db import models
from django.utils.timezone import now

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cultivo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_planta = models.CharField(max_length=50)
    tiempo_crecimiento = models.IntegerField()

    def __str__(self):
        return self.nombre

class Parcela(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100)
    tamaño = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Parcela en {self.ubicacion} de {self.cliente}"

class Finca(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"Finca {self.nombre} ({self.ubicacion})"

class Siembra(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE, null=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    tiempo_siembra = models.IntegerField(default=0)
    fecha_siembra = models.DateField(default=now)

    def __str__(self):
        parcela_ubicacion = self.parcela.ubicacion if self.parcela else "Sin parcela"
        cultivo_nombre = self.cultivo.nombre if self.cultivo else "Sin cultivo"
        return f"Siembra de {cultivo_nombre} en {parcela_ubicacion}"

class Cosecha(models.Model):
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE, null=True)
    tiempo_cosecha = models.IntegerField(default=0)
    fecha_cosecha = models.DateField(default=now)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cosecha de {self.siembra.cultivo.nombre} - {self.cantidad} kg"

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fecha_insumo = models.DateField(default=now)
    tiempo_insumo = models.IntegerField(default=0)
    unidad_medida = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class AplicacionInsumo(models.Model):
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateField(default=now)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Aplicación de {self.insumo.nombre} para {self.siembra.cultivo.nombre}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Clima(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField(default=now)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    precipitacion = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Clima en {self.parcela.ubicacion} - {self.fecha}"

class Plaga(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Tratamiento(models.Model):
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE, null=True)
    tipo = models.CharField(max_length=50)
    fecha_tratamiento = models.DateField(default=now)
    descripcion = models.TextField()

    def __str__(self):
        if self.siembra and self.siembra.cultivo:
            return f"Tratamiento para {self.siembra.cultivo.nombre} - {self.tipo}"
        return "Tratamiento (datos incompletos)"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField(default=now)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Sensores(models.Model):
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    ultima_lectura = models.DateTimeField()

    def __str__(self):
        return f"Sensor {self.tipo} - {self.ubicacion}"

class Rangos(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE)
    tipo_medicion = models.CharField(max_length=50)
    valor_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_maximo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rango de {self.cultivo.nombre} - {self.tipo_medicion}"

class Estacion(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tipo_estacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class EstadoSuelo(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField()
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_nutrientes = models.TextField()

    def __str__(self):
        return f"Estado del suelo en {self.parcela.ubicacion} - {self.fecha}"

class EstadoAgua(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField()
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    conductividad = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_contaminantes = models.TextField()

    def __str__(self):
        return f"Estado del agua en {self.parcela.ubicacion} - {self.fecha}"

class EstadoAmbiental(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField()
    calidad_aire = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_ruido = models.DecimalField(max_digits=5, decimal_places=2)
    radiacion_solar = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Estado ambiental en {self.parcela.ubicacion} - {self.fecha}"

class Reportes(models.Model):
    tipo_reporte = models.CharField(max_length=50)
    fecha_generacion = models.DateField()
    contenido = models.TextField()

    def __str__(self):
        return self.tipo_reporte

class Alertas(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo_alerta = models.CharField(max_length=50)
    mensaje = models.TextField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Alerta en {self.parcela.ubicacion} - {self.tipo_alerta}"

class Mantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    tipo_mantenimiento = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"Mantenimiento de {self.equipo.nombre} - {self.tipo_mantenimiento}"

class RolUsuario(models.Model):
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_rol

class ConfiguracionSensores(models.Model):
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    parametro = models.CharField(max_length=50)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return f"Configuración de {self.sensor.tipo} - {self.parametro}"

class EventoSoporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_evento = models.DateTimeField()
    tipo_evento = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Evento de soporte para {self.usuario.nombre} - {self.tipo_evento}"

class HistoricoClimatico(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    datos_climaticos = models.TextField()

    def __str__(self):
        return f"Histórico climático de {self.parcela.ubicacion}"

class AlertasUsuario(models.Model):
    alerta = models.ForeignKey(Alertas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    notificacion = models.BooleanField(default=False)

    def __str__(self):
        return f"Alerta de {self.alerta.tipo_alerta} para {self.usuario.nombre}"

class Counter(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cnt = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterDistancia(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntDistancia = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterHT(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntHT = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterLUX(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntLUX = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterLluvia(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntLluvia = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterMQ7(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntMQ7 = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterMQ8(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntMQ8 = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterPH(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntPH = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterTC(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntTC = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterTDS(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntTDS = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterTF(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntTF = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class CounterTS(models.Model):
    nodo = models.CharField(max_length=255, primary_key=True)
    cntTS = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

class Riego(models.Model):
    fecha_riego = models.DateField(default=now)
    tiempo_riego = models.IntegerField(default=0)