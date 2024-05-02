from django.contrib import admin
from .models import Task
from logs.models import Log


class LogInline(admin.TabularInline):
    model = Log
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug", "total_time"]
    inlines = [LogInline]


admin.site.register(Task, TaskAdmin)
