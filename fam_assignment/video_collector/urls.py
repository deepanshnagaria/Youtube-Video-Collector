from django.urls import path

from .views import Videos

urlpatterns = [
    path("", Videos.as_view(), name="Video_listing"),
]