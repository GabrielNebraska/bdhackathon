from django.contrib import admin

# Register your models here.
from .models import Cargo, Usuario, Cliente, Orcamentos, Servico, Verificacoespreventivas, Relatorio, Estoque, Ferramentaspecas, Paralelismo, Funcionario, Administrador

admin.site.register(Cargo)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Orcamentos)
admin.site.register(Servico)
admin.site.register(Verificacoespreventivas)
admin.site.register(Relatorio)
admin.site.register(Estoque)
admin.site.register(Ferramentaspecas)
admin.site.register(Paralelismo)
admin.site.register(Funcionario)
admin.site.register(Administrador)