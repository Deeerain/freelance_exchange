from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_from', 'price_to', 'visible', 'created', 'updated')
    list_editable = ('price_from', 'price_to', 'visible')
    list_filter = ('visible', 'created', 'updated')
    prepopulated_fields = {'slug': ('title', 'employer')}

