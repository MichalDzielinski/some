from django.urls import path
from .views import TimezoneSelectView

app_name = "users"

urlpatterns = [
    path("tz/", TimezoneSelectView.as_view(), name="tz"),
]
