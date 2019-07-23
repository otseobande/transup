from rest_framework import viewsets
from providers.models import Provider
from providers.serializers import ProviderSerializer
from rest_framework import permissions

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny]
