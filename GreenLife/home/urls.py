from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'
urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name="index"),
    path('graphics/', views.graphics, name='graphics'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('soporte/', views.registrar_soporte, name='soporte'),
    path('graphicsagua/', views.graphicsagua, name='graphicsagua'),
    path('cliente/', views.registro_combinado, name='cliente'),
    path('obtener_datos/', views.obtener_datos_relacionados, name='obtener_datos'),
    path('datos-humedad/', views.obtener_datos_humedad, name='datos-humedad'),
    path('datos-gas/', views.obtener_datos_gas, name='datos-gas'),
    path('datos-temperatura/', views.obtener_datos_temperatura, name='datos-temperatura'),
    path('datos-lux/', views.obtener_datos_lux, name='datos-lux'),
    path('datos-ph/', views.obtener_datos_ph, name='datos-ph'),
    path('datos-tds/', views.obtener_datos_tds, name='datos-tds'),
    path('datos-agua/', views.obtener_datos_agua, name='datos-agua'),
    path('datos-distancia/', views.obtener_datos_distancia, name='datos-distancia'),
    path('prediccion/', views.prediccion_view, name='prediccion'),
    path('inventario/', views.inventario_view, name='inventario')
]