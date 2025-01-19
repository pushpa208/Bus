from django.db import models

class Bus(models.Model):
    bus_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()
    trip = models.CharField(max_length=100)
    trip_duration = models.DurationField()
    conductor = models.CharField(max_length=50)
    driver = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.bus_number} - {self.brand}"

from Feature.models import Bus

#Fetch all buses

buses = Bus.objects.all()

for bus in buses:
    print(bus.bus_number, bus.brand, bus.trip)
