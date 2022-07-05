from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "country",
        "city",
        "is_married",
        "proffession",
        "date_created",
        "date_updated",
    ]
    list_display_links = ["user", "id", "country"]

    search_fields = ["username", "location"]

    list_filter = ["is_married", "country", "city", "user"]


admin.site.register(Profile, ProfileAdmin)
