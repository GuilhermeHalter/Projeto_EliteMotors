from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from elitemotors.views import CarroViewSet, CorViewSet, AcessorioViewSet

router = DefaultRouter()
router.register(r"carros", CarroViewSet)
router.register(r"cores", CorViewSet)
router.register(r"acessorios", AcessorioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
