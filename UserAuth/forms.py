from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


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
