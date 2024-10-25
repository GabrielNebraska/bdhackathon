from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from hackathon.models import Cargo
from hackathon.serializers import CargoSerializer

class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Relatorio, Image


#tudo a partir daqui fiz com auxílio de IA, portanto pode estar errado. precisa ser revisado*
def upload_relatorio(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        dificuldadeservico = request.POST.get('dificuldadeservico')
        colaboracao = request.POST.get('colaboracao')
        datainicial = request.POST.get('datainicial')
        datafinal = request.POST.get('datafinal')
        pendencias = request.POST.get('pendencias')

        relatorio = Relatorio(
            descricao_relatorio=descricao,
            dificuldadeservico_relatorio=dificuldadeservico,
            colaboracaodaempresa_relatorio=colaboracao,
            datainicialservico_relatorio=datainicial,
            datafinalservico_relatorio=datafinal,
            pendenciasmaquina_relatorio=pendencias
        )

        # Salva o relatório antes de adicionar as imagens
        relatorio.save()

        # Processa as imagens antes do serviço
        if 'imagens_antes' in request.FILES.getlist('imagens_antes'):
            for imagem_file in request.FILES.getlist('imagens_antes'):
                imagem = Image(imagem=imagem_file)
                try:
                    imagem.full_clean()  # Valida a imagem
                    imagem.save()
                    relatorio.imagens_antes.add(imagem)  # Adiciona a imagem ao relatorio
                except ValidationError as e:
                    messages.error(request, str(e))

        # Processa as imagens depois do serviço
        if 'imagens_depois' in request.FILES.getlist('imagens_depois'):
            for imagem_file in request.FILES.getlist('imagens_depois'):
                imagem = Image(imagem=imagem_file)
                try:
                    imagem.full_clean()  # Valida a imagem
                    imagem.save()
                    relatorio.imagens_depois.add(imagem)  # Adiciona a imagem ao relatorio
                except ValidationError as e:
                    messages.error(request, str(e))

        messages.success(request, 'Relatório enviado com sucesso!')
        return redirect('sua_view')

    return render(request, 'upload_relatorio.html')
