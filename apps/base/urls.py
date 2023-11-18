from django.urls import path
from apps.base.views import settings

urlpatterns = [
    path('', settings, name="index"),
]