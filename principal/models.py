from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.IntegerField()
    email = models.EmailField(unique=True)
    rua = models.CharField(max_length=100)
    numeroDaRua = models.IntegerField()
    cep = models.IntegerField()
    telefone = models.IntegerField()


class Lanche(models.Model):
    nome = models.CharField(max_length=20)
    descrição = models.CharField(max_length=100)
    preço = models.IntegerField()
    foto = models.ImageField()


class Almoço(models.Model):
    nome = models.CharField(max_length=20)
    descrição = models.CharField(max_length=100)
    preço = models.IntegerField()
    foto = models.ImageField()


class Janta(models.Model):
    nome = models.CharField(max_length=20)
    descrição = models.CharField(max_length=100)
    preço = models.IntegerField()
    foto = models.ImageField()


class Sobremesa(models.Model):
    nome = models.CharField(max_length=20)
    descrição = models.CharField(max_length=100)
    preço = models.IntegerField()
    foto = models.ImageField()


class Vinho(models.Model):
    nome = models.CharField(max_length=20)
    descrição = models.CharField(max_length=100)
    preço = models.IntegerField()
    foto = models.ImageField()


class Bebida(models.Model):
    nome = models.CharField(max_length=20)
    descrição = models.CharField(max_length=100)
    preço = models.IntegerField()
    foto = models.ImageField()


class ItemDoEstoque(models.Model):
    nome = models.CharField(max_length=50)
    dataDeValidade = models.DateField()


class Reserva(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    telefone = models.IntegerField()
    data = models.DateField()
    horário = models.IntegerField()
    quantidadeDePessoas = models.IntegerField()
