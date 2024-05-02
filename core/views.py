from django.http import HttpResponse
from django.shortcuts import render
import pytz
from django.utils import timezone
from datetime import datetime


def experiment_view(request):
    tz = timezone.get_current_timezone()
    timezones = pytz.all_timezones
    dt = datetime.now()
    dt = datetime.now(tz)
    print("timezones ", timezones)
    print("current timezone ", tz)
    print("dt ", dt)
    print("datetime UTC", datetime.utcnow())

    return render(request, "main.html", {"tz": tz})
