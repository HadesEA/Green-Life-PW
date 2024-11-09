from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)

class Cultivo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_planta = models.CharField(max_length=50)
    tiempo_crecimiento = models.IntegerField()

class Parcela(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100)
    tamaño = models.DecimalField(max_digits=10, decimal_places=2)

class Finca(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

class Siembra(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE)
    fecha_siembra = models.DateField()

class Cosecha(models.Model):
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    fecha_cosecha = models.DateField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=20)

class AplicacionInsumo(models.Model):
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

class Clima(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    precipitacion = models.DecimalField(max_digits=5, decimal_places=2)

class Plaga(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Tratamiento(models.Model):
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    fecha_tratamiento = models.DateField()
    descripcion = models.TextField()

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=50)

class Sensores(models.Model):
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    ultima_lectura = models.DateTimeField()

class Rangos(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE)
    tipo_medicion = models.CharField(max_length=50)
    valor_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_maximo = models.DecimalField(max_digits=10, decimal_places=2)

class Estacion(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tipo_estacion = models.CharField(max_length=50)

class EstadoSuelo(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField()
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_nutrientes = models.TextField()

class EstadoAgua(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField()
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    conductividad = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_contaminantes = models.TextField()

class EstadoAmbiental(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateField()
    calidad_aire = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_ruido = models.DecimalField(max_digits=5, decimal_places=2)
    radiacion_solar = models.DecimalField(max_digits=5, decimal_places=2)

class Reportes(models.Model):
    tipo_reporte = models.CharField(max_length=50)
    fecha_generacion = models.DateField()
    contenido = models.TextField()

class Alertas(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo_alerta = models.CharField(max_length=50)
    mensaje = models.TextField()
    estado = models.CharField(max_length=20)

class Mantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    tipo_mantenimiento = models.CharField(max_length=50)
    descripcion = models.TextField()

class RolUsuario(models.Model):
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.TextField()

class ConfiguracionSensores(models.Model):
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    parametro = models.CharField(max_length=50)
    valor = models.CharField(max_length=100)

class EventoSoporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_evento = models.DateTimeField()
    tipo_evento = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20)

class HistoricoClimatico(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    datos_climaticos = models.TextField()
