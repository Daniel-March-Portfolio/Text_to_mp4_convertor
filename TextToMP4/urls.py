from django.urls import path
from TextToMP4.views import index

urlpatterns = [
    path("", index),
]
