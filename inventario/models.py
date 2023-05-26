from django.db import models

# Create your models here.

class productos(models.Model):
    id  = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, blank=False, null=False, unique=True)
    descripcion = models.CharField(max_length=300, blank=False, null=False)
    referencia = models.CharField(max_length=50, blank=False, null=False)
    peso = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    volumen = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    costo = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    precio = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    unidad_empaque = models.DecimalField(max_digits=16, decimal_places=4, blank=False, null=False)
    proveedor = models.CharField(max_length=300, blank=False, null=False)
    estado = models.IntegerField(default=1, blank=True, null=True)

class inventario(models.Model):
    id  = models.AutoField(primary_key=True)
    sku = models.ForeignKey(productos, db_column='sku', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300, blank=False, null=False)
    referencia = models.CharField(max_length=50, blank=False, null=False)
    nivel_inventario = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    almacen = models.CharField(max_length=300, blank=False, null=False)
    proveedor = models.CharField(max_length=300, blank=False, null=False)


class movimientos(models.Model):
    id  = models.AutoField(primary_key=True)
    sku = models.ForeignKey(productos, db_column='sku', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300, blank=False, null=False)
    referencia = models.CharField(max_length=50, blank=False, null=False)
    fecha = models.DateField()
    tipo_movimiento = models.CharField(max_length=300, blank=False, null=False)
    salidas = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    entradas = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    nivel_inventario_final = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    almacen = models.CharField(max_length=300, blank=False, null=False)

class reposicion(models.Model):
    id  = models.AutoField(primary_key=True)
    sku = models.ForeignKey(productos, db_column='sku', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300, blank=False, null=False)
    referencia = models.CharField(max_length=50, blank=False, null=False)
    nivel_inventario_minimo = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    nivel_inventario_maximo = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    nivel_inventario_actual = models.ForeignKey(inventario, db_column='nivel_inventario', on_delete=models.CASCADE)
    almacen = models.CharField(max_length=300, blank=False, null=False)