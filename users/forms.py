from django import forms
import pytz


class TimezoneForm(forms.Form):
    timezones = [(tz, tz) for tz in pytz.all_timezones]
    selected_timezone = forms.ChoiceField(
        choices=timezones,
        widget=forms.Select(
            attrs={"class": "form-select bg-secondary border-dark text-white"}
        ),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["selected_timezone"].initial = user.timezone
