"""sap URL Configuration

The `urlpatterns` list routes URLs to webapp. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function webapp
    1. Add an import:  from my_app import webapp
    2. Add a URL to urlpatterns:  path('', webapp.home, name='home')
Class-based webapp
    1. Add an import:  from other_app.webapp import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personas.views import detalle_persona, agregarPersona, editarPersona, eliminarPersona, detalleDomicilio, \
    agregarDomicilio, editarDomicilio, eliminarDomicilio
from webapp import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('detalle_persona/<int:id>', detalle_persona),
    path('nueva_persona', agregarPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona),
    # Next to this comment starts the Direcctions template.
    path('direcciones',views.domicilios ,name="direcctions"),
    path('detalle-domicilio/<int:id>',detalleDomicilio),
    path('editar-domicilio/<int:id>',editarDomicilio),
    path('eliminar-domicilio/<int:id>', eliminarDomicilio),
    path('agregar-domicilio/', agregarDomicilio),
]
