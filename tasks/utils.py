def is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


def convert_to_work_minutes(duration):
    total_seconds = duration.total_seconds()
    minutes, remainder = divmod(total_seconds, 60)

    total_minutes = minutes + round(remainder / 60, 2)
    return total_minutes
