from django.views.generic import DetailView

from database.models import Master, SocialAccount

from pages.forms import SelectSalonForm


class MasterInfo(DetailView):
    model = Master
    template_name = "master/MasterInfo.html"
    context_object_name = "master"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["social_accounts"] = SocialAccount.objects.filter(master=self.object)
        context["salon_form"] = SelectSalonForm()
        return context
