from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
     = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='autos/', null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
class Venta(models.Model):
    auto = models.OneToOneField(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)  # Fecha de la venta
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, default=1)  # Vendedor del auto, con valor por defecto

    def __str__(self):
        return f"Venta de {self.auto} a {self.comprador} el {self.fecha_venta}"
