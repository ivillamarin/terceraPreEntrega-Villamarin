from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("ke onda") 

def miNombreEs(self, nombre):
    data= f"mi nombre es: <h2>{nombre}</h2> "
    return HttpResponse(data)

def probandoTemplate(self):

    nombre= "ivan"
    apellido= "villamarin"
    namelist = ["candela", "karina", "juancho"]

    diccionario = {
        "nombre" : nombre,
        "apellido" : apellido,
        "namelist" : namelist
    }

    loader.get_template("template1.html")
    #myHtml = open ("C:/nuevoProyecto/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = loader.get_template("template1.html")
    #myContext = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
