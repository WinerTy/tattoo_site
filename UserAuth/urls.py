from django.urls import path, include
from .views import user_login, user_logout, user_register, user_change

urlpatterns = [
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    path("register/", user_register, name="user_register"),
    path("change/", user_change, name="user_change"),
]
