from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from database.models import Master, Slider
from site_setting.models import AboutBlock
from pages.forms import AppointmentForm, SelectSalonForm
from pages.misc.page_info import get_contact_info, get_random_salon
from django.http import JsonResponse
from django.template.loader import render_to_string


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from UserAuth.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomUserChangeForm,
    ChangeForm,
)


def main(request):
    data = {}
    salon = request.session.get("salon")
    if salon is None:
        new_salon = get_random_salon()
        request.session["salon"] = new_salon.get_session_data()
        salon = request.session.get("salon")
    masters = Master.objects.filter(is_active=True, salon__pk=salon.get("pk"))
    slides = Slider.objects.filter(is_active=True)
    abouts = AboutBlock.objects.all()[:3]
    info = get_contact_info(salon)
    if request.user.is_authenticated:
        data["change_form"] = ChangeForm(instance=request.user)
    else:
        data["login_form"] = CustomAuthenticationForm()
        data["register_form"] = CustomUserCreationForm()
    data["masters"] = masters
    data["slides"] = slides
    data["abouts"] = abouts
    data["info"] = info
    data["salon_form"] = SelectSalonForm()
    data["appointment_form"] = AppointmentForm(salon_pk=salon["pk"])
    return render(request, "home/main.html", data)
