from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
import http
# Create your views here.

def inicio(request):
    return render (request, "AppCoder/inicio.html")


def usuario(request):
    return render (request, "AppCoder/usuario.html")



def staff(request):
    return render (request, "AppCoder/staff.html")

def servidor(request):
    return render (request, "AppCoder/servidor.html")
