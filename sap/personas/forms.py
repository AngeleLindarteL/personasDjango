from django.forms import ModelForm, EmailInput
from personas.models import Persona,Domicilio

class PersonaFrom(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class DomicilioFrom(ModelForm):
    class Meta:
        model = Domicilio
        fields = "__all__"