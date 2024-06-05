from django.urls import path
from .Views import (
    main,
    select_salon,
    about,
    create_appointment,
    clear_session,
    MasterInfo,
    MastersView,
    WokrView,
    AboutInfo,
)
from .Views.func.upd_master import update_master_info
from .Views.Master.master_info import (
    filter_sessions,
    get_form_review,
    create_rewiew,
    get_form_appointment,
    create_appointmentv2,
)

urlpatterns = [
    path("", main, name="home"),
    path("ourworks/", WokrView.as_view(), name="ourworks"),
    path("about/", about, name="about"),
    path("masters/", MastersView.as_view(), name="masters"),
    path("masters/<int:pk>/", MasterInfo.as_view(), name="master-info"),
    path("about/<int:pk>", AboutInfo.as_view(), name="about-info"),
    path("select_salon/", select_salon, name="select_salon"),
    path("clear/", clear_session, name="clear"),
    path("consultation/", create_appointment, name="consultation"),
    path("update_master/", update_master_info, name="update_master"),
    path("filter_sessions/", filter_sessions, name="filter_sessions"),
    path("get_form_review/", get_form_review, name="get_form_review"),
    path("create_rewiew/", create_rewiew, name="create_rewiew"),
    path("get_form_appointment/", get_form_appointment, name="get_form_appointment"),
    path("create_appointmentv2/", create_appointmentv2, name="create_appointmentv2"),
]
