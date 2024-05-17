from django.contrib import admin
from .models import Contact, AboutBlock, Salon


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    max_num = 1
    verbose_name = "Контактная информация"

    def has_delete_permission(self, request, obj=None):
        return False


class SalonAdmin(admin.ModelAdmin):
    inlines = [ContactInline,]
    list_display = ["id", "name", "address", "longitude", "latitude"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "address", "longitude", "latitude", "id"]
    date_hierarchy = "created_at"


admin.site.register(Salon, SalonAdmin)
admin.site.register(AboutBlock)
