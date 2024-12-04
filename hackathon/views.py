from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from hackathon.models import Chamado, Cargo, Usuario, Cliente, Orcamentos, Servico, Relatorio, Ferramentaspecas, Paralelismo, Funcionario, Administrador

from hackathon.serializers import ChamadoSerializer, CargoSerializer, UsuarioSerializer, ClienteSerializer, OrcamentosSerializer, ServicoSerializer, RelatorioSerializer, FerramentaspecasSerializer, ParalelismoSerializer, FuncionarioSerializer, AdministradorSerializer

class ChamadoViewSet(ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class OrcamentosViewSet(ModelViewSet):
    queryset = Orcamentos.objects.all()
    serializer_class = OrcamentosSerializer

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class RelatorioViewSet(ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

class FerramentaspecasViewSet(ModelViewSet):
    queryset = Ferramentaspecas.objects.all()
    serializer_class = FerramentaspecasSerializer

class ParalelismoViewSet(ModelViewSet):
    queryset = Paralelismo.objects.all()
    serializer_class = ParalelismoSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class AdministradorViewSet(ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Relatorio, Image
