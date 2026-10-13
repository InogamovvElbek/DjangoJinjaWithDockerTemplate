from django.contrib import admin

from apps.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "is_done", "created_at")
    list_filter = ("is_done",)
    search_fields = ("title", "description")
