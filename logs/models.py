from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser
from tasks.models import Task
from django.utils import timezone


class Log(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time_start = models.DateTimeField(default=timezone.now)
    time_end = models.DateTimeField(blank=True, null=True)
    time = models.DurationField(blank=True, null=True)
    is_work = models.BooleanField(default=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} logged in on {self.task.name}"

    @property
    def formatted_time(self):
        f_duration = str(self.time).split(".")[0]
        return f_duration

    class Meta:
        ordering = ("-time_start",)
