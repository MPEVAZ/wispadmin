from unicodedata import name
from django.db import models
from django.utils.timezone import now 

# Create your models here.
class Zon(models.Model):
    name=models.CharField(max_length=200,verbose_name="Nombre zona")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural ="Zonas"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Pack(models.Model):
    name=models.CharField(max_length=200,verbose_name="Nombre Paquete")
    down=models.CharField(max_length=50,verbose_name="Velocidad Descarga")
    up=models.CharField(max_length=50,verbose_name="Velocidad Subida")
    price=models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Paquete"
        verbose_name_plural ="Paquetes"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.CharField(max_length=100,verbose_name="Usuario")
    name = models.CharField(max_length=200,verbose_name="Nombre cliente")
    zon = models.ForeignKey(Zon, verbose_name="Zona", on_delete=models.CASCADE)
    package = models.ForeignKey(Pack, verbose_name="Paquete", on_delete=models.CASCADE)
    telephone= models.CharField(max_length=15,verbose_name="Telefono")
    pay_day = models.CharField(max_length=2,verbose_name="Fecha de pago")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    update = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural ="Clientes"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Payment(models.Model):
    name= models.CharField(max_length=100,verbose_name="Mes")
    corte = models.DateTimeField(verbose_name="Fecha de corte",default=now)
    client = models.ForeignKey(Client, verbose_name="Cliente", on_delete=models.CASCADE)
    paid_out = models.CharField(max_length=2, verbose_name="Pagado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural ="Pagos"
        ordering = ["-created"]

    def __str__(self):
        return self.name
