from django.shortcuts import render
from database.models import Master, Slider
from site_setting.models import AboutBlock
from pages.forms import AppointmentForm, SelectSalonForm, MasterForm
from pages.misc.page_info import (
    get_contact_info,
    get_random_salon,
    get_master_info,
    check_groups,
)
from UserAuth.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
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

    if request.user.is_authenticated:
        user_master = Master.objects.filter(user=request.user).first()
        data["change_form"] = ChangeForm(instance=request.user)
        data["master_info"] = get_master_info(request.user)
        data["master_form"] = MasterForm(instance=user_master)
        data["is_master"] = check_groups(request, "Мастер")
    else:
        data["login_form"] = CustomAuthenticationForm()
        data["register_form"] = CustomUserCreationForm()

    data["masters"] = masters
    data["slides"] = slides
    data["abouts"] = abouts
    data["info"] = get_contact_info(salon)
    data["salon_form"] = SelectSalonForm()
    data["appointment_form"] = AppointmentForm(salon_pk=salon["pk"])
    return render(request, "home/home_page.html", data)
