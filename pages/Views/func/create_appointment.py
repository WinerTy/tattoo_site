from django.shortcuts import redirect

from pages.forms import AppointmentForm
from pages.misc.create_message import create_message


def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(
            request.POST, salon_pk=request.session.get("salon").get("pk")
        )
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.save()
            request.session["message"] = create_message(
                "success", "Запись успешно создана!"
            )
            return redirect("home")
        else:
            request.session["message"] = create_message(
                "error", "Произошла ошибка при оформлении записи!"
            )
            return redirect("home")
    return redirect("home")
