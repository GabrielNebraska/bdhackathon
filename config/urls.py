from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from hackathon.views import CargoViewSet

path("api/media/", include(uploader_router.urls)), 

router = DefaultRouter()
router.register(r"Cargos", CargoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
