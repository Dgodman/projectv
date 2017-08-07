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

ABSENTEE_TYPES = (
    ('NONE', 'no absentee ballots'),
    ('ALL', 'every election'),
    ('1_YEAR', 'every year'),
    ('2_YEAR', 'every two years'),
)

ADDRESS_TYPES = (
    ('MAILING_1', 'mailing address'),
    ('MAILING_2', 'other mailing'),
    ('HOME_1', 'home address'),
)

STATE_ABSENTEE_TYPE = {
    'AL': {
        'absentee_type': 'none'
    },
    'AK': {
        'absentee_type': 'early'
    },
    'AZ': {
        'absentee_type': 'early'
    },
    'AR': {
        'absentee_type': 'early'
    },
    'CA': {
        'absentee_type': 'early'
    },
    'CO': {
        'absentee_type': 'all'
    },
    'CT': {
        'absentee_type': 'none'
    },
    'DC': {
        'absentee_type': 'early'
    },
    'DE': {
        'absentee_type': 'none'
    },
    'FL': {
        'absentee_type': 'early'
    },
    'GA': {
        'absentee_type': 'early'
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
        'absentee_type': 'early',
        'absentee': {
            'can_vote_by_mail': True,
            'general_days_prior': 60,
            'can_be_permanent': False,
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