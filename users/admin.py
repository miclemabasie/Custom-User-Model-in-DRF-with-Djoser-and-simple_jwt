from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import ugettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.admin.sites import AdminSite


class UserAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "pkid",
        "username",
        "first_name",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    list_filter = [
        "username",
        "first_name",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    ]
    search_fields = ["username", "first_name", "last_name", "email"]
    odering = ("id",)
    filter_horizontal = ["groups", "user_permissions"]
    list_display_links = ["id", "email", "username"]
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (
            _("Personal Information"),
            {"fields": ("username", "first_name", "last_name")},
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": {"email", "password1", "password2", "is_staff", "is_active"},
            },
        ),
    )


admin.site.register(User, UserAdmin)

admin.site.site_header = "Custom User Creation in Django"
admin.site.site_title = "Custom User Creation in Django Portal"
