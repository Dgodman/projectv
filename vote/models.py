from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from vote.states import STATE_LIST, ADDRESS_TYPES


STATES_DICT = dict(STATE_LIST)


class StateRule(models.Model):
    """
    Model representing state absentee rules
    """
    state = models.ForeignKey('State')
    name = models.CharField(max_length=20, help_text="Generic name (may be used in forms)", default="")
    description = models.TextField(default="")

    class Meta:
        verbose_name_plural = 'state rules'

    def __str__(self):
        return self.name

    def clean_name(self, *args, **kwargs):
        self.name = self.name.upper()
        super(StateRule, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(StateRule, self).save(*args, **kwargs)


class StateException(models.Model):
    """
    Model representing state absentee exceptions
    """
    state = models.ForeignKey('State')
    name = models.CharField(max_length=20, help_text="'<STATE>_<DESCRIPTION>, ex: GA_ILLNESS", default="")
    description = models.TextField(default="")

    class Meta:
        verbose_name_plural = 'state exceptions'

    def __str__(self):
        return self.name

    def clean_name(self, *args, **kwargs):
        self.name = self.name.upper()
        super(StateException, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(StateException, self).save(*args, **kwargs)


class State(models.Model):
    """
    Model representing state information (name, absentee_allowed, absentee_type,)
    """
    # state names
    name_short = models.CharField(max_length=2, help_text="Enter state abbreviation")
    name_long = models.CharField(max_length=30, help_text="Enter state name")
    # state absentee info
    can_vote_by_mail = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return self.name_long

    def clean(self, *args, **kwargs):
        super(State, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(State, self).save(*args, **kwargs)


class Address(models.Model):
    """
    Model representing an address (Democrat, Republican, Libertarian, Unaffiliated)
    """
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    #state = models.CharField(max_length=2)
    state = models.ForeignKey(State)
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
        return self.formatted_address()


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
    # voter information
    user = models.OneToOneField(User)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    suffix_name = models.CharField(_('suffix'), max_length=5, blank=True)
    # postal information
    address = models.ManyToManyField(Address)
    lived_for_month = models.BooleanField(default=True, blank=True)
    date_of_move = models.DateField(blank=True)
    # voter party
    party = models.ForeignKey('Party', blank=True)
    # voter exceptions (based on state)
    exceptions = models.ManyToManyField(
        StateException,
        help_text="Select the absentee exceptions for this user (based on state)",
        blank=True,
    )

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
