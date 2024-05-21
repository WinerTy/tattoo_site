from django.contrib import admin
from django.utils.html import format_html
from django.db import models

from image_uploader_widget.widgets import ImageUploaderWidget

from .models import Works, Master, Note, SocialAccount, Slider


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
class SocialAccountInline(admin.TabularInline):
    model = SocialAccount


class MasterAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["salon",]
    inlines = [SocialAccountInline,]


admin.site.register(Works)
admin.site.register(Master, MasterAdmin)
admin.site.register(Note)
admin.site.register(Slider, SliderAdmin)
