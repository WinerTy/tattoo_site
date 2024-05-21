from django.views.generic import ListView

from database.models import Works


class WokrView(ListView):
    model = Works
    template_name = "works.html"
    context_object_name = "data"
