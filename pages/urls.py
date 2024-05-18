from django.urls import path
from .views import *

urlpatterns = [
    path("", main, name="home"),
    path("ourworks/", WokrView.as_view(), name="ourworks"),
    path("about/", about, name="about"),
    path("master/<int:pk>/", MasterInfo.as_view(), name="master-info"),
    path("about/<int:pk>", AboutInfo.as_view(), name="about-info"),
    path('select_salon/', select_salon, name='select_salon'),
    path("clear/", clear, name="clear"),
    path("appointment/", CreateAppointment, name="appointment"),
]
