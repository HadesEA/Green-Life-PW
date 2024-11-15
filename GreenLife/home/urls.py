from django.urls import path
from django.contrib import admin
from . import views

app_name = 'home'
urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name="index"),
    path('get_chart/', views.get_chart, name='get_chart'),
    path('graphics/', views.graphics, name='graphics'),
    path('graphicsagua/', views.graphicsagua, name='graphicsagua'),
    path('cliente/', views.cliente, name='cliente'),
    path('prediccion/', views.prediccion, name='prediccion'),
]