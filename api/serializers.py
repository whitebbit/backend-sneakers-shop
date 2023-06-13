from . import models
from rest_framework import serializers
from rest_framework import fields
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from . import models
from . import documents

class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sneaker
        fields = "__all__"


class SneakerDocumentSerializer(DocumentSerializer):
    class Meta:
        document = documents.SneakerDocument
        fields = ["name", "article", "color", "price", "brand"]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = ("value", )
