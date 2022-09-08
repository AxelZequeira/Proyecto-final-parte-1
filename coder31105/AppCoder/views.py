from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
import http
from AppCoder.forms import *
# Create your views here.

def inicio(request):
    return render (request, "AppCoder/inicio.html")


def usuario(request):
    return render (request, "AppCoder/usuario.html")



def staff(request):
    return render (request, "AppCoder/staff.html")

def servidor(request):
    return render (request, "AppCoder/servidor.html")


def usuarios(request):
    if request.method=="POST":
        form=UsuariosForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            nickname=informacion["nickname"]
            usuario = Usuarios(nombre=nombre, apellido=apellido,nickname=nickname, email=email)
            usuario.save()
            return render(request, 'AppCoder/inicio.html')
        
    
    else:
        formulario=UsuariosForm()
        return render (request, "AppCoder/usuarios.html", {"formulario":formulario})



def staff(request):
    if request.method=="POST":
        form=StaffForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            nickname=informacion["nickname"]
            area_control=informacion["area_control"]
            staff= Staff(nombre=nombre, apellido=apellido,nickname=nickname, area_control=area_control)
            staff.save()
            return render(request, 'AppCoder/inicio.html')
        

    else:
        formulario=StaffForm()
        return render (request, "AppCoder/staff.html", {"formulario":formulario})



def servidor(request):
    if request.method=="POST":
        form=ServidorForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            canal_1=informacion["canal_1"]
            canal_2=informacion["canal_2"]
            canal_3=informacion["canal_3"]
            
            canales= Servidor(canal_1=canal_1, canal_2=canal_2, canal_3=canal_3)
            canales.save()
            return render(request, 'AppCoder/inicio.html')
        

    else:
        formulario=ServidorForm()
        return render (request, "AppCoder/servidor.html", {"formulario":formulario})


def busquedaUsuarios(request):
    return render(request, "AppCoder/busquedaUsuarios.html")


def resultadoUsuarios(request):
    if request.GET["nickname"]:
        nickname=request.GET["nickname"]
        usuarios=Usuarios.objects.filter(nickname=nickname)
        return render(request, "AppCoder/resultadoUsuarios.html", {"usuarios":usuarios})
    else:
        return render(request, "AppCoder/busquedaUsuarios.html", {"mensaje":"Ingrese un nickname:"})
    return HttpResponse(respuesta)