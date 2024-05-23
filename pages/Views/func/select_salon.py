from django.shortcuts import redirect
from django.urls import reverse
from database.models import Salon
from icecream import ic


def select_salon(request):
    if request.method == "POST":
        salon = request.POST.get("salon")
        selected_salon = Salon.objects.get(pk=salon)
        request.session["salon"] = selected_salon.get_session_data()
        redirect_url = request.META.get("HTTP_REFERER", reverse("home"))

        return redirect(redirect_url)

    return redirect(reverse("home"))
