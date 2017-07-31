from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from vote.states import STATE_LIST


class AddressType(models.Model):
    '''
    Models representing address types (Home, Mailing, other)
    '''
    name = models.CharField(max_length=20, help_text="Enter an address type")

    def __str__(self):
        return self.name


class AddressLongForm(models.Model):
    '''
    Model representing an address
    '''
    street_number = models.CharField(max_length=20)
    route = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_LIST)
    zip = models.CharField(max_length=12)
    county = models.CharField(max_length=50)

    def formatted_address(self):
        return "{0} {1}, {2}, {3} {4}".format(
            self.street_number,
            self.route,
            self.city,
            self.state,
            self.zip
        )

    def __str__(self):
        return self.formatted_address()


class AddressShortForm(models.Model):
    '''
    Model representing an address
    '''
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_LIST)
    zip = models.CharField(max_length=12)
    county = models.CharField(max_length=50)
    type = models.ForeignKey('AddressType')

    def formatted_address(self):
        return "{0} {1}, {2}, {3}".format(
            self.street,
            self.city,
            self.state,
            self.zip
        )

    def __str__(self):
        return self.formatted_address()


class UserProfile(models.Model):
    '''
    Model representing the user's profile
    '''
    user = models.OneToOneField(User)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    # postal information
    home_address = models.ForeignKey('Address', )

    def __str__(self):
        return self.user.email
