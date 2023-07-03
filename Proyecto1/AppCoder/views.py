from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCoder.models import Estudiante
from AppCoder.models import Profesor

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def setEstudiante(request):
    if request.method == 'POST':
        estudiante = Estudiante(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"])
        estudiante.save()
        return render(request,"AppCoder/inicio.html")
    return render(request, "AppCoder/setEstudiante.html")

def getProfesores(request):
    return render(request, "AppCoder/GetProfesores.html")

def buscarProfesor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesor = Profesor.objects.filter(nombre = nombre)
        return render(request, "/AppCoder/getProfesores.html", {"profesor": profesor})
    else:
        respuesta = "profesor no existe"

    return HttpResponse(respuesta)
