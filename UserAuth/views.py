from django.shortcuts import render

from django.template.loader import render_to_string

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from pages.misc.create_message import create_message


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session["message"] = create_message(
                    "success", "Вы успешно вошли в аккаунт"
                )
                return redirect("home")
        else:
            request.session["message"] = create_message(
                "error", "Неверное имя пользователя или пароль"
            )
            return redirect("home")

    return redirect("home")


def user_logout(request):
    logout(request)
    request.session["message"] = create_message("success", "Вы вышли из аккаунта")
    return redirect("home")
