from django.urls import path
from . import views

urlpatterns = [
    path('', views.trending_outfits, name='trending_outfits'),
]