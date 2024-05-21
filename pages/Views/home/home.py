from django.shortcuts import render

from database.models import Master, Slider
from site_setting.models import AboutBlock, Salon
from pages.forms import AppointmentForm
from pages.misc.page_info import get_contact_info, get_random_salon


def main(request):
    data = {}
    salons = Salon.objects.all()
    data["salons"] = salons
    salon = request.session.get("salon")
    message = request.session.get("message")
    data["message"] = message
    if salon is None:
        new_salon = get_random_salon()
        request.session["salon"] = {
            "name": new_salon.name,
            "address": new_salon.address,
            "pk": new_salon.pk,
            "longitude": new_salon.longitude,
            "latitude": new_salon.latitude,
        }
        salon = request.session.get("salon")
    masters = Master.objects.filter(is_active=True, salon__pk=salon.get("pk"))[:3]
    slides = Slider.objects.filter(is_active=True)
    abouts = AboutBlock.objects.all()[:3]
    info = get_contact_info(salon)
    data["masters"] = masters
    data["slides"] = slides
    data["abouts"] = abouts
    data["info"] = info
    data["appointment_form"] = AppointmentForm(salon_pk=salon["pk"])
    return render(request, "main.html", data)
