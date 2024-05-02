from django.urls import path
from .views import (
    TaskListView,
    TaskDeleteView,
    get_timezone_view,
    TaskDetailView,
    manage_log_view,
    TaskLogHistoryView,
    task_summary_view,
)

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="main"),
    path("detect-tz/", get_timezone_view, name="detect-tz"),
    path("<slug>/", TaskDetailView.as_view(), name="detail"),
    path("<slug>/log/", manage_log_view, name="log"),
    path("<slug>/summary/", task_summary_view, name="summary"),
    path("<slug>/history/", TaskLogHistoryView.as_view(), name="history"),
    path("<slug>/delete/", TaskDeleteView.as_view(), name="delete"),
]
