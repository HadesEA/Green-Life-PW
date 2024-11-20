from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from random import randrange
from .forms import RegistroClienteForm


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


def cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:graphics')  # Redirige a una vista de éxito
    else:
        form = RegistroClienteForm()
    
    return render(request, 'home/cliente.html', {'form': form})
    
    
    
    

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