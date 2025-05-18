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
    # path('register/', views.register, name='register'),
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
    path('inventario/', views.inventario_view, name='inventario'),
    # Rutas CRUD para Proveedor
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    # Rutas CRUD para equipo
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:equipo_id>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),
    # Rutas CRUD para Insumos
    path('insumos/', views.listar_insumos, name='listar_insumos'),
    path('insumos/crear/', views.crear_insumo, name='crear_insumo'),
    path('insumos/editar/<int:insumo_id>/', views.editar_insumo, name='editar_insumo'),
    path('insumos/eliminar/<int:insumo_id>/', views.eliminar_insumo, name='eliminar_insumo'),
    # Rudtas CRUD para Plagas
    path('plagas/', views.listar_plagas, name='listar_plagas'),
    path('plagas/crear/', views.crear_plaga, name='crear_plaga'),
    path('plagas/editar/<int:plaga_id>/', views.editar_plaga, name='editar_plaga'),
    path('plagas/eliminar/<int:plaga_id>/', views.eliminar_plaga, name='eliminar_plaga'),
    # Rutas CRUD para enfermedades
    path('enfermedades/', views.listar_enfermedades, name='listar_enfermedades'),
    path('enfermedades/crear/', views.crear_enfermedad, name='crear_enfermedad'),
    path('enfermedades/editar/<int:enfermedad_id>/', views.editar_enfermedad, name='editar_enfermedad'),
    path('enfermedades/eliminar/<int:enfermedad_id>/', views.eliminar_enfermedad, name='eliminar_enfermedad'),
    # Rutas CRUD para Tratamientos
    path('tratamientos/', views.listar_tratamientos, name='listar_tratamientos'),
    path('tratamientos/crear/', views.crear_tratamiento, name='crear_tratamiento'),
    path('tratamientos/editar/<int:tratamiento_id>/', views.editar_tratamiento, name='editar_tratamiento'),
    path('tratamientos/eliminar/<int:tratamiento_id>/', views.eliminar_tratamiento, name='eliminar_tratamiento'),
    path('reporte_agua/', views.generar_pdf_agua, name='reporte_agua'),
    path('reporte_suelo/', views.generar_pdf_suelo, name='reporte_suelo'),
]