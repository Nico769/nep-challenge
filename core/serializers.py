from rest_framework import serializers

from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("id", "title", "content")
        read_only_fields = ("id",)
