from django.contrib import admin

# Register your models here.
from .models import Cargo, Usuario, Cliente, Orcamentos, Servico, Relatorio, Ferramentaspecas, Paralelismo, Funcionario, Administrador, Chamado

admin.site.register(Chamado)
admin.site.register(Cargo)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Orcamentos)
admin.site.register(Servico)
admin.site.register(Relatorio)
admin.site.register(Ferramentaspecas)
admin.site.register(Paralelismo)
admin.site.register(Funcionario)
admin.site.register(Administrador)