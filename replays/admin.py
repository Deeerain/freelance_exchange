from django.contrib import admin
from .models import Replay


@admin.register(Replay)
class ReplayAdmin(admin.ModelAdmin):
    list_display = ('task', 'user')