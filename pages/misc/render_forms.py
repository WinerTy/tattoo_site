from django.shortcuts import render
from UserAuth.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ChangeForm,
)
from database.models import Master
from pages.forms import SelectSalonForm, MasterForm, AppointmentForm, MasterReviewForm


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


def render_master_form(request):
    user_master = Master.objects.filter(user=request.user).first()
    return render(
        request,
        "components/forms/master_form.html",
        {"form": MasterForm(instance=user_master)},
    )


def render_form_appointment(request):
    master = Master.objects.get(id=request.GET.get("master_id"))
    form = AppointmentForm(master=master)
    return render(
        request,
        "components/forms/appointment.html",
        {"form": form, "master_id": master.pk},
    )


def render_form_review(request):
    if request.user.is_authenticated:
        master_id = request.GET.get("master_id")
        return render(
            request,
            "components/forms/review_form.html",
            {"form": MasterReviewForm(), "master_id": master_id},
        )
    else:
        return render(
            request,
            "components/master/review_form.html",
            {"form": CustomAuthenticationForm()},
        )
