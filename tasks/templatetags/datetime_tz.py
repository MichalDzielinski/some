from django import template
import pytz
from datetime import datetime

register = template.Library()


@register.filter
def datetime_tz(val, user):
    if isinstance(val, datetime):
        tz = pytz.timezone(user.timezone)
        converted_dt = val.astimezone(tz)
        formatted_dt = converted_dt.strftime("%b. %d, %Y, %I:%M:%p")
        return formatted_dt
    return ""
