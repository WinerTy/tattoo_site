from django.views.generic import ListView

from database.models import Master

from pages.misc.page_info import get_random_salon
from pages.forms import SelectSalonForm


class MastersView(ListView):
    model = Master  # Модель
    template_name = "master/Masters.html"  # Шаблон для рендера
    context_object_name = "masters"  # Контект для использования в шаблоне
    paginate_by = 20  # Количество отоброжаемых мастеров на странице

    def get_context_data(self, **kwargs):  # Унаследованная функция для получения дополнительных данных в контекст шаблона 
        context = super().get_context_data(**kwargs)  # Вызов родительской функции
        context["salon_form"] = SelectSalonForm()  # Добавление формы для выбора салона
        return context  # Возврат контекста

    def get_queryset(self):  # Функция для получения списка мастеров
        try: # Попытка получить список мастеров через сессию
            return (
                super()
                .get_queryset()
                .filter(
                    is_active=True,
                    salon__pk=self.request.session.get("salon").get("pk"),
                )
                .order_by("name")
            )
        except Exception:  # при ошибке выдачи случайного салона
            return (
                super()
                .get_queryset()
                .filter(is_active=True, salon__pk=get_random_salon().pk)
                .order_by("name")
            )
