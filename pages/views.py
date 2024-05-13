from django.views.generic import ListView, DetailView
from django.shortcuts import render
from database.models import Works, Master, SocialAccount, Slider

abouts = [{"title": "asdasdasd", "text": "asdasas32rewfdvcd"}, {}, {}]

def main(request):
    masters = Master.objects.filter(is_active=True)
    slides = Slider.objects.filter(is_active=True)
    data = {
        "masters": masters,
        "slides": slides,
        'abouts': abouts,
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_accounts'] = SocialAccount.objects.filter(master=self.object)
        return context