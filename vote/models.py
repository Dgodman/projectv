from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from vote.states import STATE_LIST


class AddressType(models.Model):
    """
    Models representing address types (Home, Mailing, other)
    """
    name = models.CharField(max_length=20, help_text="Enter an address type")

    class Meta:
        verbose_name_plural = 'address types'

    def __str__(self):
        return self.name


class Address(models.Model):
    """
    Model representing an address (Democrat, Republican, Libertarian, Unaffiliated)
    """
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
        return self.street


class Party(models.Model):
    """
    Model representing political parties
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """
    Model representing the user's profile
    """
    user = models.OneToOneField(User)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    suffix_name = models.CharField(_('suffix'), max_length=5, blank=True)
    # postal information
    address = models.ManyToManyField(Address)
    lived_for_month = models.BooleanField(default=True, blank=True)
    date_of_move = models.DateField(blank=True)
    # voter information
    party = models.ForeignKey('Party', blank=True)

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        verbose_name_plural = 'user profiles'
