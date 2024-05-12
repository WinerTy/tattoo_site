from django.views.generic import ListView,DetailView
from django.shortcuts import render
from database.models import Works, Master


def main(request):
    masters = Master.objects.filter(is_active=True)
    data = {
        "masters": masters
    }
    return render(request, "main.html", data)


class WokrView(ListView):
    model = Works
    template_name = "works.html"
    context_object_name = "data"


def about(request):
    return render(request, "about.html")


class MasterInfo(DetailView):
    model = Master
    template_name = "master/MasterInfo.html"
    context_object_name = "master"