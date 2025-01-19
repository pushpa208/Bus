from django.contrib import admin
from .models import Bus

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_number', 'brand', 'number_of_seats', 'trip', 'trip_duration', 'conductor', 'driver')
