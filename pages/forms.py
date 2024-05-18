from django import forms
from database.models import Master
from site_setting.models import Salon
from icecream import ic


class AppointmentForm(forms.Form):
    client_email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        )
    )
    client_phone = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Телефон'}
        )
    )
    master = forms.ModelChoiceField(
        queryset=Master.objects.none(),
        label='Мастер',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        salon_pk = kwargs.pop('salon_pk', None)
        super().__init__(*args, **kwargs)
        if salon_pk:
            self.fields['master'].queryset = Master.objects.filter(
                salon__pk=salon_pk,
                is_active=True
            )
