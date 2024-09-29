# admin.py

from django.contrib import admin
from .models import Outfit

class OutfitAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_trending', 'created_at']
    list_filter = ['is_trending', 'created_at']
    search_fields = ['name', 'description']

admin.site.register(Outfit, OutfitAdmin)
