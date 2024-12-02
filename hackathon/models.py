from django.core.exceptions import ValidationError
from django.db import models
from uploader.models import Image


def only_numbers(value):
    if not value.isdigit():
        raise ValidationError("Este campo deve conter apenas números")


class Cargo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    senha = models.CharField(max_length=128)  # Aumentei o tamanho para armazenar hashes
    matricula = models.CharField(max_length=20, unique=True)  # Novo campo matrícula

    def __str__(self):
        return f"{self.nome}"


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=45)
    cnpj_cliente = models.CharField(max_length=14)
    endereco_cliente = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_cliente


class Orcamentos(models.Model):
    descricao_orcamento = models.CharField(max_length=45)
    datasolicitada_orcamento = models.DateField(auto_now_add=True)
    valor_orcamento = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    tipo_orcamento = models.CharField(max_length=45, null=True)
    endereco_cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="cliente"
    )

    def __str__(self):
        return self.descricao_orcamento


class Servico(models.Model):
    descricao_servico = models.CharField(max_length=45)
    cliente = models.OneToOneField(
        Cliente, on_delete=models.PROTECT, related_name="Cliente"
    )
    orcamento = models.ForeignKey(Orcamentos, on_delete=models.PROTECT)
    nome_servico = models.CharField(max_length=45)
    relatorio = models.ForeignKey("Relatorio", on_delete=models.PROTECT)
    status_concluido = models.BooleanField(default=False)  
    funcionario = models.ForeignKey("Funcionario", on_delete=models.PROTECT)
    tipo_de_servico = models.IntegerField()
    aparelho_seguro = models.BooleanField(default=True)  
    data_inicio = models.DateField()

    def __str__(self):
        return f"{self.nome_servico}, ({self.descricao_servico})"


class Relatorio(models.Model):
    descricao_relatorio = models.CharField(max_length=45)
    dificuldade_servico = models.IntegerField()
    colaboracao_empresa = models.IntegerField()
    data_inicio = models.ForeignKey("Servico", on_delete=models.PROTECT)
    data_final_servico = models.DateField()
    pendencias_maquina = models.CharField(max_length=45)

    imagens_antes = models.ImageField(upload_to="imagens/antes/", blank=True, null=True)
    imagens_depois = models.ImageField(
        upload_to="imagens/antes/", blank=True, null=True
    )

    def __str__(self):
        return self.descricao_relatorio


class Image(models.Model):
    imagem = models.ImageField(
        upload_to="imagens/"
    )  # Ajuste o caminho conforme necessário

    def __str__(self):
        return f"Image {self.id}"


class Ferramentaspecas(models.Model):
    nome_ferramentaspecas = models.CharField(max_length=45)
    valor_ferramentaspecas = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Alterado para DecimalField
    quantidade_ferramentaspecas = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_ferramentaspecas


class Paralelismo(models.Model):
    superioresquerdo = models.CharField(max_length=5)
    superiordireito = models.CharField(max_length=5)
    inferioresquerdo = models.CharField(max_length=5)
    inferiordireito = models.CharField(max_length=5)

    def __str__(self):
        return self.superiordireito


class Funcionario(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.PROTECT, related_name="funcionario"
    )
    matricula = models.CharField(max_length=10)
    cargo = models.ForeignKey(
        Cargo, on_delete=models.PROTECT, related_name="funcionarios"
    )


class Administrador(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.PROTECT, related_name="administrador"
    )


class Chamado(models.Model):
    motivo = models.CharField(max_length=140)
    descricao = models.CharField(max_length=200)
    titulo = models.CharField(max_length=45)
    status = models.BooleanField(default=False)
    data_envio = models.DateField()
