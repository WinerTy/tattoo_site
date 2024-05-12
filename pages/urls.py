from django.urls import path
from .views import *

urlpatterns = [
    path("", main, name="home"),
    path("ourworks/", WokrView.as_view(), name="ourworks"),
    path("about/", about, name="about"),
    path("master/<int:pk>/", MasterInfo.as_view(), name="master-info")
]
