from __future__ import unicode_literals

from django.db import models
from users.models import SIAUser

# Create your models here.

class Booking(models.Model):
    """
    Representation of a flight
    """
    user = models.ForeignKey(SIAUser, null=True)
    from_airport = models.CharField(max_length=200, null=True)
    to_airport = models.CharField(max_length=200, null=True)
    departure_time = models.DateTimeField(null=True)
    arrival_time = models.DateTimeField(null=True)
    price = models.FloatField(null=True)

    class Meta:
        ordering = ['departure_time']

class AttractionTicket(models.Model):
    """
    Representation of a attraction
    """
    user = models.ForeignKey(SIAUser, null=True)
    activityId = models.IntegerField(null=True)
    start_date = models.CharField(max_length=200, null=True)
    end_date = models.CharField(max_length=200, null=True)

    
class Hotel(models.Model):
    """
    Representation of a attraction
    """
    user = models.ForeignKey(SIAUser)
    hotelId = models.IntegerField()
