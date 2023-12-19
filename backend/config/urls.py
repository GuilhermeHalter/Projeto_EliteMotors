from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from elitemotors.views import CarroViewSet

router = DefaultRouter()
router.register(r"carros", CarroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
