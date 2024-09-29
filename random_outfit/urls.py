from django.urls import path
from .views import RandomView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RandomView.as_view(), name='random'),
]

