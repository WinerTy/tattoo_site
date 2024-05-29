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


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Пароль"}
        ),
        required=False,  # Поле становится необязательным
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ["username", "email", "password"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""
            self.fields[fieldname].widget.attrs.update({"class": "form-control"})
            self.fields[fieldname].required = False

        self.fields["username"].widget.attrs.update({"placeholder": "Логин"})
        self.fields["email"].widget.attrs.update({"placeholder": "Электронная почта"})
        self.fields["password"].widget.attrs.update({"placeholder": "Пароль"})


class ChangeForm(forms.ModelForm):
    old_password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Текущий пароль"}
        ),
        required=False,
    )
    new_password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Новый пароль"}
        ),
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "old_password", "new_password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ["username", "email", "phone"]:
            self.fields[fieldname].label = ""
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({"class": "form-control"})

        self.fields["username"].widget.attrs.update({"placeholder": "Логин"})
        self.fields["email"].widget.attrs.update({"placeholder": "Электронная почта"})
        self.fields["phone"].widget.attrs.update({"placeholder": "Номер телефона"})

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        if old_password and new_password:
            if not self.instance.check_password(old_password):
                self.add_error("old_password", "Неверный пароль")
            else:
                self.instance.set_password(new_password)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["new_password"])
        if commit:
            user.save()
        return user
