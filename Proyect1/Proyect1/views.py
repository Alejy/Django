from django.http import HttpResponse
from django.template import Template, Context
import datetime

def index(request):
    return HttpResponse("Hola")

def prueba(request):
    return HttpResponse("<html><body><h1>Hola mundo</h1></body></html>")

def prueba_two(request):
    documento = "<html><body><h1>Hola mundo2</h1></body></html>"
    return HttpResponse(documento)

def prueba_three(request):
    fecha = datetime.datetime.now()
    documento = f"<html><body><h1>Hola mundo3</h1><h2>La hora es {fecha}</h2></body></html>"
    return HttpResponse(documento)

def prueba_four(request, edad, ano):
    #Recupera la edad por metodo get y calcula la edad en un futuro.
    periodo = ano - 2022
    edad_futura = edad + periodo
    documento = f"<html><body><h1>Hola mundo4</h1><h2>En el año {ano} tendras {edad_futura} años.</h2></body></html>"
    return HttpResponse(documento)

def prueba_five(request):
    #Importamos html desde una plantilla
    doc_externo = open("C:/Users/Alejandro Alonso/OneDrive - Alejandro/Escritorio/Desarrollo/Python/Django/Proyect1/Proyect1/templates/prueba_five.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def prueba_six(request):
    #Importamos html desde una plantilla y le pasamos variables que influyen en el html
    doc_externo = open("C:/Users/Alejandro Alonso/OneDrive - Alejandro/Escritorio/Desarrollo/Python/Django/Proyect1/Proyect1/templates/prueba_six.html")
    nombre = "Alejandro"
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre":nombre})
    documento = plt.render(ctx)
    return HttpResponse(documento)