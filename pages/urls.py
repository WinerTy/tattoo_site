from django.urls import path
from .Views import (
    main,
    select_salon,
    create_appointment,
    clear_session,
    MasterInfo,
    MastersView,
    WokrView,
)
from .Views.func.upd_master import update_master_info
from .Views.Master.master_info import (
    filter_sessions,
    get_form_review,
    create_rewiew,
    get_form_appointment,
    create_appointmentv2,
)
from .misc.render_forms import (
    render_login_form,
    render_register_form,
    render_salon_form,
    render_settings_form,
    render_master_form,
)

urlpatterns = [
    path("", main, name="home"),
    path("ourworks/", WokrView.as_view(), name="ourworks"),
    path("masters/", MastersView.as_view(), name="masters"),
    path("masters/<int:pk>/", MasterInfo.as_view(), name="master-info"),
    path("select_salon/", select_salon, name="select_salon"),
    path("clear/", clear_session, name="clear"),
    path("consultation/", create_appointment, name="consultation"),
    path("update_master/", update_master_info, name="update_master"),
    path("filter_sessions/", filter_sessions, name="filter_sessions"),
    path("create_rewiew/", create_rewiew, name="create_rewiew"),
    path("create_appointmentv2/", create_appointmentv2, name="create_appointmentv2"),
    path("get_form_appointment/", get_form_appointment, name="get_form_appointment"),
    path("get_form_review/", get_form_review, name="get_form_review"),
    path("get_login_form/", render_login_form, name="get_login_form"),
    path("get_register_form/", render_register_form, name="get_register_form"),
    path("get_salon_form/", render_salon_form, name="get_salon_form"),
    path("get_settings_form/", render_settings_form, name="get_settings_form"),
    path("get_master_form/", render_master_form, name="get_master_form"),
]
