from django import forms
from database.models import Master, Appointment, TattooType
from site_setting.models import Salon


class AppointmentForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(
        queryset=TattooType.objects.all(),
        widget=forms.SelectMultiple(attrs={"size": 3, "class": "form-control"}),
        label="Типы тату",
        required=False,
    )

    class Meta:
        model = Appointment
        fields = [
            "client_email",
            "client_phone",
            "client_name",
            "types",
            "master",
        ]
        labels = {
            "client_email": "",
            "client_phone": "",
            "master": "",
            "types": "Типы",
        }
        widgets = {
            "client_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "example@mail.ru"}
            ),
            "client_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "+7 (123) 456-78-90"}
            ),
            "master": forms.Select(attrs={"class": "form-control"}),
            "client_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Имя"}
            ),
        }

    def __init__(self, *args, **kwargs):
        salon_pk = kwargs.pop("salon_pk", None)
        super().__init__(*args, **kwargs)
        if salon_pk:
            self.fields["master"].queryset = Master.objects.filter(
                salon__pk=salon_pk, is_active=True
            )
        self.fields["master"].empty_label = "Выберите мастера"


class SelectSalonForm(forms.Form):
    salon = forms.ModelChoiceField(
        queryset=Salon.objects.all(),
        label="",
        empty_label="Выберите салон",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    


class MasterForm(forms.ModelForm):

    class Meta:
        model = Master
        fields = [
            "name",
            "description",
            "photo",
            "tattoo_type",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Имя"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Описание"}
            ),
            "photo": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Фото"}
            ),
            "tattoo_type": forms.SelectMultiple(
                attrs={"class": "form-control", "placeholder": "Типы тату"}
            ),
        }
        labels = {
            "name": "",
            "description": "",
            "photo": "Фотография",
            "tattoo_type": "Типы тату",
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields["master"].queryset = Master.objects.filter(user=self.user)
