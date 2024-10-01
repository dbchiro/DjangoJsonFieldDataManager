from rest_framework import viewsets

from .models import AllowedKey
from .serializers import AllowedKeySerializer


class AllowedKeyViewSet(viewsets.ModelViewSet):
    queryset = AllowedKey.objects.all()
    serializer_class = AllowedKeySerializer
