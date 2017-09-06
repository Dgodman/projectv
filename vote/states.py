STATE_LIST = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

ADDRESS_TYPES = (
    ('HOME_1', 'Primary home'),
    ('HOME_2', 'Secondary home'),
    ('MAILING_1', 'Primary mailing'),
    ('MAILING_2', 'Secondary mailing'),
)

# EXCEPTIONS WILL BE PREFIXED AS FOLLOWS
# "You will be absent from your polling site on Election Day because..."

STATE_ABSENTEE_TYPE = {
    'AL': {
        'absentee': {
            'type': 'ALLOWED_BUT',
            'can_be_permanent': False,
            'rules': {
                'request_available': '40 days before Election Day',
                'deadline_return': '5 days before Election Day',
            },
            'exceptions': {
                'your military status',
                'you are the spouse or dependant of military',
                'an illness',
                'a physical Disability',
                'you are an appointed election official or poll watcher',
                'you work +10 hours or more during polling hours',
            },
        },
    },
    'AK': {
        'absentee': {
            'type': 'ALLOWED_BUT',
            'can_be_permanent': False,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': '10 days before Election Day',
            },
            'exceptions': {
            },
        },
    },
    'AZ': {
        'absentee': {
            'type': 'ALLOWED',
            'can_be_permanent': False,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': '5pm on the second Friday before Election',
            },
            'exceptions': {
            },
        },
    },
    'AR': {
        'absentee': {
            'type': 'ALLOWED_BUT',
            'can_be_permanent': False,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': '7 days before Election Day',
            },
            'exceptions': {
                'an unavoidable absence',
                'an illness',
                'a physical disability',
                'your military status',
                'you are the spouse or dependant of military',
                'you are registered in this state but temporarily outside',
            },
        },
    },
    'CA': {
        'absentee': {
            'type': 'ALLOWED',
            'can_be_permanent': True,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': '7 days before Election Day',
            },
            'exceptions': {
            },
        },
    },
    'CO': {
        'absentee': {
            'type': 'ALL',
            'can_be_permanent': True,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': 'Tuesday before Election Day',
            },
            'exceptions': {
            },
        },
    },
    'CT': {
        'absentee': {
            'type': 'ALLOWED_BUT',
            'can_be_permanent': False,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': 'Tuesday before Election Day',
            },
            'exceptions': {
                'your military status',
                'an unavoidable absence',
                'an illness',
                'a physical disability',
                'religious beliefs',
                'you are an appointed election official or poll watcher',
            },
        },
    },
    'DC': {
        'absentee': {
            'type': 'ALLOWED',
            'can_be_permanent': False,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': 'Tuesday before Election Day',
            },
            'exceptions': {
            },
        },
    },
    'DE': {
        'absentee': {
            'type': 'ALLOWED_BUT',
            'can_be_permanent': False,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': 'Friday before Election Day',
                'notary_required': True,
            },
            'exceptions': {
                'temporarily residing outside the State',
                'illness',
                'physical disability',
                'public service',
                'military status',
                'spouse or dependant residing outside the State',
            },
        },
    },
    'FL': {
        'absentee': {
            'type': 'ALLOWED',
            'can_be_permanent': False,
            'rules': {
                'request_available': 'January 1st',
                'deadline_return': 'Before 5 p.m. on the 6th day before Election Day',
            },
            'exceptions': {
            },
        },
    },
    'GA': {
        'absentee': {
            'type': 'ALLOWED',
            'can_be_permanent': False,
            'rules': {
                'request_available': '180 days before Election Day',
                'deadline_return': 'Before 5 p.m. on the 6th day before Election Day',
            },
            'exceptions': {
            },
        },
    },
    'HI': {
        'absentee_type': 'early'
    },
    'ID': {
        'absentee_type': 'early'
    },
    'IL': {
        'absentee_type': 'early'
    },
    'IN': {
        'absentee_type': 'early'
    },
    'IA': {
        'absentee_type': 'early'
    },
    'KS': {
        'absentee_type': 'early'
    },
    'KY': {
        'absentee_type': 'none'
    },
    'LA': {
        'absentee_type': 'early'
    },
    'ME': {
        'absentee_type': 'early'
    },
    'MD': {
        'absentee_type': 'early'
    },
    'MA': {
        'absentee_type': 'early'
    },
    'MI': {
        'absentee_type': 'none'
    },
    'MN': {
        'absentee_type': 'early'
    },
    'MS': {
        'absentee_type': 'none'
    },
    'MO': {
        'absentee_type': 'none'
    },
    'MT': {
        'absentee_type': 'early'
    },
    'NE': {
        'absentee_type': 'early'
    },
    'NV': {
        'absentee_type': 'early'
    },
    'NH': {
        'absentee_type': 'none'
    },
    'NJ': {
        'absentee_type': 'early'
    },
    'NM': {
        'absentee_type': 'early'
    },
    'NY': {
        'absentee_type': 'none'
    },
    'NC': {
        'absentee_request': {
            'can_vote_by_mail': True,
            'can_be_permanent': False,
            'rules': {
                'request_available': '50 days before Election Day',
                'deadline_return': 'Tuesday before Election Day by 5:00 p.m',
            },
            'exceptions': {
                None,
            },
        },
        'absentee_ballot': {
            'notary_or_witness': "One public notary or two witnesses are required and will need to sign the ballot."
        },
    },
    'ND': {
        'absentee_type': 'early'
    },
    'OH': {
        'absentee_type': 'early'
    },
    'OK': {
        'absentee_type': 'early'
    },
    'OR': {
        'absentee_type': 'all'
    },
    'PA': {
        'absentee_type': 'none'
    },
    'RI': {
        'absentee_type': 'none'
    },
    'SC': {
        'absentee_type': 'none'
    },
    'SD': {
        'absentee_type': 'early'
    },
    'TN': {
        'absentee_type': 'early'
    },
    'TX': {
        'absentee_type': 'early'
    },
    'UT': {
        'absentee_type': 'early'
    },
    'VT': {
        'absentee_type': 'early'
    },
    'VA': {
        'absentee_type': 'none'
    },
    'WA': {
        'absentee_type': 'all'
    },
    'WV': {
        'absentee_type': 'early'
    },
    'WI': {
        'absentee_type': 'early'
    },
    'WY': {
        'absentee_type': 'early'
    },
}
