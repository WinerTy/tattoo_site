from django.contrib import admin
from .models import Works, Master, Note, SocialAccount, Slider


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount


class MasterAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["salon",]
    inlines = [SocialAccountInline,]


admin.site.register(Works)
admin.site.register(Master, MasterAdmin)
admin.site.register(Note)
admin.site.register(Slider)
