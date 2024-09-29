from django.shortcuts import render
from .models import Outfit

def trending_outfits(request):
    outfits = Outfit.objects.filter(is_trending=True).order_by('-created_at')[:15]
    return render(request, 'trending_outfits.html', {'outfits': outfits})