from django.contrib import admin
from .models import Outfit

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('name', 'outfit_type', 'main_color', 'color_one', 'color_two')
    search_fields = ('name', 'outfit_type', 'main_color', 'color_one', 'color_two')