from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from personas.forms import PersonaFrom as PersonaForm
from personas.forms import DomicilioFrom
# Create your views here.
from personas.models import Persona,Domicilio


def detalle_persona(req,id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona,pk=id)
    return render(req,'personas/detalle.html', {'persona':persona})


def agregarPersona(req):
    if req.method == 'POST':
        formaPersona = PersonaForm(req.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()

    return render(req,'personas/nuevo.html', {'formaPersona':formaPersona})

def editarPersona(req,id):
    persona = get_object_or_404(Persona, pk=id)
    if req.method == 'POST':
        formaPersona = PersonaForm(req.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(req,'personas/editar.html', {'formaPersona':formaPersona})

def eliminarPersona(req,id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

#

def detalleDomicilio(req,id):
    detalles = get_object_or_404(Domicilio,pk=id)
    return render(req,'direcciones/detalle-domicilio.html',{'detalles':detalles})

def agregarDomicilio(req):
    if req.method == 'POST':
       formDomicilio = DomicilioFrom(req.POST)
       if formDomicilio.is_valid():
            formDomicilio.save()
            return redirect('direcctions')
    else:
        formDomicilio = DomicilioFrom()
    return render(req,'direcciones/nuevo-domicilio.html',{'formDomicilio':formDomicilio})

def editarDomicilio(req,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if req.method == 'POST':
       formDomicilio = DomicilioFrom(req.POST,instance=domicilio)
       if formDomicilio.is_valid():
            formDomicilio.save()
            return redirect('direcctions')
    else:
        formDomicilio = DomicilioFrom(instance=domicilio)
    return render(req,'direcciones/nuevo-domicilio.html',{'formDomicilio':formDomicilio})

def eliminarDomicilio(req,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('direcctions')