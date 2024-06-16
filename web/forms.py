from django import forms
from .models import Auto,Vendedor,Cliente,Venta

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'precio', 'cantidad', 'color', 'foto']
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido','correo_electronico',]
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido','correo_electronico',]  
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['auto', 'cliente', 'vendedor',]      
        

        