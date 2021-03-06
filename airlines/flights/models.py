from django.db import models

# Create your models here.

class Airports(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="departures")
    dest = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id}. {self.origin}: {self.destination} - {self.duration}"

class Passenger(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
