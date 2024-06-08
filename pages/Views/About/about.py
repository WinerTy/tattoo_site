from django.views.generic import ListView
from site_setting.models import AboutBlock


class AboutPage(ListView):
    model = AboutBlock
    template_name = "about/AboutPage.html"
    context_object_name = "data"
