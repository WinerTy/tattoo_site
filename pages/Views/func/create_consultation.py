from django.shortcuts import redirect

from pages.forms import ConsultationForm
from pages.misc.create_message import create_message


def create_consultation(request):
    if request.method == "POST":
        form = ConsultationForm(
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
