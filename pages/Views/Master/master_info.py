from django.views.generic import DetailView
from django.shortcuts import render
from database.models import Master, SocialAccount, Session

from pages.forms import SelectSalonForm
from UserAuth.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ChangeForm,
)
from pages.misc.page_info import get_master_info, check_groups
from pages.forms import SelectSalonForm, MasterForm


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
        context["salon_form"] = SelectSalonForm()
        if self.request.user.is_authenticated:
            user_master = Master.objects.filter(user=self.request.user).first()
            context["change_form"] = ChangeForm(instance=self.request.user)
            context["master_info"] = get_master_info(self.request.user)
            context["master_form"] = MasterForm(instance=user_master)
            context["is_master"] = check_groups(self.request, "Мастер")
        else:
            context["login_form"] = CustomAuthenticationForm()
            context["register_form"] = CustomUserCreationForm()
        return context


def filter_sessions(request):
    master_id = request.GET.get("master_id")
    day_of_week = request.GET.get("day_of_week")
    sessions = Session.objects.filter(master__pk=master_id, day_of_week=day_of_week)
    return render(request, "components/master/sessions.html", {"times": sessions})
