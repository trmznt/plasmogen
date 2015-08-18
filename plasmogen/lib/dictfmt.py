from genaf.lib import dictfmt
from io import StringIO


csv_headers = dictfmt.csv_headers.union({ 'PASSIVE_DETECTION', 'AGE', 'GENDER',
                'BLOOD_WITHDRAWAL', 'BLOOD_STORAGE',
                'MICROSCOPY_IDENTITY', 'PCR_IDENTITY', 'PCR_METHOD',
                'PARASITE_DENSITY', 'SYMPTOMATIC_STATUS',
                'DAY', 'RECURRENT', 'SUBJECT_CODE', 'RELATED_SAMPLE'})



def csv2dict(istream, with_report=False, delimiter = '\t'):

    (reader, errlog) = dictfmt.reader_from_stream( istream, csv_headers, delimiter )

    #samples, log = dictfmt.parse_csv( reader, log, sample_func = update_sample )

    return dictfmt.parse_csv( reader, errlog, sample_func = update_sample)


def update_sample( sample, r ):
    """ updating sample dictionary with spesific PlasmoMS field data """

    sample.update(
        dict(
            case_detection = r.get('PASSIVE_DETECTION', 'X'),
            gender = r.get('GENDER', 'X'),
            method = r.get('BLOOD_WITHDRAWAL', '').strip(),
            storage = r.get('BLOOD_STORAGE', '').strip(),
            microscopy = r.get('MICROSCOPY_IDENTITY', '').strip(),
            pcr = r.get('PCR_IDENTITY', '').strip(),
            pcr_method = r.get('PCR_METHOD', '').strip(),
            parasite_density = int(r.get('PARASITE_DENSITY','') or 0),
            symptomatic_status = r.get('SYMPTOMATIC_STATUS', 'N'),
            day = int(r.get('DAY','') or 0),
            recurrent = r.get('RECURRENT', 'N').strip(),
            subject_code = r.get('SUBJECT_CODE', None),
            related_sample = r.get('RELATED_SAMPLE', None),

        )
    )

    age = int(r.get('AGE', '') or 0)
    if age == 0:
        sample.update(
            dict(
                yearofbirth = 0,
                age = 0
            )
        )
    else:
        sample_date = dictfmt.parse_date( sample['collection_date'] )
        sample.update(
            dict(
                yearofbirth = sample_date.year - age,
                age = age
            )
        )

