from django.db import models

# Create your models here.

##############   Genericos

class Medida(models.Model):
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=10)


##############   Propios

class Factura(models.Model):
    TIPO_FACTURA = (
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
    )
    comprador = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=50)
    tipo =  models.CharField(max_length=2, choices=TIPO_FACTURA)
    fecha = models.DateField(auto_now=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    medida = models.ForeignKey(Medida)

class ProductoFactura(models.Model):
    factura = models.ForeignKey(Factura)
    producto = models.ForeignKey(Producto)
    medida = models.ForeignKey(Medida)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10)
    precio = models.DecimalField(decimal_places=2, max_digits=10)

    


