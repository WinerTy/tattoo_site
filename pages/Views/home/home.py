from django.shortcuts import render
from django.conf import settings
from database.models import Master
from site_setting.models import AboutBlock, Slider
from pages.forms import ConsultationForm
from pages.misc.page_info import (
    get_contact_info,
    get_random_salon,
    check_groups,
)


def main(request):
    data = {}
    salon = request.session.get("salon")
    if salon is None:
        try:
            new_salon = get_random_salon()
            request.session["salon"] = new_salon.get_session_data()
            salon = request.session.get("salon")
        except IndexError:
            return render(
                request, "errors/error.html", {"admin_email": settings.ADMIN_EMAIL}
            )
    masters = Master.objects.filter(is_active=True, salon__pk=salon.get("pk"))
    slides = Slider.objects.filter(is_active=True)
    abouts = AboutBlock.objects.all()[:3]

    if request.user.is_authenticated:
        data["is_master"] = check_groups(request, "Мастер")

    data["masters"] = masters
    data["slides"] = slides
    data["abouts"] = abouts
    data["info"] = get_contact_info(salon)
    data["consultation_form"] = ConsultationForm(salon_pk=salon["pk"])
    return render(request, "home/home_page.html", data)
