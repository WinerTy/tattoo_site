from django import forms
from database.models import Master
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
    master = forms.ChoiceField(label='Мастер', choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        salon = kwargs.pop('salon', None)
        super().__init__(*args, **kwargs)
        if salon:
            masters = Master.objects.filter(salon__pk=salon['pk'], is_active=True).order_by('?')
            for test in masters:
                ic(test.pk)
            choices = [(master.pk, master.name) for master in masters]
            self.fields['master'].choices = choices
