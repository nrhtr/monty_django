from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ("name", "published", "email", "location", "message")


admin.site.register(Entry, EntryAdmin)
