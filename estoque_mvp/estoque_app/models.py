from django.db import models

# Create your models here.
class Produto(models.Model):
    tipo = models.CharField(max_length=120)
    categoria = models.CharField(max_length=80)

    # veja: https://docs.djangoproject.com/en/2.2/topics/db/models/#model-methods
    # veja: https://docs.djangoproject.com/en/2.2/topics/db/models/#overriding-predefined-model-methods
    # Nós vamos ter o nosso próprio save() que faz questão de criar um Estoque
    # caso esse estoque não exista previamente!
    def save(self, *args, **kwargs):
        if self.id == None: # Ops, esse tipo de Produto não existia previamente!!
            pass
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return ('<Produto #{}. Tipo: "{}", categoria: "{}">'
                .format(self.id, self.tipo, self.categoria))


# veja: https://docs.djangoproject.com/en/2.2/topics/db/models/#fields
class Entrada(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return ('<Entrada #{} para "{}", qtd: {}>'
                .format(self.id,
                        Produto.objects.get(pk=self.produto_id),
                        quantidade))


class Estoque(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE,
                                   primary_key=True)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return ('<Estoque #{} para "{}": {}>'
                .format(self.id, Produto.objects.get(pk=self.produto_id),
                        self.estoque))
