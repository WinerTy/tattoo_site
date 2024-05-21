from django.views.generic import DetailView
from django.shortcuts import render

from site_setting.models import AboutBlock


def about(request):
    return render(request, "about/About.html")


class AboutInfo(DetailView):
    model = AboutBlock
    template_name = "about/AboutInfo.html"
    context_object_name = "about"
