from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from hackathon.models import Cargo, Usuario, Cliente, Orcamentos, Servico, Verificacoespreventivas, Relatorio, Estoque, Ferramentaspecas, Paralelismo, Funcionario, Administrador

from hackathon.serializers import CargoSerializer, UsuarioSerializer, ClienteSerializer, OrcamentosSerializer, ServicoSerializer, VerificacoespreventivasSerializer, RelatorioSerializer, EstoqueSerializer, FerramentaspecasSerializer, ParalelismoSerializer, FuncionarioSerializer, AdministradorSerializer

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

class VerificacoespreventivasViewSet(ModelViewSet):
    queryset = Verificacoespreventivas.objects.all()
    serializer_class = VerificacoespreventivasSerializer

class RelatorioViewSet(ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

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
