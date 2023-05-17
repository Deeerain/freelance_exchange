from django.contrib import admin

from .models import User, Role


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
