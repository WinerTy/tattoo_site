from django.shortcuts import redirect
from django.urls import reverse
from database.models import Master
from pages.forms import AppointmentForm


def create_appointment(request):
    if request.method == "POST":
        master = Master.objects.get(id=request.POST.get("master_id"))
        form = AppointmentForm(request.POST, master=master)
        path = request.META.get("HTTP_REFERER", reverse("home"))
        if form.is_valid():
            app = form.save(commit=False)
            app.master = master
            app.user = request.user
            app.session = form.cleaned_data.get("session")
            app.save()
            return redirect(path)
    return redirect("master_info", pk=master.pk)
