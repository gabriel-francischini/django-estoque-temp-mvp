from django.db import models

# Create your models here.
class Produto(models.Model):
    tipo = models.CharField(max_length=120)
    categoria = models.CharField(max_length=80)


# veja: https://docs.djangoproject.com/en/2.2/topics/db/models/#fields
class Entrada(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


class Estoque(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    estoque = models.IntegerField()
