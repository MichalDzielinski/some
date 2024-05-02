from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Additional Info", {"fields": ("timezone",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
