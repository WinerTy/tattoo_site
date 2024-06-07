from django.views.generic import DetailView
from django.shortcuts import redirect, render
from django.urls import reverse
from database.models import Master, SocialAccount, Session

from UserAuth.forms import (
    CustomAuthenticationForm,
)
from pages.misc.page_info import check_groups
from pages.forms import SelectSalonForm, MasterForm, MasterReviewForm, AppointmentV2Form


class MasterInfo(DetailView):
    model = Master
    template_name = "master/MasterInfo.html"
    context_object_name = "master"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sessions = Session.objects.filter(master=self.object)
        context["social_accounts"] = SocialAccount.objects.filter(master=self.object)
        context["days_of_week"] = sessions.values_list(
            "day_of_week", flat=True
        ).distinct()
        if self.request.user.is_authenticated:
            user_master = Master.objects.filter(user=self.request.user).first()
            context["master_form"] = MasterForm(instance=user_master)
            context["is_master"] = check_groups(self.request, "Мастер")
        return context


def filter_sessions(request):
    master_id = request.GET.get("master_id")
    day_of_week = request.GET.get("day_of_week")
    sessions = Session.objects.filter(master__pk=master_id, day_of_week=day_of_week)
    return render(request, "components/master/sessions.html", {"times": sessions})


def get_form_review(request):
    if request.user.is_authenticated:
        master_id = request.GET.get("master_id")
        return render(
            request,
            "components/forms/review_form.html",
            {"form": MasterReviewForm(), "master_id": master_id},
        )
    else:
        return render(
            request,
            "components/master/review_form.html",
            {"form": CustomAuthenticationForm()},
        )


def create_appointmentv2(request):
    if request.method == "POST":
        master = Master.objects.get(id=request.POST.get("master_id"))
        form = AppointmentV2Form(request.POST, master=master)
        path = request.META.get("HTTP_REFERER", reverse("home"))
        if form.is_valid():
            app = form.save(commit=False)
            app.master = master
            app.user = request.user
            app.session = form.cleaned_data.get("session")
            app.save()
            return redirect(path)
    return redirect("master_info", pk=master.pk)


def get_form_appointment(request):
    master = Master.objects.get(id=request.GET.get("master_id"))
    form = AppointmentV2Form(master=master)
    return render(
        request,
        "components/forms/appointment.html",
        {"form": form, "master_id": master.pk},
    )


def create_rewiew(request):
    if request.method == "POST":
        master_id = request.POST.get("master_id")
        master = Master.objects.get(pk=master_id)
        form = MasterReviewForm(request.POST)
        path = request.META.get("HTTP_REFERER", reverse("home"))
        if form.is_valid():
            review = form.save(commit=False)
            review.master = master
            review.user = request.user
            review.save()
            return redirect(path)
    return redirect(path)
