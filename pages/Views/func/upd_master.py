from pages.forms import MasterForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from database.models import Master
from pages.misc.create_message import create_message


def update_master_info(request):
    if request.method == "POST":
        path = request.META.get("HTTP_REFERER", "home")
        master = get_object_or_404(Master, user=request.user)
        form = MasterForm(request.POST, request.FILES, instance=master)
        if form.is_valid():
            form.save()
            request.session["message"] = create_message(
                "success", "Вы обновили информацию о себе"
            )
            return redirect(path + "#UserModal")

    return redirect(path)
