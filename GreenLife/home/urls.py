from django.urls import path
from django.contrib import admin
from . import views

app_name = 'home'
urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name="index"),
    path('get_chart/', views.get_chart, name='get_chart')
]