from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
import djoser

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/v1/profiles/", include("profiles.urls", namespace="profiles")),
    path("api/v1/auth/", include("djoser.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/authbasic/", views.obtain_auth_token),
]
