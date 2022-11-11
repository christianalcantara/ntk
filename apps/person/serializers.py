from rest_framework import serializers

from .models import Person
from ..car.serializers import CarSerializer


class PersonSerializer(serializers.ModelSerializer):
    """Person models serializer"""

    cars = CarSerializer(many=True, read_only=True)
    sale_opportunity = serializers.SerializerMethodField(
        method_name="calculate_is_sale_opportunity"
    )

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "email",
            "sale_opportunity",
            "cars",
            "created",
            "modified",
        ]

    @staticmethod
    def calculate_is_sale_opportunity(instance):
        return instance.sale_opportunity
