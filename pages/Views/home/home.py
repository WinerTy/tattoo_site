from django.shortcuts import render
from database.models import Master
from site_setting.models import AboutBlock, Slider
from pages.forms import AppointmentForm
from pages.misc.page_info import (
    get_contact_info,
    get_random_salon,
    check_groups,
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
        data["is_master"] = check_groups(request, "Мастер")

    data["masters"] = masters
    data["slides"] = slides
    data["abouts"] = abouts
    data["info"] = get_contact_info(salon)
    data["appointment_form"] = AppointmentForm(salon_pk=salon["pk"])
    return render(request, "home/home_page.html", data)
