from django.db import models
from datetime import timedelta
from django.utils.text import slugify
from .utils import convert_to_work_minutes
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    total_time = models.DurationField(default=timedelta(seconds=0))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("tasks:detail", kwargs={"slug": self.slug})

    @property
    def time_in_work_minutes(self):
        tiwh = convert_to_work_minutes(self.total_time)
        return tiwh

    class Meta:
        ordering = ("-created",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
