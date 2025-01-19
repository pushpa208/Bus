from django import forms
from .models import Bus

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_number', 'brand', 'number_of_seats', 'trip', 'trip_duration', 'conductor', 'driver']
