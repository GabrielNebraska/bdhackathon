from rest_framework.serializers import ModelSerializer

from hackathon.models import Chamado, Cargo, Usuario, Cliente, Orcamentos, Servico, Relatorio, Ferramentaspecas, Paralelismo, Funcionario, Administrador

class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = "__all__"
        
class ChamadoSerializer(ModelSerializer):
    class Meta:
        model = Chamado
        fields = "__all__"

class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class OrcamentosSerializer(ModelSerializer):
    class Meta:
        model = Orcamentos
        fields = "__all__"        


class RelatorioSerializer(ModelSerializer):
    class Meta:
        model = Relatorio
        fields = "__all__"



class FerramentaspecasSerializer(ModelSerializer):
    class Meta:
        model = Ferramentaspecas
        fields = "__all__"

class ParalelismoSerializer(ModelSerializer):
    class Meta:
        model = Paralelismo
        fields = "__all__"


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = "__all__"


class AdministradorSerializer(ModelSerializer):
    class Meta:
        model = Administrador
        fields = "__all__"
