from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona, Domicilio

# Create your webapp here.


def inicio(request):
    cont = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request,'bienvenido.html', {'cont':cont,'personas':personas})


def  domicilios(req):
    cont = Domicilio.objects.count()
    domicilios = Domicilio.objects.order_by('id')
    return render(req,'domicilios.html', {'cont':cont, 'domicilios':domicilios})