from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"



class Flight(models.Model):
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    depart_time = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.DurationField(null=True)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    airline = models.CharField(max_length=64)
    economy_fare = models.FloatField(null=True)
    business_fare = models.FloatField(null=True)
    first_fare = models.FloatField(null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

