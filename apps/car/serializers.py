from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """Car models serializer"""

    class Meta:
        model = Car
        fields = ["id", "name", "model", "color", "person", "created", "modified"]

        extra_kwargs = {"url": {"view_name": "api:car-detail", "lookup_field": "id"}}
