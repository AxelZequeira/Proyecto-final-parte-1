
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("usuarios/", usuario, name="usuarios"),
    path("staff/", staff, name="staff"),
    path("servidor/", servidor, name="servidor"),
]
