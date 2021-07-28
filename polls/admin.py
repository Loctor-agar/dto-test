from django.contrib import admin

# Register your models here.
from .models import Position, Employee


class PositionAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "position", "status"]


admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)