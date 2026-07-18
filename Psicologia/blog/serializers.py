from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Articulo


class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )


class ArticuloSerializer(serializers.ModelSerializer):

    autor = serializers.ReadOnlyField(
        source="autor.username"
    )

    class Meta:
        model = Articulo
        fields = "__all__"