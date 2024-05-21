from django.shortcuts import redirect

from database.models import Salon


def select_salon(request):
    if request.method == "POST":
        salon_pk = request.POST.get("salon_pk")
        if salon_pk == "Наши салоны":
            if "salon" in request.session:
                del request.session["salon"]
        else:
            salon = Salon.objects.get(pk=salon_pk)
            data = {
                "name": salon.name,
                "address": salon.address,
                "pk": salon.pk,
                "longitude": salon.longitude,
                "latitude": salon.latitude,
            }
            request.session["salon"] = data
    return redirect("home")
