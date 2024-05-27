from django.urls import path, include
from .views import user_login, user_logout

urlpatterns = [
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
]