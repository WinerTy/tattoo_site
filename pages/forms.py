from django import forms
from database.models import Master

from site_setting.models import Salon
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AppointmentForm(forms.Form):
    client_email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "example@mail.ru"}
        ),
    )
    client_phone = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "+7 (123) 456-78-90",
            }
        ),
    )
    master = forms.ModelChoiceField(
        queryset=Master.objects.none(),
        label="",
        empty_label="Выберите мастера",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        salon_pk = kwargs.pop("salon_pk", None)
        super().__init__(*args, **kwargs)
        if salon_pk:
            self.fields["master"].queryset = Master.objects.filter(
                salon__pk=salon_pk, is_active=True
            )


class SelectSalonForm(forms.Form):
    salon = forms.ModelChoiceField(
        queryset=Salon.objects.all(),
        label="",
        empty_label="Выберите салон",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
