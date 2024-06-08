from django.views.generic import DetailView
from django.shortcuts import redirect, render
from django.urls import reverse
from database.models import Master, SocialAccount, Session

from UserAuth.forms import (
    CustomAuthenticationForm,
)
from pages.misc.page_info import check_groups
from pages.forms import MasterReviewForm, AppointmentForm


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
            context["is_master"] = check_groups(self.request, "Мастер")
        return context

    def filter_sessions(request):
        master_id = request.GET.get("master_id")
        day_of_week = request.GET.get("day_of_week")
        sessions = Session.objects.filter(master__pk=master_id, day_of_week=day_of_week)
        return render(request, "components/master/sessions.html", {"times": sessions})
