from django import forms
from .models import Auto,Vendedor,Cliente,Venta,Usuario


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar los autos con cantidad mayor o igual a 1
        self.fields['auto'].queryset = Auto.objects.filter(cantidad__gte=1)

    class Meta:
        model = Venta
        fields = '__all__'
        
class FiltroMarcaForm(forms.Form):
    marca_choices = [(marca, marca) for marca in Auto.objects.values_list('marca', flat=True).distinct()]
    marca = forms.ChoiceField(choices=marca_choices, label='Selecciona una marca')

class FiltroVentaPorMarcaForm(forms.Form):
    marca_choices = [(marca, marca) for marca in Auto.objects.values_list('marca', flat=True).distinct()]
    marca = forms.ChoiceField(choices=marca_choices, label='Selecciona una marca')
        

class ExampleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Primer Nombre'}))
    age = forms.IntegerField(min_value=0, max_value=120, label='Edad')
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Debes ser mayor de edad.")
        return age
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Tu correo electrónico'}))
    birth_date = forms.DateField(required=False, label='Fecha de Nacimiento')
    favorite_color = forms.ChoiceField(
        choices=[('blue', 'Azul'), ('green', 'Verde'), ('red', 'Rojo')],
        label='Color Favorito'
    )
    profile_picture = forms.ImageField(required=False, label='Foto de Perfil')
    subscribe_newsletter = forms.BooleanField(
        required=False, initial=True, label='Suscribirse al Boletín'
    )

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields ='__all__'