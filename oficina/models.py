from django.db import models


class Carro(models.Model):
    placa = models.CharField(max_length=10)
    nome = models.CharField(max_length=30)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    ano_fabricacao = models.CharField(max_length=12)
    ano_modelo = models.CharField(max_length=12)
    cor = models.CharField(max_length=15)

    def __str__(self):
        return self.placa


class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=13)
    endereco = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)


    def __str__(self):
        return self.nome

class Mecanico(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=13)
    endereco = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    nome_pai = models.CharField(max_length=30)
    nome_mae = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Orcamento(models.Model):
    mecanico = models.ForeignKey(Mecanico, on_delete=models.SET_NULL, null=True)
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=5)

    def __str__(self):
        return self.cliente