from django.db import models
from django.contrib.auth.models import AbstractUser
import pytz


class CustomUser(AbstractUser):
    timezone = models.CharField(
        max_length=63, choices=[(tz, tz) for tz in pytz.all_timezones], default="UTC"
    )
