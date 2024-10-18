from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from hackathon.views import CargoViewSet

router = DefaultRouter()
router.register(r"Cargos", CargoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]