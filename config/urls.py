from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#from django.contrib import admin
#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from hackathon.views import (
    ChamadoViewSet, CargoViewSet, UsuarioViewSet, ClienteViewSet,
    OrcamentosViewSet, ServicoViewSet, RelatorioViewSet,
    FerramentaspecasViewSet, ParalelismoViewSet, FuncionarioViewSet
)


from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

from hackathon.views import (
    CargoViewSet,
    UsuarioViewSet,
    ClienteViewSet,
    OrcamentosViewSet,
    ServicoViewSet,
    RelatorioViewSet,
    FerramentaspecasViewSet,
    ParalelismoViewSet,
    FuncionarioViewSet,
    AdministradorViewSet,
)


router = DefaultRouter()
router.register(r"cargos", CargoViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"orcamentoss", OrcamentosViewSet)
router.register(r"servicos", ServicoViewSet)
router.register(r"relatorios", RelatorioViewSet)
router.register(r"ferramentaspecas", FerramentaspecasViewSet)
router.register(r"paralelismos", ParalelismoViewSet)
router.register(r"funcionarios", FuncionarioViewSet)
router.register(r"administradores", AdministradorViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        default_version="v1",
        description="Test API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
