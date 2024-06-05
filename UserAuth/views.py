from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from pages.misc.create_message import create_message
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ChangeForm,
)


def user_login(request):
    if request.method == "POST":
        path = request.META.get("HTTP_REFERER", "home")
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session["message"] = create_message(
                    "success", "Вы успешно вошли в аккаунт"
                )
                return redirect(path)
        else:
            request.session["message"] = create_message(
                "danger", "Неверное имя пользователя или пароль"
            )
            return redirect(path + "#UserModal")

    return redirect(path + "#UserModal")


def user_logout(request):
    logout(request)
    request.session["message"] = create_message("success", "Вы вышли из аккаунта")
    return redirect(request.META.get("HTTP_REFERER", "home"))


def user_register(request):
    if request.method == "POST":
        path = request.META.get("HTTP_REFERER", "home")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session["message"] = create_message(
                "success", "Аккаунт успешно создан"
            )
            login(request, user)
            return redirect(path)
        else:
            request.session["message"] = create_message(
                "danger", "Произошла ошибка при регистрации"
            )
            return redirect(path + "#UserModal")

    return redirect(path + "#UserModal")


def user_change(request):
    if request.method == "POST":
        path = request.META.get("HTTP_REFERER", "home")
        form = ChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            request.session["message"] = create_message(
                "success", "Данные успешно изменены"
            )
            return redirect(path + "#UserModal")
        else:
            request.session["message"] = create_message(
                "error", "Произошла ошибка при изменении данных"
            )
            return redirect(path + "#UserModal")
    return redirect(path + "#UserModal")
