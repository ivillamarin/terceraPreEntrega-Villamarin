from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def inicio(request):
    return HttpResponse("vista inicio")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return HttpResponse("profesores")

def estudiantes(request):
    return HttpResponse("estudiantes")

def entregables(request):
    return HttpResponse("entregables")
