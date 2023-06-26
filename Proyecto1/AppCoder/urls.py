from django.urls import path
from AppCoder.views import inicio, cursos, profesores, estudiantes, setEstudiante, getProfesores, buscarProfesor

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('setEstudiante/', setEstudiante, name="setEstudiante"),
    path('getProfesores/', getProfesores, name="getProfesores"),
    path('buscarProfesor/', buscarProfesor, name="buscarProfesor")
]