from django.contrib import admin
from django.utils.html import format_html
from django.db import models

from image_uploader_widget.widgets import ImageUploaderWidget

from .models import Contact, AboutBlock, Salon, SocialAccountIcon, SalonSocial, Slider


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

    class Media:
        js = ("admin/js/contact.js",)

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


admin.site.register(Salon, SalonAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(AboutBlock, AboutAdmin)
admin.site.register(SocialAccountIcon)
