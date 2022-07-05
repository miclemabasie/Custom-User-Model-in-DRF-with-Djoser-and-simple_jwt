from rest_framework import serializers
from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.CharField(source="user.email")
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "country",
            "city",
            "photo",
            "is_married",
            "proffession",
            "date_created",
        ]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["country", "city", "photo", "is_married", "proffession"]
