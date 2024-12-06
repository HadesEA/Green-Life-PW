from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
import csv
import os
from django.conf import settings
from random import randrange
from datetime import timedelta
from .forms import RegistroCombinadoForm, EventoSoporteForm, RegistroForm, PrediccionForm, ProveedorForm, PlagaForm, EnfermedadForm, TratamientoForm, EquipoForm, InsumoForm
from .models import (Cultivo, Counter, CounterHT, CounterMQ7, CounterMQ8, CounterTC, CounterTF, CounterTS, 
CounterLUX, CounterPH, CounterTDS, CounterLluvia, CounterDistancia, EventoSoporte, Cosecha, Siembra, Riego, Insumo, Proveedor, Equipo, Enfermedad, Plaga, Tratamiento)


# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

class index(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:cliente")
        else:
            return redirect("home:index")

def graphics(request):
    return render(request, 'home/graphics.html')

def graphicsagua(request):
    return render(request, 'home/graphicsagua.html')

def cliente(request):
    return render(request, 'home/cliente.html')

def soporte(request):
    return render(request, 'home/soporte.html')

def prediccion(request):
    return render(request, 'home/prediccion.html')

def inventario(request):
    return render(request, 'home/inventario.html')





# Vistas de los formularios
def registro_combinado(request):
    form = RegistroCombinadoForm()
    
    # Poblar el campo select con datos de la base de datos
    opciones = Cultivo.objects.values_list('id', 'nombre')  # Cambia según tu modelo.
    opciones_choices = [(op[0], op[1]) for op in opciones]

    # Si el formulario se envió (POST)
    if request.method == 'POST':
        form = RegistroCombinadoForm(request.POST)
        form.fields['opciones'].choices = opciones_choices
        if form.is_valid():
            print("Formulario válido, reditiriengo...")
            form.guardar()  # Esto debe guardar el formulario si es necesario
            return redirect('home:graphics')
        else:
            print("Formulario no válido, errores: ", form.errors)
    else:
        form = RegistroCombinadoForm()

    opciones = Cultivo.objects.values_list('id', 'nombre')  # Cambia según tu modelo.
    form.fields['opciones'].choices = [(op[0], op[1]) for op in opciones]

    return render(request, 'home/cliente.html', {'form': form})

def registrar_soporte(request):
    if request.method == 'POST':
        form = EventoSoporteForm(request.POST)
        if form.is_valid():
            form.guardar()
            messages.success(request, 'Formulario enviado con éxito')
            return redirect('home:soporte')  # Redirigir después de guardar
    else:
        form = EventoSoporteForm()

    return render(request, 'home/soporte.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home:cliente')  # Redirige al registro de cliente después del registro
    else:
        form = RegistroForm()
    return render(request, 'home/register.html', {'form': form})

def prediccion_view(request):
    csv_path = os.path.join(settings.BASE_DIR, 'home', 'data', 'predicciones_9.csv')
    recomendaciones = {}

    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            fecha_riego = form.cleaned_data['fecha_riego']
            tiempo_riego = form.cleaned_data['tiempo_riego']

            fecha_cosecha = form.cleaned_data['fecha_cosecha']
            tiempo_cosecha = form.cleaned_data['tiempo_cosecha']

            fecha_siembra = form.cleaned_data['fecha_siembra']
            tiempo_siembra = form.cleaned_data['tiempo_siembra']

            fecha_insumo = form.cleaned_data['fecha_insumo']
            tiempo_insumo = form.cleaned_data['tiempo_insumo']

            # Calcular fechas recomendadas
            recomendaciones['riego'] = fecha_riego + timedelta(days=tiempo_riego)
            recomendaciones['cosecha'] = fecha_cosecha + timedelta(days=tiempo_cosecha)
            recomendaciones['siembra'] = fecha_siembra + timedelta(days=tiempo_siembra)
            recomendaciones['insumo'] = fecha_insumo + timedelta(days=tiempo_insumo)

            if fecha_cosecha and tiempo_cosecha:
                Cosecha.objects.create(
                    siembra=None,
                    fecha_cosecha=fecha_cosecha,
                    tiempo_cosecha=tiempo_cosecha,
                    cantidad=0  # Ajusta si tienes datos de cantidad inicial
                )

            if fecha_siembra and tiempo_siembra:
                Siembra.objects.create(
                    fecha_siembra=fecha_siembra,
                    tiempo_siembra=tiempo_siembra,
                    cultivo=None,  # Cambia según la lógica de cultivo
                    parcela=None  # Cambia según la lógica de parcela
                )

            if fecha_insumo and tiempo_insumo:
                Insumo.objects.create(
                    nombre='Insumo Default',  # Cambia si tienes un nombre específico
                    tipo='Tipo Default',  # Cambia según la lógica de tipo
                    fecha_insumo=fecha_insumo,
                    tiempo_insumo=tiempo_insumo,
                    unidad_medida='kg'  # Ajusta la unidad si es necesario
                )

            if fecha_riego and tiempo_riego:
                Riego.objects.create(
                    fecha_riego=fecha_riego,
                    tiempo_riego=tiempo_riego  # Asume que duracion es un campo en Riego
                )

            # Opcional: Guardar datos en un archivo CSV
            with open(csv_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Evento', 'Fecha Recomendación'])
                for evento, fecha in recomendaciones.items():
                    writer.writerow([evento, fecha])
    else:
        form = PrediccionForm()

    return render(request, 'home/prediccion.html', {'form': form, 'recomendaciones': recomendaciones})

def inventario_view(request):
    # Formularios
    proveedor_form = ProveedorForm(request.POST or None)
    plaga_form = PlagaForm(request.POST or None)
    enfermedad_form = EnfermedadForm(request.POST or None)
    tratamiento_form = TratamientoForm(request.POST or None)
    equipo_form = EquipoForm(request.POST or None)
    insumo_form = InsumoForm(request.POST or None)

    if request.method == 'POST':
        # Guardar Proveedor
        if 'registrar_proveedor' in request.POST and proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('home:inventario')

        # Guardar Plaga
        elif 'registrar_plaga' in request.POST and plaga_form.is_valid():
            plaga_form.save()
            return redirect('home:inventario')

        # Guardar Enfermedad
        elif 'registrar_enfermedad' in request.POST and enfermedad_form.is_valid():
            enfermedad_form.save()
            return redirect('home:inventario')

        # Guardar Tratamiento
        elif 'registrar_tratamiento' in request.POST and tratamiento_form.is_valid():
            tratamiento_form.save()
            return redirect('home:inventario')

        # Guardar Equipo
        elif 'registrar_equipo' in request.POST and equipo_form.is_valid():
            equipo_form.save()
            return redirect('home:inventario')

        # Guardar Insumo
        elif 'registrar_insumo' in request.POST and insumo_form.is_valid():
            insumo_form.save()
            return redirect('home:inventario')

    # Consultar datos existentes
    proveedores = Proveedor.objects.all()
    plagas = Plaga.objects.all()
    enfermedades = Enfermedad.objects.all()
    tratamientos = Tratamiento.objects.all()
    equipos = Equipo.objects.all()
    insumos = Insumo.objects.all()

    return render(request, 'home/inventario.html', {
        'proveedor_form': proveedor_form,
        'plaga_form': plaga_form,
        'enfermedad_form': enfermedad_form,
        'tratamiento_form': tratamiento_form,
        'equipo_form': equipo_form,
        'insumo_form': insumo_form,
        'proveedores': proveedores,
        'plagas': plagas,
        'enfermedades': enfermedades,
        'tratamientos': tratamientos,
        'equipos': equipos,
        'insumos': insumos,
    })




# Vistas para las gráficas

# Endpoint para datos dinámicos
def obtener_datos_relacionados(request):
    if request.method == 'GET':
        cultivo_id = request.GET.get('cultivo_id')
        print(f"cultivo_id recibido: {cultivo_id}")  # Depuración
        if cultivo_id:
            cultivo = Cultivo.objects.filter(id=cultivo_id).first()
            print(f"Cultivo encontrado: {cultivo}")  # Depuración
            if cultivo:
                datos = {
                    'tipo_planta': cultivo.tipo_planta,
                    'tiempo_crecimiento': cultivo.tiempo_crecimiento,
                }
                return JsonResponse(datos)
    return JsonResponse({'error': 'No se encontraron datos relacionados.'})


def obtener_datos_humedad(request):
    # Consultar los datos de ambas tablas
    counters = Counter.objects.all()
    ht_data = CounterHT.objects.all()

    # Combinar los datos en una sola estructura
    data = {
        "counter": [
            {"nodo": counter.nodo, "cnt": counter.cnt, "fecha_actualizacion": counter.fecha_actualizacion}
            for counter in counters
        ],
        "counter_ht": [
            {"nodo": counter_ht.nodo, "cnt_ht": counter_ht.cntHT, "fecha_actualizacion": counter_ht.fecha_actualizacion}
            for counter_ht in ht_data
        ]
    }

    # Devolver los datos como JSON
    return JsonResponse({"data": data})

def obtener_datos_gas(request):
    # Consultar los datos de ambas tablas
    mq7_data = CounterMQ7.objects.all()
    mq8_data = CounterMQ8.objects.all()

    # Combinar los datos en una estructura
    data = {
        "mq7": [
            {"nodo": mq7.nodo, "cnt_mq7": mq7.cntMQ7, "fecha_actualizacion": mq7.fecha_actualizacion}
            for mq7 in mq7_data
        ],
        "mq8": [
            {"nodo": mq8.nodo, "cnt_mq8": mq8.cntMQ8, "fecha_actualizacion": mq8.fecha_actualizacion}
            for mq8 in mq8_data
        ]
    }

    # Devolver los datos como JSON
    return JsonResponse({"data": data})

def obtener_datos_temperatura(request):
    # Consultar los datos de las tres tablas
    tc_data = CounterTC.objects.all()
    tf_data = CounterTF.objects.all()
    ts_data = CounterTS.objects.all()

    # Combinar los datos en una estructura
    data = {
        "tc": [
            {"nodo": tc.nodo, "cnt_tc": tc.cntTC, "fecha_actualizacion": tc.fecha_actualizacion}
            for tc in tc_data
        ],
        "tf": [
            {"nodo": tf.nodo, "cnt_tf": tf.cntTF, "fecha_actualizacion": tf.fecha_actualizacion}
            for tf in tf_data
        ],
        "ts": [
            {"nodo": ts.nodo, "cnt_ts": ts.cntTS, "fecha_actualizacion": ts.fecha_actualizacion}
            for ts in ts_data
        ]
    }

    print(data)
    # Devolver los datos como JSON
    return JsonResponse({"data": data})

def obtener_datos_lux(request):
    # Consultar los datos de la tabla CounterLUX
    lux_data = CounterLUX.objects.all()

    # Preparar los datos en la estructura deseada
    data = {
        "lux": [
            {"nodo": lux.nodo, "cnt_lux": lux.cntLUX, "fecha_actualizacion": lux.fecha_actualizacion}
            for lux in lux_data
        ]
    }

    # Devolver los datos como JSON
    return JsonResponse({"data": data})

def obtener_datos_ph(request):
    # Consultar los datos de la tabla CounterPH
    ph_data = CounterPH.objects.all()

    # Preparar los datos en la estructura deseada
    data = {
        "ph": [
            {"nodo": ph.nodo, "cnt_ph": ph.cntPH, "fecha_actualizacion": ph.fecha_actualizacion}
            for ph in ph_data
        ]
    }

    # Devolver los datos como JSON
    return JsonResponse({"data": data})

def obtener_datos_tds(request):
    # Consultar los datos de la tabla CounterTDS
    tds_data = CounterTDS.objects.all()

    # Preparar los datos en la estructura deseada
    data = {
        "tds": [
            {"nodo": tds.nodo, "cnt_tds": tds.cntTDS, "fecha_actualizacion": tds.fecha_actualizacion}
            for tds in tds_data
        ]
    }

    # Devolver los datos como JSON
    return JsonResponse({"data": data})
from .models import CounterLluvia  # Asegúrate de importar el modelo

def obtener_datos_agua(request):
    # Consultar los datos de la tabla CounterLluvia
    lluvia_data = CounterLluvia.objects.all()

    # Preparar los datos en la estructura deseada
    data = {
        "lluvia": [
            {"nodo": lluvia.nodo, "cnt_lluvia": lluvia.cntLluvia, "fecha_actualizacion": lluvia.fecha_actualizacion}
            for lluvia in lluvia_data
        ]
    }

    # Devolver los datos como JSON
    return JsonResponse({"data": data})

from .models import CounterDistancia  # Asegúrate de importar el modelo

def obtener_datos_distancia(request):
    # Consultar los datos de la tabla CounterDistancia
    distancia_data = CounterDistancia.objects.all()

    # Preparar los datos en la estructura deseada
    data = {
        "distancia": [
            {"nodo": distancia.nodo, "cnt_distancia": distancia.cntDistancia, "fecha_actualizacion": distancia.fecha_actualizacion}
            for distancia in distancia_data
        ]
    }

    # Devolver los datos como JSON
    return JsonResponse({"data": data})

