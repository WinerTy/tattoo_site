from django.views.generic import DetailView
from django.shortcuts import render

from site_setting.models import AboutBlock
from pages.forms import SelectSalonForm


def about(request):
    return render(request, "about/About.html")


class AboutInfo(DetailView):
    model = AboutBlock
    template_name = "about/AboutInfo.html"
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["salons"] = Salon.objects.all()
        context["info"] = get_contact_info(self.request.session.get("salon"))
        return context
