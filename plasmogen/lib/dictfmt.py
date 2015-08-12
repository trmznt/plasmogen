from genaf.lib import dictfmt
from io import StringIO


csv_headers = dictfmt.csv_headers.union({ 'PASSIVE_DETECTION', 'AGE', 'GENDER',
                'BLOOD_WITHDRAWAL', 'BLOOD_STORAGE',
                'MICROSCOPY_IDENTITY', 'PCR_IDENTITY', 'PCR_METHOD',
                'RECURRENT', 'RECURRENT_SAMPLE', 'PARASITE_DENSITY',
                'SYMPTOMATIC_STATUS', 'SUBJECT_CODE', 'RELATED_SAMPLE'})



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
            recurrent = r.get('RECURRENT', 'N').strip(),
            recurrent_sample = r.get('RECURRENT_SAMPLE', None),
            parasite_density = r.get('PARASITE_DENSITY', 0),
            symptomatic_status = r.get('SYMPTOMATIC_STATUS', 'N'),
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

