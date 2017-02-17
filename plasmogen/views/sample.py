import logging

log = logging.getLogger(__name__)

from genaf.views import  *

import json

def format_sampleinfo(samples, request):

    T = table(class_='table table-condensed table-striped', id='sample_table')

    data = [
        [   '<a href="%s">%s</a>' % (request.route_url('genaf.sample-view',
                                                id = s.id),
                                    s.code),
            s.altcode,
            s.category,
            s.location.country,
            s.location.level1,
            s.location.level2,
            s.location.level3,
            s.location.level4,
            str(s.collection_date),
            s.day,
        ] for s in samples
    ]

    jscode = '''
var dataset = %s;

$(document).ready(function() {
    $('#sample_table').DataTable( {
        data: dataset,
        paging: false,
        fixedHeader: true,
        columns: [
            { title: "Sample Code" },
            { title: "Alt Code" },
            { title: "Category" },
            { title: "Country" },
            { title: "Admin L1" },
            { title: "Admin L2" },
            { title: "Admin L3" },
            { title: "Admin L4" },
            { title: "Collection Date" },
            { title: "Day"},
        ]
    } );
} );
''' % json.dumps( data )

    return ( str(T), jscode )
