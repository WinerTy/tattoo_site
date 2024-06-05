from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from .models import CustomUser
from django import forms
from django.contrib.auth.hashers import make_password


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ["username", "password"]:
            self.fields[fieldname].label = ""
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({"class": "form-control"})

        self.fields["username"].widget.attrs.update({"placeholder": "Логин"})
        self.fields["password"].widget.attrs.update({"placeholder": "Пароль"})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Электронная почта"}
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""
            self.fields[fieldname].widget.attrs.update({"class": "form-control"})

        self.fields["username"].widget.attrs.update({"placeholder": "Логин"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Пароль"})
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Повторите пароль"}
        )


class ChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ["username", "email", "phone"]:
            self.fields[fieldname].label = ""
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({"class": "form-control"})

        self.fields["username"].widget.attrs.update({"placeholder": "Логин"})
        self.fields["email"].widget.attrs.update({"placeholder": "Электронная почта"})
        self.fields["phone"].widget.attrs.update({"placeholder": "Номер телефона"})
