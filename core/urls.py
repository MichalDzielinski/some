from django.contrib import admin
from django.urls import path, include
from .views import experiment_view
from users import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", experiment_view, name='home'),
    path("", include("tasks.urls", namespace="tasks")),
    path("users/", include("users.urls", namespace="users")),
]
