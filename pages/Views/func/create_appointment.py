from django.shortcuts import redirect

from database.models import Note
from pages.forms import AppointmentForm


def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(
            request.POST, salon_pk=request.session.get("salon").get("pk")
        )
        if form.is_valid():
            appointment = Note.objects.create(
                client_email=form.cleaned_data["client_email"],
                client_phone=form.cleaned_data["client_phone"],
                master=form.cleaned_data["master"],
            )
            appointment.save()
            request.session["message"] = "Запись успешно создана!"
            return redirect("home")
        else:
            request.session["message"] = "Произошла ошибка при оформлении записи!"
            return redirect("home")
    return redirect("home")
