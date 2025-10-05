from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_number', 'department', 'applied_at')
    search_fields = ('name', 'roll_number', 'department')
