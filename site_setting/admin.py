from django.contrib import admin
from .models import Contact, AboutBlock, Salon, SocialAccountIcon, SalonSocial

from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class SalonSocialInline(admin.TabularInline):
    model = SalonSocial
    extra = 1
    max_num = 4
    verbose_name = "Социальная сеть"
    verbose_name_plural = "Социальные сети"


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    max_num = 1
    verbose_name = "Контактная информация"
    verbose_name_plural = "Контактные данные"

    def has_delete_permission(self, request, obj=None):
        return False


class SalonAdmin(admin.ModelAdmin):
    inlines = [ContactInline, SalonSocialInline]
    list_display = ["id", "name", "address", "longitude", "latitude"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "address", "longitude", "latitude", "id"]
    date_hierarchy = "created_at"


class AboutAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "description", "id"]
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {"all": ("css/admin/ImageUploader.css",)}


admin.site.register(Salon, SalonAdmin)
admin.site.register(AboutBlock, AboutAdmin)
admin.site.register(SocialAccountIcon)
