from django.contrib import admin
from .models import Update

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("id", "idea", "user", "state", "created_at")
    list_filter = ("state", "created_at")
    search_fields = ("idea__title", "user__username", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
