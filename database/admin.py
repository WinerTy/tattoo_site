from collections.abc import Sequence
from doctest import master
from django.contrib import admin
from django.http import HttpRequest
from django.utils.html import format_html
from django.db import models

from image_uploader_widget.widgets import ImageUploaderWidget

from .models import (
    TattooType,
    Works,
    Master,
    Consultation,
    SocialAccount,
    Slider,
    Session,
    MasterReview,
    AppointmentV2,
)


class ReviewInline(admin.StackedInline):
    model = MasterReview


class SliderAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "show_image", "is_active"]
    list_display_links = ["id", "title"]
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {"all": ("css/admin/ImageUploader.css",)}

    def show_image(self, obj):
        image = obj.photo
        return format_html(
            '<img src="{}" style="width: 100px; height: 100px; object-fit: cover;" />'.format(
                image.url
            )
        )

    show_image.short_description = "Изображение"


class SessionInline(admin.TabularInline):
    model = Session


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {"all": ("css/admin/ImageUploader.css",)}


class MasterAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = [
        "salon",
    ]
    inlines = [SocialAccountInline, SessionInline, ReviewInline]
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {"all": ("css/admin/ImageUploader.css",)}


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ["id", "master"]
    list_filter = ["master"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        master = Master.objects.filter(user=request.user).first()
        if master:
            return qs.filter(master=master)
        return qs.none()

    def get_list_filter(self, request: HttpRequest) -> Sequence[str]:
        if request.user.is_superuser:
            return super().get_list_filter(request)
        master = Master.objects.filter(user=request.user).first()
        if master:
            return []


admin.site.register(AppointmentV2)
admin.site.register(Works)
admin.site.register(Master, MasterAdmin)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(TattooType)
