from django.contrib import admin

from .models import Chump, ChumpMedia, SpecialEvent, Era


class ChumpMediaAdmin(admin.ModelAdmin):
    list_display = ("chump", "media")


class ChumpMediaInline(admin.TabularInline):
    model = ChumpMedia
    extra = 1


class ChumpAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date")
    inlines = [ChumpMediaInline]


admin.site.register(Chump, ChumpAdmin)
admin.site.register(ChumpMedia, ChumpMediaAdmin)
admin.site.register(SpecialEvent)
admin.site.register(Era)
