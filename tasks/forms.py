from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "type new task"}
        )
    )

    class Meta:
        model = Task
        fields = ("name",)
