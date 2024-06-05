from django.shortcuts import render
from UserAuth.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ChangeForm,
)
from pages.forms import SelectSalonForm


def render_login_form(request):
    return render(
        request,
        "components/forms/login_form.html",
        {"form": CustomAuthenticationForm()},
    )


def render_register_form(request):
    return render(
        request,
        "components/forms/register_form.html",
        {"form": CustomUserCreationForm()},
    )


def render_salon_form(request):
    return render(
        request,
        "components/forms/salon_form.html",
        {"form": SelectSalonForm()},
    )


def render_settings_form(request):
    return render(
        request,
        "components/forms/settings_form.html",
        {"form": ChangeForm(instance=request.user)},
    )
