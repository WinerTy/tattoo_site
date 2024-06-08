from django.urls import path
from .Views import (
    main,
    select_salon,
    create_consultation,
    clear_session,
    MasterInfo,
    MastersView,
    create_rewiew,
    create_appointment,
)
from .Views.func.upd_master import update_master_info

from .misc.render_forms import (
    render_login_form,
    render_register_form,
    render_salon_form,
    render_settings_form,
    render_master_form,
    render_form_appointment,
    render_form_review,
)
from .Views.About.about import AboutPage

urlpatterns = [
    path("", main, name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("masters/", MastersView.as_view(), name="masters"),
    path("masters/<int:pk>/", MasterInfo.as_view(), name="master-info"),
    path("select_salon/", select_salon, name="select_salon"),
    path("clear/", clear_session, name="clear"),
    path("consultation/", create_consultation, name="consultation"),
    path("update_master/", update_master_info, name="update_master"),
    path("filter_sessions/", MasterInfo.filter_sessions, name="filter_sessions"),
    path("create_rewiew/", create_rewiew, name="create_rewiew"),
    path("create_appointment/", create_appointment, name="create_appointment"),
    path("get_form_appointment/", render_form_appointment, name="get_form_appointment"),
    path("get_form_review/", render_form_review, name="get_form_review"),
    path("get_login_form/", render_login_form, name="get_login_form"),
    path("get_register_form/", render_register_form, name="get_register_form"),
    path("get_salon_form/", render_salon_form, name="get_salon_form"),
    path("get_settings_form/", render_settings_form, name="get_settings_form"),
    path("get_master_form/", render_master_form, name="get_master_form"),
]
