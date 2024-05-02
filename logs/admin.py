from django.contrib import admin
from .models import Log
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
import pytz


class LogResource(resources.ModelResource):
    user = Field()
    task = Field()
    time_start = Field()
    time_end = Field()

    class Meta:
        model = Log
        fields = ("id", "user", "task", "time_start", "time_end", "time")
        export_order = ("id", "user", "task", "time_start", "time_end", "time")

    def dehydrate_user(self, obj):
        return obj.user.username

    def dehydrate_task(self, obj):
        return obj.task.name

    def dehydrate_time_start(self, obj):
        tz = pytz.timezone(obj.user.timezone)
        time_start_tz = obj.time_start.astimezone(tz)
        return time_start_tz

    def dehydrate_time_end(self, obj):
        tz = pytz.timezone(obj.user.timezone)
        time_end_tz = obj.time_end.astimezone(tz)
        return time_end_tz


class LogAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = LogResource


admin.site.register(Log, LogAdmin)
