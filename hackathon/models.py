from django.core.exceptions import ValidationError
from django.db import models 
from uploader.models import Image

def only_numbers(value): 
    if not value.isdigit():
        raise ValidationError('Este campo deve conter apenas números')

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
    endereco_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="cliente")

    def __str__(self):
        return self.descricao_orcamento

class Servico(models.Model):
    descricao_servico = models.CharField(max_length=45)
    cliente = models.OneToOneField(Cliente, on_delete=models.PROTECT, related_name="Cliente")
    orcamento = models.ForeignKey(Orcamentos, on_delete=models.PROTECT)
    nome_servico = models.CharField(max_length=45)
    relatorio = models.ForeignKey('Relatorio', on_delete=models.PROTECT)
    status_concluido = models.BooleanField(default=False)  # Alterado para BooleanField
    funcionario = models.ForeignKey('Funcionario', on_delete=models.PROTECT)
    tipo_de_servico = models.IntegerField()
    aparelho_seguro = models.BooleanField(default=True)  # Novo campo

    def __str__(self):
        return f"{self.nome_servico}, ({self.descricao_servico})"

class Verificacoespreventivas(models.Model):
    paralelismo = models.IntegerField()
    estiramento = models.IntegerField()
    limpeza_equipamentos = models.IntegerField()
    testes_movimento = models.IntegerField()
    seguranca = models.IntegerField()
    funcionamento_alimentador = models.IntegerField()
    funcionamento_manipulador = models.IntegerField()
    ruido_aparelho = models.IntegerField()
    aquecimento_conforme_prog = models.IntegerField()
    
    def __str__(self):
        return str(self.seguranca)

class Relatorio(models.Model):
    descricao_relatorio = models.CharField(max_length=45)
    dificuldade_servico = models.IntegerField()
    colaboracao_empresa = models.IntegerField()
    data_inicial_servico = models.DateField()
    data_final_servico = models.DateField()
    pendencias_maquina = models.CharField(max_length=45)
    verificacoes_preventivas = models.ForeignKey(Verificacoespreventivas, on_delete=models.PROTECT, related_name="IDverificacoespreventivas")
    # imagens_antes = models.ManyToManyField(
    #     Image,
    #     related_name="relatorios_antes",
    #     blank=True
    # )
    # imagens_depois = models.ManyToManyField(
    #     Image,
    #     related_name="relatorios_depois",
    #     blank=True
    # )
    def __str__(self):
        return self.descricao_relatorio

class Image(models.Model):
    imagem = models.ImageField(upload_to='imagens/')  # Ajuste o caminho conforme necessário

    def __str__(self):
        return f"Image {self.id}"

class Estoque(models.Model):
    endereco_estoque = models.CharField(max_length=45)

    def __str__(self):
        return self.endereco_estoque
    
class Ferramentaspecas(models.Model):
    nome_ferramentaspecas = models.CharField(max_length=45)
    valor_ferramentaspecas = models.DecimalField(max_digits=10, decimal_places=2)  # Alterado para DecimalField
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
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, related_name="funcionario")
    matricula = models.CharField(max_length=10)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name="funcionarios")

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, related_name="administrador")