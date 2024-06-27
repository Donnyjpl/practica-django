from django.contrib import admin
from .models import Vendedor, Cliente, Auto, Venta,Persona

admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Venta)

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo_electronico')
    search_fields = ('nombre', 'apellido')
    
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'fecha_nacimiento')
    search_fields = ('email', 'nombre')    