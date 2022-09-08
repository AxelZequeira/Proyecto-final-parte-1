
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("usuarios/", usuarios, name="usuarios"),
    path("staff/", staff, name="staff"),
    path("servidor/", servidor, name="servidor"),
    path("busquedaUsuarios/", busquedaUsuarios, name="busquedaUsuarios"),
    path("resultadoUsuarios/", resultadoUsuarios, name="resultadoUsuarios"),
]
