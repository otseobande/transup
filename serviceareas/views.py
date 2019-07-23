from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.gis.geos import Polygon
from rest_framework.schemas import AutoSchema
import coreapi

# Create your views here.
from rest_framework import viewsets, status
from serviceareas.models import ServiceArea
from serviceareas.serializers import ServiceAreaSerializer
from rest_framework import permissions


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [permissions.AllowAny]
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("latitude",
            required=False,
            location='query',
            description='Location latitude'),
        ]
    )

    def get_queryset(self):
        """
        Filter using latitude and longitude
        """
        longitude = self.request.query_params.get('longitude', None)
        latitude = self.request.query_params.get('latitude', None)

        queryset = self.queryset
        if longitude and latitude:
            queryset = queryset.filter(coordinates__contains=[latitude, longitude])
        elif latitude:
            queryset = queryset.filter(coordinates__contains=[latitude])
        elif longitude:
            queryset = queryset.filter(coordinates__contains=[longitude])

        return queryset
