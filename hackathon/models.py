from django.core.exceptions import ValidationError
from django.db import models 


def only_numbers(value): 
    if value.isdigit()==False:
        raise ValidationError('Este campo deve conter apenas números')

class Cliente (models.Model):
    nome_cliente = models.CharField(45)
    cnpj_cliente = models.CharField(14)
    endereco_cliente = models.CharField(45)

    def __str__(self):
        return self.nome_cliente
    
class Orcamentos(models.Model):
    descricao_orcamento = models.CharField(45)
    cnpj_cliente = models.CharField(14)
    endereco_cliente = models.CharField(45)
    cliente = models.ManyToManyField(Cliente, related_name="Orcamentos")

    def __str__(self):
        return f"{self.descricao_orcamento} ({self.cnpj_cliente})"


class Servico(models.Model):
    descricao_servico = models.CharField(45)
    tempo_Servico = models.TimeField
    orcamento_idorcamentos = models.IntegerField
    orcamentos_cliente_cnpjcliente = models.CharField(14)
    orcamentos_cliente_idcliente = models.CharField(14)
    nome_servico = models.CharField(45)
    relatorio_id_relatorio = models.IntegerField
    relatorio_verificacoespreventivas_idverificacoespreventivas = models.IntegerField
#tem que botar as imagens antes e depois do servico
    def __str__(self):
        return f"{self.nome_servico}, ({self.descricao_servico})" 


class Relatorio(models.Model):
    descricao_relatorio = models.CharField
    dificuldadeservico_relatorio = models.IntegerField
    colaboracaodaempresa_relatorio = models.IntegerField
    datainicialservico_relatorio = models.DateField
    datafinalservico_relatorio = models.DateField
    pendenciasmaquina_relatorio = models.CharField(45)

#ainda tem que ser incluido o "verificacoespreventivas_idverificacoespreventivas" e "imagens do servico"/"imagens depois do servico"





class Estoque(models.Model):
    endereco_estoque = models.CharField(45)

    def __str__ (self):
        return self.endereco_estoque
    
class Ferramentaspecas(models.Model):
    nome_ferramentaspecas = models.CharField(45)
    valor_ferramentaspecas = models.CharField(5)
    quantidade_ferramentaspecas = models.CharField(45)

    def __str__ (self):
        return self.nome_ferramentaspecas
    
class Verificacoespreventivas (models.Model):
    paralelismo_idparalelismo = models.IntegerField
    estiramento_idestiramento = models.IntegerField
    limpezaequipamentos_verificacoespreventivas = models.IntegerField
    testesdemovimento_verificacoespreventivas = models.IntegerField
    seguranca_verificacoespreventivas = models.IntegerField
    funcionamentoalimentador_verificacoespreventivas = models.IntegerField
    funcionamentomanipulador_verificacoespreventivas = models.IntegerField
    ruidoaparelho_verificacoespreventivas = models.IntegerField
    aquecimentoconformeprog_verificacoespreventivas = models.IntegerField



    def __str__ (self):
        return self.seguranca_verificacoespreventivas
    
class Paralelismo (models.Model):
    superioresquerdo_paralelismo = models.CharField(5)
    superiordireito_paralelismo = models.CharField(5)
    inferioresquerdo_paralelismo = models.CharField(5)
    inferiordireito_paralelismo = models.CharField(5)

    def __str__ (self):
        return self.superiordireito_paralelismo

class Cargo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class usuario(models.Model):

    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    endereco = models.CharField(max_length=350, null=False )
    email = models.EmailField(null=False, blank=False)
    senha = models.CharField(max_length=20, null=False, blank=False)
    telefone = models.CharField(validators=[only_numbers], max_length=11)
    cargo = models.ForeignKey(
        Cargo, on_delete=models.PROTECT, related_name="funcionarios"
    )

    def __str__(self):
        return f"{self.nome} ({self.matricula})"