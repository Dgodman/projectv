from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from vote.states import STATE_LIST, ADDRESS_TYPES


STATES_DICT = dict(STATE_LIST)


class AbsenteeType(models.Model):
    """
    Model representing state absentee types (every election, over x time, 1 year, 2 years)
    """
    name = models.CharField(max_length=20)
    days_prior = models.IntegerField(
        default=0,
        help_text="Number of days prior to election when absentee requests can be made"
    )
    vote_by_mail = models.BooleanField(default=False, help_text="Allows vote by mail?")

    # initially only doing general elections
    election_type = models.CharField(max_length=10, default="GENERAL")

    class Meta:
        pass

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(AbsenteeType, self).save(*args, **kwargs)


class State(models.Model):
    """
    Model representing state information (name, absentee_allowed, absentee_type,)
    """
    name_short = models.CharField(max_length=2, choices=STATE_LIST, help_text="Enter state abbreviation")
    name_long = models.CharField(max_length=30, help_text="Enter state name")
    absentee_type = models.ForeignKey('AbsenteeType')

    class Meta:
        pass

    def __str__(self):
        return self.name_long

    def get_long(self):
        return STATES_DICT.get(self.name_short, '')

    def clean(self, *args, **kwargs):
        print("test")
        short = self.name_short
        if short:
            name_long = STATES_DICT[self.name_short]
            if name_long:
                self.name_long = name_long
        super(State, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(State, self).save(*args, **kwargs)

'''
class AddressType(models.Model):
    """
    Models representing address types (Home, Mailing, other)
    """
    name = models.CharField(max_length=20, help_text="Enter an address type")

    class Meta:
        verbose_name_plural = 'address types'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(AddressType, self).save(*args, **kwargs)
'''


class Address(models.Model):
    """
    Model representing an address (Democrat, Republican, Libertarian, Unaffiliated)
    """
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.ForeignKey('State')
    zip = models.CharField(max_length=12)
    county = models.CharField(max_length=50)
    address_type = models.CharField(max_length=20, choices=ADDRESS_TYPES)

    def formatted_address(self):
        return "{0} {1}, {2}, {3}".format(
            self.street,
            self.city,
            self.state,
            self.zip
        )

    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self):
        return self.street


class Party(models.Model):
    """
    Model representing political parties
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'parties'

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
