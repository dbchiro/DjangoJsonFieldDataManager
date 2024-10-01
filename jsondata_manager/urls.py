from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AllowedKeyViewSet

router = DefaultRouter()
router.register(r"allowed-keys", AllowedKeyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
