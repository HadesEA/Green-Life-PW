from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from random import randrange
from .forms import RegistroCombinadoForm
from .models import Cultivo


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
    form = RegistroCombinadoForm()
    
    # Poblar el campo select con datos de la base de datos
    opciones = Cultivo.objects.values_list('id', 'nombre')  # Cambia según tu modelo.
    form.fields['opciones'].choices = [(op[0], op[1]) for op in opciones]

    # Si el formulario se envió (POST)
    if request.method == 'POST':
        form = RegistroCombinadoForm(request.POST)
        if form.is_valid():
            form.guardar()  # Esto debe guardar el formulario si es necesario
            return redirect('home:graphics')

    return render(request, 'home/cliente.html', {'form': form})


# Endpoint para datos dinámicos
def obtener_datos_relacionados(request):
    if request.method == 'GET':
        cultivo_id = request.GET.get('cultivo_id')
        if cultivo_id:
            cultivo = Cultivo.objects.filter(id=cultivo_id).first()
            if cultivo:
                # Devolver cada dato por separado
                datos = {
                    'nombre': cultivo.nombre,
                    'tipo_planta': cultivo.tipo_planta,
                    'tiempo_crecimiento': cultivo.tiempo_crecimiento,
                }
                return JsonResponse(datos)
    return JsonResponse({'error': 'No se encontraron datos relacionados.'})

    
    



# /////////////
def get_chart(_request):
    serie=[]
    counter=0

    while(counter<7):
        serie.append(randrange(100,400))
        counter += 1

    chart={
        'xAxis':[
            {
                'type': "category",
                'data': ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            }
        ],
        'yAxis':[
            {
                'type': "value"
            }
        ],
        'series':[
            {
                'data':serie,
                'type': "line"
            }
        ]
    }

    return JsonResponse(chart)