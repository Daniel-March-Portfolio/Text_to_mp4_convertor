from django.contrib import admin

from TextToMP4.models import TextToMP4Requests


class TextToMP4RequestsAdmin(admin.ModelAdmin):
    list_display = ["text"]


admin.site.register(TextToMP4Requests, TextToMP4RequestsAdmin)
