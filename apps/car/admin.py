from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "color")
    list_filter = ("model", "color")
    search_fields = ("name",)
