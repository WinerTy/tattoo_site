from django.contrib import admin
from django.db import models


from image_uploader_widget.widgets import ImageUploaderWidget

from .models import (
    TattooType,
    Works,
    Master,
    Consultation,
    SocialAccount,
    Session,
    MasterReview,
    Appointment,
)


class ConsultationInline(admin.TabularInline):
    model = Consultation

    def has_existing_obj(self, obj):
        return self.model.objects.all().exists()

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return 2
        elif self.has_existing_obj(obj):
            return 1
        return 2


class AppointmentInline(admin.TabularInline):
    model = Appointment

    def has_existing_obj(self, obj):
        return self.model.objects.all().exists()

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return 2
        elif self.has_existing_obj(obj):
            return 1
        return 2


class ReviewInline(admin.StackedInline):
    model = MasterReview


class SessionInline(admin.TabularInline):
    model = Session
    extra = 0

    def has_existing_obj(self, obj):
        return self.model.objects.all().exists()

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return 2
        elif self.has_existing_obj(obj):
            return 1
        return 2


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {"all": ("css/admin/ImageUploader.css",)}

    def has_existing_obj(self, obj):
        return self.model.objects.all().exists()

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return 2
        elif self.has_existing_obj(obj):
            return 1
        return 2


class MasterAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = [
        "salon",
    ]
    inlines = [
        SocialAccountInline,
        SessionInline,
        ReviewInline,
        AppointmentInline,
        ConsultationInline,
    ]
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {"all": ("css/admin/ImageUploader.css",)}


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ["id", "master"]
    list_filter = ["master"]

    def has_existing_obj(self, obj):
        return self.model.objects.all().exists()

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return 2
        elif self.has_existing_obj(obj):
            return 1
        return 2

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return super().get_list_filter(request)
        master = Master.objects.filter(user=request.user).first()
        if master:
            return []


admin.site.register(Works)
admin.site.register(Master, MasterAdmin)
admin.site.register(TattooType)
admin.site.site_title = "BARAKA tattoo"
admin.site.site_header = "BARAKA tattoo"
