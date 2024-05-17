from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from database.models import Works, Master, SocialAccount, Slider
from site_setting.models import AboutBlock, Contact, Salon
import random


def main(request):
    data = {}
    salons = Salon.objects.all()
    data['salons'] = salons
    salon = request.session.get('salon')
    if salon is None:
        new_salon = random.choice(salons)
        request.session['salon'] = {"name": new_salon.name,
                                    "address": new_salon.address,
                                    "pk": new_salon.pk,
                                    "longitude": new_salon.longitude,
                                    "latitude": new_salon.latitude,
                                    }
        salon = request.session.get('salon')
    masters = Master.objects.filter(is_active=True, salon__pk=salon.get('pk'))[:3]
    slides = Slider.objects.filter(is_active=True)
    abouts = AboutBlock.objects.all()[:3]
    info = Contact.objects.get(salon__pk=salon['pk'])
    data['masters'] = masters
    data['slides'] = slides
    data["abouts"] = abouts
    data["info"] = info

    return render(request, "main.html", data)


def clear(request):
    request.session.flush()
    return redirect('home')


def about(request):
    return render(request, "about/About.html")


class WokrView(ListView):
    model = Works
    template_name = "works.html"
    context_object_name = "data"


class MasterInfo(DetailView):
    model = Master
    template_name = "master/MasterInfo.html"
    context_object_name = "master"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_accounts'] = SocialAccount.objects.filter(
            master=self.object)
        return context


class AboutInfo(DetailView):
    model = AboutBlock
    template_name = "about/AboutInfo.html"
    context_object_name = "about"


class MastersView(ListView):
    model = Master


def select_salon(request):
    if request.method == 'POST':
        salon_pk = request.POST.get('salon_pk')
        salon = Salon.objects.get(pk=salon_pk)
        data = {
            "name": salon.name,
            "address": salon.address,
            "pk": salon.pk,
            "longitude": salon.longitude,
            "latitude": salon.latitude,
        }
        request.session['salon'] = data
        if salon_pk:
            request.session['salon']['pk'] = salon_pk
    return redirect('home')
