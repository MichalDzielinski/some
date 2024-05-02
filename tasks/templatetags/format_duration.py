from django import template


register = template.Library()


@register.filter
def format_duration(val):
    f_duration = str(val).split(".")[0]
    return f_duration
