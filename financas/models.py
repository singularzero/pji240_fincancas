from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField( auto_created=True, primary_key=True, serialize=False)
    nome = models.CharField(max_length=50, null=False, blank=False)


class Gastos(models.Model):
    id = models.AutoField( auto_created=True, primary_key=True, serialize=False)
    categoria = models.CharField(max_length=50, null=False, blank=False)
    retirado_em = models.DateField(
        auto_now_add=False, null=False, blank=False, editable=True
    )
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)


class Receitas(models.Model):
    id = models.AutoField( auto_created=True, primary_key=True, serialize=False)
    categoria = models.CharField(max_length=50, null=False, blank=False)
    adicionado_em = models.DateField(
        auto_now_add=False, null=False, blank=False, editable=True
    )
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
