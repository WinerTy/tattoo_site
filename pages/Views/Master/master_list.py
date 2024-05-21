from django.views.generic import ListView

from database.models import Master, Salon

from pages.misc.page_info import get_contact_info


class MastersView(ListView):
    model = Master
    template_name = "master/Masters.html"
    context_object_name = "masters"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["salons"] = Salon.objects.all()
        context["info"] = get_contact_info(self.request.session.get("salon"))
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
