from django.contrib import admin
from .models import Comment
from .models import Vote

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "idea", "content", "created_at")
    search_fields = ("content", "user__username", "idea__title")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "idea", "created_at")
    search_fields = ("user__username", "idea__title")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
