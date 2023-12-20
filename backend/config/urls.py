from django.contrib import admin
from django.urls import path, include
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from uploader.router import router as uploader_router

from elitemotors.views import CarroViewSet, CorViewSet, AcessorioViewSet

router = DefaultRouter()
router.register(r"carros", CarroViewSet)
router.register(r"cores", CorViewSet)
router.register(r"acessorios", AcessorioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
