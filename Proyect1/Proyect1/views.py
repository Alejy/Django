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
    apellido = "Alonso"
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre":nombre, "apellido": apellido})
    documento = plt.render(ctx)
    return HttpResponse(documento)

class Usuario():
    def __init__(self, name, apellido):
        self.name = name
        self.apellido = apellido

def prueba_seven(request):
    user = Usuario("Carlos", "Alonso")
    doc_externo = open("C:/Users/Alejandro Alonso/OneDrive - Alejandro/Escritorio/Desarrollo/Python/Django/Proyect1/Proyect1/templates/prueba_seven.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre":user.name, "apellido": user.apellido})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def prueba_eight(request):
    #Recupera listas en el html. Como ejecutar codigo python en plantillas html
    nombres = ["Carlos", "Paco", "Alejandro"]
    doc_externo = open("C:/Users/Alejandro Alonso/OneDrive - Alejandro/Escritorio/Desarrollo/Python/Django/Proyect1/Proyect1/templates/prueba_eight.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombres":nombres})
    documento = plt.render(ctx)
    return HttpResponse(documento)

#Loader cargador de plantillas reduce el codigo
#Configurar file settings with templates

from django.template import loader

'''
Ahora con la funcion loader nos permite acceder a la plantilla indicando unicamente el archivo ya que hemos indicado el path en el archivo settings.
Para añadir el contexto ya no es necesario llamar a context sino que podemos pasar como contexto un diccionario directamente.
 '''
def prueba_nine(request):
    nombres = ["Carlos", "Paco", "Alejandro"]
    doc_externo = loader.get_template('prueba_nine.html')
    ctx = {"nombres":nombres}
    documento = doc_externo.render(ctx)
    return HttpResponse(documento)

#Render Simplifica aun mas el codigo

from django.shortcuts import render
def prueba_ten(request):
    nombres = ["Carlos", "Paco", "Alejandro"]
    return render(request, "prueba_ten.html", {"nombres":nombres})

#Plantillas incrustadas se declara en el html
#Para plantillas incrustadas generar subdirectorios dentro de templates y asi organizar todas las plantillas.
def plantilla_incrustada(request):
    return render(request, "principal.html")

#Herencia de plantillas-- Si en la pagina web la cabecerla y el pie de pagina se mantiene
#Creamos una plantilla padre con la cabecera y el pie pero que se modifique el contenido de las paginas para cada una de ellas.
#Tener en cuenta que hay que llamar al contenido y no al padre.
def herencias_html(request):
    return render(request, "contenido.html")