from django.contrib import admin
from .models import Category,Event
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")

class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title","location","startDate","endDate","published")

admin.site.register(Category,CategoryAdmin)
admin.site.register(Event,EventAdmin)