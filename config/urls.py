from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from django.contrib import admin
from django.urls import include, path

from rest_framework_swagger import schema_view
from rest_framework.routers import DefaultRouter
from hackathon.views import CargoViewSet, UsuarioViewSet, ClienteViewSet, OrcamentosViewSet, ServicoViewSet, VerificacoespreventivasViewSet, RelatorioViewSet, EstoqueViewSet, FerramentaspecasViewSet, ParalelismoViewSet, FuncionarioViewSet, AdministradorViewSet

path("api/media/", include(uploader_router.urls)), 

router = DefaultRouter()
router.register(r"cargos", CargoViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"orcamentoss", OrcamentosViewSet)
router.register(r"servicos", ServicoViewSet)
router.register(r"verificacoespreventivas", VerificacoespreventivasViewSet)
router.register(r"relatorios", RelatorioViewSet)
router.register(r"estoques", EstoqueViewSet)
router.register(r"ferramentaspecas", FerramentaspecasViewSet)
router.register(r"paralelismos", ParalelismoViewSet)
router.register(r"funcionarios", FuncionarioViewSet)
router.register(r"administradores", AdministradorViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
