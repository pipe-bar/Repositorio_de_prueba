from django import template
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from  django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):

        self.nombre = nombre

        self.apellido = apellido

def herencia(request):
    fecha = datetime.datetime.now
    return render(request,"daugther.html",{"dame_fecha":fecha})

def herencia_2(request):
    
    return render(request,"daugther2.html")

def saludo(request):

    #nombre = "Duvan Felipe"
    #apellido = "Barbosa Barbosa"
    fecha = datetime.datetime.now
    listado_personas = ["Duvan","Dayana","El Pepe","Ete sech"]

    persona1 = Persona("Duvan Felipe Barbosa","Ete sech")

    #doc_externo = open("C:/Users/USUARIO/Desktop/Project-Python/first_project/first_project/plantillas/mi_plantilla.html")

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo = loader.get_template('mi_plantilla.html')

    # ctx = Context({"nombre_persona":persona1.nombre , "apellido_persona":persona1.apellido , "ahora":fecha, "listado":listado_personas})

    #documento = doc_externo.render({"nombre_persona":persona1.nombre , "apellido_persona":persona1.apellido , "ahora":fecha, "listado":listado_personas})

    return render(request,"mi_plantilla.html",{"nombre_persona":persona1.nombre , 
    "apellido_persona":persona1.apellido , "ahora":fecha, "listado":listado_personas})

def despedida(request):

    return HttpResponse("Esto es una despedida desde django")

def dame_fecha(request):

    fecha = datetime.datetime.now()

    documento = """
    <html>
    <body>
    <h1>
    La hora y fecha actuales son %s
    </h1>
    </body>
    </html> 

    """ % fecha
    
    return HttpResponse(documento)

def calcula_edades(request,edad,anio):

    #edad_actual = 20
    periodo = anio - 2021
    edad_futura = edad + periodo

    documento = "<html><body><h1>En el año %s tendras %s </h1></body></html>" %(anio,edad_futura)

    return HttpResponse(documento)
    