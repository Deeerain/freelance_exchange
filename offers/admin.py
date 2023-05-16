from django.contrib import admin
from .models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('executor', 'task', 'state', 'created', 'updated')
    list_editable = ('state',)