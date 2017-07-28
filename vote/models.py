from django.db import models
from .states import STATE_LIST


class Address(models.Model):
    street_number = models.CharField(max_length=20)
    route = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, choices=STATE_LIST)
    zip = models.CharField(max_length=12)

    def __str__(self):
        return self.street_number
