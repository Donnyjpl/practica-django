from django.contrib import admin

# Register your models here.
from .models import Vendedor, Cliente, Auto, Venta, Usuario

admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Venta)
admin.site.register(Usuario)