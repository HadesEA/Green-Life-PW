from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from random import randrange
from .forms import RegistroCombinadoForm
from .models import Cultivo, Counter, CounterHT, CounterMQ7, CounterMQ8, CounterTC, CounterTF, CounterTS, CounterLUX, CounterPH, CounterTDS, CounterLluvia, CounterDistancia


# Create your views here.


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
            return redirect("home:index")
        else:
            return redirect("home:index")

def graphics(request):
    return render(request, 'home/graphics.html')

def graphicsagua(request):
    return render(request, 'home/graphicsagua.html')

def cliente(request):
    return render(request, 'home/cliente.html')

def prediccion(request):
    return render(request, 'home/prediccion.html')





# Vistas de los formularios
def registro_combinado(request):
    print("Método: ", request.method)
    print("Datos POST recibidos: ", request.POST)
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
