import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectv.settings')
django.setup()

from vote.models import Party, State
from vote.states import STATE_LIST


def populate():
    # create parties
    party_list = ['Democrat', 'Republican', 'Independent', 'Libertarian', 'Green', ]
    print("Adding parties")
    for party in party_list:
        add_party(party)
    # create states
    print("Adding states")
    for state in STATE_LIST:
        add_state(state[0], state[1])


def add_party(_name):
    p = Party.objects.get_or_create(name=_name)[0]
    p.save()
    return p


def add_state(_name_short, _name_long):
    s = State.objects.get_or_create(name_short=_name_short, name_long=_name_long)[0]
    s.save()
    return s


if __name__ == '__main__':
    print("Starting population script...")
    populate()
    print("Done")
