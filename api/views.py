from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from django_elasticsearch_dsl_drf.filter_backends import CompoundSearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from .utils import cache_utils, logging
from . import documents

class SneakerViewSet(viewsets.ModelViewSet):
    queryset = models.Sneaker.objects.all()
    serializer_class = serializers.SneakerSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = cache_utils.make_cache(
            "sneaker_cache", response.data, 30 * 60)
        response.data = self.set_sizes(response.data)
        
        return response

    def retrieve(self, request, pk, *args, **kwargs):
        response = super().retrieve(request, pk, * args, **kwargs)

        response.data = cache_utils.make_cache(
            f"{response.data['id']}_sneaker_cache", response.data, 10 * 60)

        response.data = self.set_sizes(response.data)

        return response

    def set_sizes(self, response_data):
        size_objects_cache = cache_utils.make_cache(
            "size_objects_cache", models.Size.objects, 60 * 60)

        if isinstance(response_data, list):
            for item in response_data:
                sizes = [str(i) for i in item["sizes"]]
                item["sizes"] = [int(str(size_objects_cache.get(id=i)))
                                 for i in sizes]
        else:
            sizes = [str(i) for i in response_data["sizes"]]
            response_data["sizes"] = [int(str(size_objects_cache.get(id=i)))
                                      for i in sizes]
        return response_data

class SneakerDocumentViewSet(DocumentViewSet):
    document = documents.SneakerDocument
    serializer_class = serializers.SneakerDocumentSerializer
    
    filter_backends = [CompoundSearchFilterBackend]
    search_fields = ["name", "article", "color", "price", "brand"]
    filter_fields = {
        "name": "name"
    }    

class SizeViewSet(viewsets.ModelViewSet):
    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        response.data = cache_utils.make_cache(
            "size_cache", response.data, 60 * 60)
        return response