from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib import messages
from .utils import is_ajax
from django.http import JsonResponse
import json
from django.utils import timezone
from logs.models import Log
from django.db.models import Sum, Count, Min, Max, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# region FUNCIONS
@login_required
def manage_log_view(request, slug):
    if is_ajax(request):
        is_finish = json.loads(request.POST.get("is_finish"))
        is_work = (
            json.loads(request.POST.get("is_work"))
            if request.POST.get("is_work")
            else False
        )

        timestamp = timezone.now()
        task = get_object_or_404(Task, slug=slug)

        existing_log = Log.objects.filter(
            user=request.user, task=task, is_finished=False
        ).first()

        if existing_log and is_finish:
            existing_log.time_end = timestamp
            existing_log.is_finished = True
            existing_log.save()
            message = "log closed"
        else:
            message = "logged in on break" if not is_work else "logged in on work"

            Log.objects.create(
                user=request.user, task=task, time_start=timestamp, is_work=is_work
            )

        return JsonResponse({"message": message})
    return redirect("tasks:main")


@login_required
def get_timezone_view(request):
    if is_ajax(request):
        if request.user.timezone == "UTC":
            timezone = request.GET.get("timezone")
            user = request.user

            user.timezone = timezone
            user.save()
            return JsonResponse(
                {"msg": f"timezon has been updated to {timezone}", "is_changed": True}
            )
        return JsonResponse({"msg": "timezone has already been updated by the user"})
    return JsonResponse({"msg": "access denied"})


@login_required
def task_summary_view(request, slug):
    task = get_object_or_404(Task, slug=slug)
    logs = Log.objects.filter(task__slug=slug).values("task")
    task_summary = (
        logs.annotate(total_time=Sum("time"))
        .annotate(total_work_time=Sum("time", filter=Q(is_work=True)))
        .annotate(total_none_work_time=Sum("time", filter=Q(is_work=False)))
        .annotate(log_count=Count("id"))
        .annotate(shortest_log=Min("time"))
        .annotate(longest_log=Max("time"))
    )
    print(task_summary)

    context = {"task": task, "qs": task_summary}

    return render(request, "tasks/summary.html", context)


# endregion


# region CLASS BASED VIEWS
class TaskListView(LoginRequiredMixin, CreateView, ListView):
    model = Task
    template_name = "tasks/main.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:main")

    def get(self, request, *args, **kwargs):
        request.session["user_timezone"] = request.user.timezone
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, "New task added")
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks:main")

    def form_valid(self, form):
        instance = self.get_object()
        messages.add_message(
            self.request,
            messages.INFO,
            f'Task "{instance.name }" was succesfully deleted',
        )
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"


class TaskLogHistoryView(LoginRequiredMixin, ListView):
    template_name = "tasks/history.html"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        task = get_object_or_404(Task, slug=slug)
        return Log.objects.filter(task=task)


# endregion
