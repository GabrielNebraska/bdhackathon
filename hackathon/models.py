from django.core.exceptions import ValidationError
from django.db import models 
from uploader.models import Image

def only_numbers(value): 
    if value.isdigit()==False:
        raise ValidationError('Este campo deve conter apenas números')

class Cargo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=350, null=False)
    email = models.EmailField(null=False, blank=False)
    senha = models.CharField(max_length=128)  # Aumentei o tamanho para armazenar hashes
    telefone = models.CharField(
        validators=[only_numbers],
        max_length=11
    )

    def __str__(self):
        return f"{self.nome}"
    
class Cliente (models.Model):
    nome_cliente = models.CharField(max_length=45)
    cnpj_cliente = models.CharField(max_length=14)
    endereco_cliente = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_cliente
    
class Orcamentos(models.Model):
    descricao_orcamento = models.CharField(max_length=45)
    datasolicitada_orcamento = models.DateField(auto_now_add=True)
    valor_orcamento = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tipo_orcamento = models.CharField(max_length=45, null=True)
    endereco_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="cliente")


    def __str__(self):
        return self.descricao_orcamento


class Servico(models.Model):
    descricao_servico = models.CharField(max_length=45)
    tempo_Servico = models.TimeField()
    orcamento_idorcamentos = models.IntegerField()
    orcamentos_cliente_cnpjcliente = models.CharField(max_length=14)
    orcamentos_cliente_idcliente = models.CharField(max_length=14)
    nome_servico = models.CharField(max_length=45)
    relatorio_id_relatorio = models.IntegerField()
    relatorio_verificacoespreventivas_idverificacoespreventivas = models.IntegerField()
#tem que botar as imagens antes e depois do servico
    def __str__(self):
        return f"{self.nome_servico}, ({self.descricao_servico})" 

class Verificacoespreventivas(models.Model):
    paralelismo_idparalelismo = models.IntegerField()
    estiramento_idestiramento = models.IntegerField()
    limpezaequipamentos_verificacoespreventivas = models.IntegerField()
    testesdemovimento_verificacoespreventivas = models.IntegerField()
    seguranca_verificacoespreventivas = models.IntegerField()
    funcionamentoalimentador_verificacoespreventivas = models.IntegerField()
    funcionamentomanipulador_verificacoespreventivas = models.IntegerField()
    ruidoaparelho_verificacoespreventivas = models.IntegerField()
    aquecimentoconformeprog_verificacoespreventivas = models.IntegerField()
    
    def __str__ (self):
        return str(self.seguranca_verificacoespreventivas)
   

class Relatorio(models.Model):
    descricao_relatorio = models.CharField(max_length=45)
    dificuldadeservico_relatorio = models.IntegerField()
    colaboracaodaempresa_relatorio = models.IntegerField()
    datainicialservico_relatorio = models.DateField()
    datafinalservico_relatorio = models.DateField()
    pendenciasmaquina_relatorio = models.CharField(max_length=45)
    Verificacoespreventivas_idverificacoespreventivas = models.ForeignKey(Verificacoespreventivas, on_delete=models.PROTECT, related_name="IDverificacoespreventivas")
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
#ainda tem que ser incluido o "verificacoespreventivas_idverificacoespreventivas" e "imagens do servico"/"imagens depois do servico"
    def __str__(self):
        return self.descricao_relatorio

class Image(models.Model):
    imagem = models.ImageField(upload_to='imagens/')  # Ajuste o caminho conforme necessário

    def __str__(self):
        return f"Image {self.id}"


class Estoque(models.Model):
    endereco_estoque = models.CharField(max_length=45)

    def __str__ (self):
        return self.endereco_estoque
    
class Ferramentaspecas(models.Model):
    nome_ferramentaspecas = models.CharField(max_length=45)
    valor_ferramentaspecas = models.CharField(max_length=5)
    quantidade_ferramentaspecas = models.CharField(max_length=45)

    def __str__ (self):
        return self.nome_ferramentaspecas
    
 
class Paralelismo (models.Model):
    superioresquerdo_paralelismo = models.CharField(max_length=5)
    superiordireito_paralelismo = models.CharField(max_length=5)
    inferioresquerdo_paralelismo = models.CharField(max_length=5)
    inferiordireito_paralelismo = models.CharField(max_length=5)

    def __str__ (self):
        return self.superiordireito_paralelismo

class Funcionario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, related_name="funcionario")
    # Adicione outros campos específicos para o funcionário aqui, se necessário

    matricula = models.CharField(max_length=10)
    cargo = models.ForeignKey(
        Cargo, on_delete=models.PROTECT, related_name="funcionarios"
    )

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, related_name="administrador")
    