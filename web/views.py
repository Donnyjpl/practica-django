from django.shortcuts import render, redirect
from .models import Auto, Vendedor, Cliente, Venta
from .forms import AutoForm, VendedorForm, ClienteForm, VentaForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def portafolio(request):
    return render(request, 'portafolio.html')

def contacto(request):
    return render(request, 'contacto.html')

def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'lista_autos.html', {'autos': autos})

def lista_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'lista_compradores.html', {'cliente': cliente})

def lista_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'lista_vendedor.html', {'vendedores': vendedores})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})

def agregar_auto(request):
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El auto se ha guardado correctamente!')
            return redirect('lista_autos')
    else:
        form = AutoForm()
    return render(request, 'agregar_auto.html', {'form': form})

def agregar_vendedor(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El vendedor se ha guardado correctamente!')
            return redirect('lista_vendedores')
    else:
        form = VendedorForm()
    return render(request, 'agregar_vendedor.html', {'form': form})

def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El comprador se ha guardado correctamente!')
            return redirect('lista_compradores')
    else:
        form = ClienteForm()
    return render(request, 'agregar_comprador.html', {'form': form})

def agregar_ventas(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡La venta se ha guardado correctamente!')
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'agregar_ventas.html', {'form': form})
def menu(request):
    return render(request, 'menu.html')