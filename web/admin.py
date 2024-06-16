from django.contrib import admin

# Register your models here.
from .models import Vendedor, Cliente, Auto, Venta

admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Venta)