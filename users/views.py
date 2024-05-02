from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from .forms import TimezoneForm
from django.contrib import messages

User = get_user_model()


class TimezoneSelectView(FormView):
    template_name = "users/select_tz.html"
    form_class = TimezoneForm

    def get_success_url(self):
        return self.request.path

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = User.objects.get(pk=self.request.user.pk)
        return kwargs

    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.pk)
        selected_timezone = form.cleaned_data["selected_timezone"]
        user.timezone = selected_timezone
        self.request.session["user_timezone"] = selected_timezone
        user.save()
        messages.add_message(self.request, messages.INFO, "Timezon updated")
        return super().form_valid(form)
