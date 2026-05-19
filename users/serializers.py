from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "first_name", "last_name", "is_staff")
        extra_kwargs = {
            "password": {"write_only": True},
            "is_staff": {"read_only": True}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

