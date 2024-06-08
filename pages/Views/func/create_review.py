from database.models import Master
from pages.forms import MasterReviewForm
from django.shortcuts import redirect
from django.urls import reverse


def create_rewiew(request):
    if request.method == "POST":
        master_id = request.POST.get("master_id")
        master = Master.objects.get(pk=master_id)
        form = MasterReviewForm(request.POST)
        path = request.META.get("HTTP_REFERER", reverse("home"))
        if form.is_valid():
            review = form.save(commit=False)
            review.master = master
            review.user = request.user
            review.save()
            return redirect(path)
    return redirect(path)
