
from rhombus.models.ek import EK

def setup(dbsession):
    assert dbsession

    EK.bulk_insert( ek_initlist, dbsession=dbsession)

ek_initlist = [
    (   '@SPECIES', None,
        [   ('Pf', 'P falciparum'),
            ('Pf/Pv', 'Mixed Pf / Pv'),
            ('Pv', 'P vivax')
        ]),

    (   '@BLOOD-WITHDRAWAL', 'Blood widthdrawal method',
        [   'venous',
            'capillary',
        ]),
    (   '@BLOOD-STORAGE', 'Blood storage/source method',
        [   'EDTA',
            'blood tube',
            'filter paper',
        ]),
    (   '@PCR-METHOD', 'PCR identification method', []
        ),
    ]
