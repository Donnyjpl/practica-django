"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index,nosotros,portafolio,contacto,lista_autos,lista_cliente,menu, filtrar_autos_por_marca
from .views import agregar_auto,agregar_cliente,agregar_vendedor,agregar_ventas,lista_ventas,lista_vendedores
from .views import filtrar_ventas_por_marca,formulario, logout_view,login_view,perfil_view
urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('nosotros/', nosotros, name='nosotros'),
    path('portafolio/', portafolio, name='portafolio'),
    path('contacto/', contacto, name='contacto'),
    path('lista_autos/', lista_autos, name='lista_autos'),
    path('lista_ventas/', lista_ventas, name='lista_ventas'),
    path('lista_clientes/', lista_cliente, name='lista_clientes'),
    path('lista_vendedores/', lista_vendedores, name='lista_vendedores'),
    path('agregar/auto', agregar_auto, name='agregar_auto'),
    path('agregar/cliente', agregar_cliente, name='agregar_cliente'),
    path('agregar/vendedor', agregar_vendedor, name='agregar_vendedor'),
    path('agregar/ventas', agregar_ventas, name='agregar_ventas'),
    path('filtro/auto', filtrar_autos_por_marca, name='filtro_auto'),
    path('filtro/venta', filtrar_ventas_por_marca, name='filtro_venta'),
    path('formulario', formulario, name='formulario'),
    path('web/login/', login_view, name='login'),
    path('web/logout/', logout_view, name='logout'),
    path('web/perfil/', perfil_view, name='perfil'),
    
                                                       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)