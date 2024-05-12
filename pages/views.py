from django.views.generic import ListView
from django.shortcuts import render
from database.models import Works


def main(request):
    return render(request, "main.html")


class WokrView(ListView):
    model = Works
    template_name = "works.html"
    context_object_name = "data"


def about(request):
    return render(request, "about.html")
