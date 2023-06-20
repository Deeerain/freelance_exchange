from django.contrib import admin
from replays.models import Replay


@admin.register(Replay)
class ReplayAdmin(admin.ModelAdmin):
    list_display = ('task', 'user')