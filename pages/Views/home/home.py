from django.shortcuts import render

from database.models import Master, Slider
from site_setting.models import AboutBlock
from pages.forms import AppointmentForm, SelectSalonForm
from pages.misc.page_info import get_contact_info, get_random_salon


def main(request):
    data = {}
    salon = request.session.get("salon")
    message = request.session.get("message")
    data["message"] = message
    if salon is None:
        new_salon = get_random_salon()
        request.session["salon"] = new_salon.get_session_data()
        salon = request.session.get("salon")
    masters = Master.objects.filter(is_active=True, salon__pk=salon.get("pk"))[:3]
    slides = Slider.objects.filter(is_active=True)
    abouts = AboutBlock.objects.all()[:3]
    info = get_contact_info(salon)
    data["masters"] = masters
    data["slides"] = slides
    data["abouts"] = abouts
    data["info"] = info
    data["salon_form"] = SelectSalonForm()
    data["appointment_form"] = AppointmentForm(salon_pk=salon["pk"])
    return render(request, "home/main.html", data)
