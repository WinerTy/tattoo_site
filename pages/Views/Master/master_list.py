from django.views.generic import ListView

from database.models import Master


from pages.misc.page_info import (
    get_random_salon,
    check_groups,
)


class MastersView(ListView):
    model = Master  # Модель
    template_name = "master/Masters.html"  # Шаблон для рендера
    context_object_name = "masters"  # Контект для использования в шаблоне
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["is_master"] = check_groups(self.request, "Мастер")
        return context

    def get_queryset(self):
        try:
            return (
                super()
                .get_queryset()
                .filter(
                    is_active=True,
                    salon__pk=self.request.session.get("salon").get("pk"),
                )
                .order_by("name")
            )
        except Exception:
            return (
                super()
                .get_queryset()
                .filter(is_active=True, salon__pk=get_random_salon().pk)
                .order_by("name")
            )
