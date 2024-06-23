from django.shortcuts import render, redirect
from .models import Auto, Vendedor, Cliente, Venta,Usuario
from .forms import AutoForm, VendedorForm, ClienteForm, VentaForm, FiltroMarcaForm,FiltroVentaPorMarcaForm,ExampleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'index.html')

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
    return render(request, 'lista_vendedores.html', {'vendedores': vendedores})

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

def filtrar_autos_por_marca(request):
    if request.method == 'POST':
        form = FiltroMarcaForm(request.POST)
        if form.is_valid():
            marca_elegida = form.cleaned_data['marca']
            autos_filtrados = Auto.objects.filter(marca=marca_elegida)
            return render(request, 'filtro.html', {'form': form, 'autos': autos_filtrados})
    else:
        form = FiltroMarcaForm()
    
    return render(request, 'filtro.html', {'form': form})
def filtrar_ventas_por_marca(request):
    if request.method == 'POST':
        form = FiltroVentaPorMarcaForm(request.POST)
        if form.is_valid():
            marca_elegida = form.cleaned_data['marca']
            ventas_filtradas = Venta.objects.filter(auto__marca=marca_elegida)
            return render(request, 'filtrar_ventas.html', {'form': form, 'ventas': ventas_filtradas})
    else:
        form = FiltroVentaPorMarcaForm()
    
    return render(request, 'filtrar_ventas.html', {'form': form})


def formulario(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            cont = form.cleaned_data
            return render(request, 'formulario.html', {'form': form, 'cont': cont})
    else:
        form = ExampleForm()
    
    return render(request, 'formulario.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # Verificar si 'username' y 'password' están en request.POST
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil')
            else:
                messages.error(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Por favor, ingrese nombre de usuario y contraseña')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')
    
    
    