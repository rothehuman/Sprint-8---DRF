# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class DireccionesSucursal(models.Model):
    branch_address_id = models.AutoField(primary_key=True, blank=True)
    street = models.TextField(blank=True, null=True)
    street_number = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones_sucursal'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address = models.ForeignKey(DireccionesSucursal, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.IntegerField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class TipoCuenta(models.Model):
    account_type_id = models.AutoField(primary_key=True, blank=True)
    type_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey(TipoCuenta, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class DireccionesCliente(models.Model):
    address_id = models.AutoField(primary_key=True, blank=True)
    street = models.TextField()
    street_number = models.IntegerField(blank=True, null=True)
    city = models.TextField()
    region = models.TextField()
    country = models.TextField()
    customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones_cliente'


class DireccionesEmpleado(models.Model):
    address_id = models.AutoField(primary_key=True, blank=True)
    street = models.TextField()
    street_number = models.IntegerField(blank=True, null=True)
    city = models.TextField()
    region = models.TextField()
    country = models.TextField()
    employee_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'direcciones_empleado'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.IntegerField(db_column='employee_DNI')
    branch_id = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcaTarjetas(models.Model):
    creditcardbrand_id = models.AutoField(primary_key=True, blank=True)
    creditcardbrand_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjetas'


class TipoTarjeta(models.Model):
    cardtype_id = models.AutoField(primary_key=True, blank=True)
    cardtype_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_tarjeta'


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True, blank=True)
    card_pan = models.TextField()
    card_cvv = models.IntegerField()
    valid_from = models.TextField()
    valid_thru = models.TextField()
    cardtype = models.ForeignKey(TipoTarjeta, on_delete=models.SET_NULL, null=True, default=None)
    creditcardbrand = models.ForeignKey(MarcaTarjetas, on_delete=models.SET_NULL, null=True, default=None)
    customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        managed = False
        db_table = 'prestamo'


class TipoCliente(models.Model):
    customer_type_id = models.AutoField(primary_key=True, blank=True)
    type_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'



