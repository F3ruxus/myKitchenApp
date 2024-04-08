from django.contrib import admin
from .models import Item

# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    # We are grabbing info from the models.py file and displaying them here
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")

admin.site.register(Item, MenuItemAdmin)