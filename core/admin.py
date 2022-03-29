from django.contrib import admin
from core import models

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'modified_at', 'active']
    search_fields = ['name']
    list_display_links = ['id', 'name', 'modified_at', 'active']

@admin.register(models.Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'modified_at', 'active']
    search_fields = ['name']
    list_display_links = ['id', 'name', 'modified_at', 'active']

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','gender', 'modified_at', 'active']
    search_fields = ['name']
    list_display_links = ['id', 'name','gender', 'modified_at', 'active']