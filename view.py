from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
def saludo(request):  #primera vista

    nombre="Juan"
    apellido="Diaz"
    #ahora=datetime.datetime.now()
    doc_externo=open("C:/Users/na4_c/Desktop/DJango/Proyecto1/Proyecto1/Plantillas/primeraplantilla.html")
                     
    plt=Template(doc_externo.read())
    
    doc_externo.close()
    
    #contexto puede recibir diccionarios tuplas, etc
    ctx=Context({"nombre_persona":nombre, "Apellidos":apellido,"momento_Actual":datetime.datetime.now()})

    documento=plt.render(ctx)

    return HttpResponse(documento)




def pedidox(request):

   # return HttpResponse(request)


   return render(request,"Base.html")


def despedida(request):

    
    qwe={"hola1":"chao1","hola2":"chao2"}

    return HttpResponse(qwe["hola1"])


def dameFecha(request):
 fecha_actual=datetime.datetime.now()
 documentos= """ <html>
                            <body>
                            <h1>                            
                            Fecha y hora actual %s
                            </h1> 
                            </body>
                     </html>   
                """% fecha_actual

 return HttpResponse(documentos)


def calcularedad(request, agno, edad):
    #edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo
    documento="<html><body><h2> En el año %s tendreas %s"%(agno,edadFutura)

    return HttpResponse	(documento)
