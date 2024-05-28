from django.shortcuts import render

from django.template.loader import render_to_string

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from pages.misc.create_message import create_message
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def user_login(request):
    if request.method == "POST":
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


def user_register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session["message"] = create_message(
                "success", "Аккаунт успешно создан"
            )
            login(request, user)
            return redirect("home")
        else:
            request.session["message"] = create_message(
                "error", "Произошла ошибка при регистрации"
            )
            return redirect("home")

    return redirect("home")
