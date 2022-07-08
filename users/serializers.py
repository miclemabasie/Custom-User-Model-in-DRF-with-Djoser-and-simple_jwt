from django.contrib.auth import get_user_model

# from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer

# from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(source="profile.photo")
    country = serializers.CharField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    # top_seller = serializers.BooleanField(source="profile.top_seller")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "profile_photo",
            "country",
            "city",
            # "top_seller",
        ]

    def get_full_name(self, obj):
        first_name = obj.first_name.title()
        last_name = obj.last_name.title()
        return f"{first_name} {last_name}"

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def to_representation(self, instance):
        represention = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            represention["admin"] = True

        return represention


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
