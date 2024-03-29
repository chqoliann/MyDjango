from django.contrib import admin
from .models import Doctor, DoctorTime, Patient

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty')

@admin.register(DoctorTime)
class DoctorTimeAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'time')

