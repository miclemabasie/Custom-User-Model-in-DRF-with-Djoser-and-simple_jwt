from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [path("", views.ListProfileAPIView.as_view(), name="profile_list")]
