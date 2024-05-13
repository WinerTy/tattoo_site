from django.contrib import admin
from .models import *


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount


class MasterAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [SocialAccountInline,]


admin.site.register(Works)
admin.site.register(Master, MasterAdmin)
admin.site.register(Note)
admin.site.register(Slider)