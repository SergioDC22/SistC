from dataclasses import field
from django import  forms
from .models import Cliente, Impuesto

class ImpuestoForm(forms.ModelForm):
    class Meta:
        model=Impuesto
        fields= '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields= '__all__'