# sample summary


from genaf.views.tools import *

from rhombus.lib.utils import get_dbhandler
from rhombus.lib import fsoverlay as fso

from collections import defaultdict


@roles(PUBLIC)
def index(request):

    return process_request( request, 'Sample Summary', 'Summarize Samples',
            callback = func_callback, mode = 'allele' )


def func_callback( query, request ):

    analytical_sets = query.get_filtered_analytical_sets()

    results = summarize_sample(analytical_sets)
    options = {}

    html, code = format_output(results, options)

    return ("Sample/Metadata Summary Report", html, code)


def format_output(results, options):

    html = div()
    for r in results:

        html.add( row( div(h4(r['label'], class_='col-md-4') )) )

        for key in [ 'passive_detection', 'symptomatic_status',
                     'pcr_identity', 'microscopy_identity',
                     'blood_withdrawal', 'imported_case',
                     'gender' ]:

            tab = table(class_='table table-condensed table-striped')
            tab.add( thead()[ tr( th(b(key)), th('N') )] )
            tb = tbody()
            for (k,v) in r[key].items():
                tb.add( tr( td(k), td(v) ) )
            tab.add(tb)

            html.add( row(div(class_='col-md-4 col-md-offset-2').add( tab ) ) )

    return (html, '')



def summarize_sample(analytical_sets):

    results = []
    dbh = get_dbhandler()

    for a_set in analytical_sets:
        d = {   'label': None,
                'passive_detection': [],
                'symptomatic_status': [],
                'pcr_identity': [],
                'microscopy_identity': [],
                'blood_withdrawal': [],
                'gender': [],
                'imported_case': [],
            }
        d['label'] = a_set.label

        for s_id in a_set.sample_ids:
            sample = dbh.get_sample_by_id(s_id)
            d['passive_detection'].append( sample.passive_case_detection )
            d['symptomatic_status'].append( sample.symptomatic_status )
            d['pcr_identity'].append( sample.pcr )
            d['microscopy_identity'].append( sample.microscopy )
            d['blood_withdrawal'].append( sample.method )
            d['gender'].append( sample.subject.gender )
            d['imported_case'].append( sample.imported_case )


        d['passive_detection'] = summarize_field( d['passive_detection'] )
        d['symptomatic_status'] = summarize_field( d['symptomatic_status'] )
        d['pcr_identity'] = summarize_field( d['pcr_identity'] )
        d['microscopy_identity'] = summarize_field( d['microscopy_identity'] )
        d['blood_withdrawal'] = summarize_field( d['blood_withdrawal'] )
        d['gender'] = summarize_field( d['gender'] )
        d['imported_case'] = summarize_field( d['imported_case'] )

        results.append( d )

    return results


def summarize_field(fields):

    t = defaultdict(int)
    for s in fields:
        t[s] += 1

    return t


