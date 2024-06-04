from django.views.generic import DetailView

from database.models import Master, SocialAccount, Session

from pages.forms import SelectSalonForm
from UserAuth.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ChangeForm,
)
from pages.misc.page_info import (
    get_random_salon,
    get_master_info,
)
from pages.forms import SelectSalonForm, MasterForm


class MasterInfo(DetailView):
    model = Master
    template_name = "master/MasterInfo.html"
    context_object_name = "master"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["social_accounts"] = SocialAccount.objects.filter(master=self.object)
        context["working_time"] = Session.objects.filter(
            master=self.object, is_active=True
        )
        context["salon_form"] = SelectSalonForm()
        if self.request.user.is_authenticated:
            user_master = Master.objects.filter(user=self.request.user).first()
            context["change_form"] = ChangeForm(instance=self.request.user)
            context["master_info"] = get_master_info(self.request.user)
            context["master_form"] = MasterForm(instance=user_master)
        else:
            context["login_form"] = CustomAuthenticationForm()
            context["register_form"] = CustomUserCreationForm()
        return context
