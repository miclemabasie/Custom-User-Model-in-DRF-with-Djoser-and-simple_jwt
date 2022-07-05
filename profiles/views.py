from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Profile
from .serializers import ProfileListSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ListProfileAPIView(ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()
