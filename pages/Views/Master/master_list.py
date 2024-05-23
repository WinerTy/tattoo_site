from django.views.generic import ListView

from database.models import Master, Salon

from pages.misc.page_info import get_contact_info
from pages.forms import SelectSalonForm


class MastersView(ListView):
    model = Master
    template_name = "master/Masters.html"
    context_object_name = "masters"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["salon_form"] = SelectSalonForm()
        return context

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                is_active=True, salon__pk=self.request.session.get("salon").get("pk")
            )
            .order_by("name")
        )
