from django.conf import settings
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    registered_at = serializers.DateTimeField(
        format="%d/%m/%Y %H:%M:%S", read_only=True
    )

    avatar = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    short_name = serializers.SerializerMethodField(read_only=True)

    def get_avatar(self, obj):
        return (
            obj.avatar.url
            if obj.avatar
            else settings.STATIC_URL + "images/default_avatar.png"
        )

    def get_full_name(self, obj):
        return obj.full_name

    def get_short_name(self, obj):
        return obj.short_name

    class Meta:
        model = User
        fields = [
            "email",
            "avatar",
            "full_name",
            "short_name",
            "is_customer",
            "registered_at",
        ]


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "is_customer",
            "avatar",
        ]
