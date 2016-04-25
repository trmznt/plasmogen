
from genaf.views.tools import genaf_form_factory, input_select, get_dbhandler

def plasmogen_form_factory( request, mode = 'mlgt' ):
    form, code = genaf_form_factory(request, mode)

    form.get('sample_option').set(
    	options = [	('AA', 'All available samples'),
                 	('AP', 'All population (day-0) samples'),
                    ('AS', 'Strict population samples'),
                    ('PS', 'Strict population samples for each differentiation '),
                    ('AU', 'Unique population samples'),
                    ('PU', 'Unique population samples for each differentiation'),
                    ('NP', 'All non-population (e.g. recurrent) samples')
        ],
        value = 'AP',
    )

    form.get('differentiation_fields').add(
        input_select(name='detection_differentiation', label='Detection differentiation',
           	value=0,
            options = [
            	(0, 'No'),
                (1, 'Yes - discard sample without detection information'),
                (2, 'Yes - treat sample without information as passive detection'),
                (3, 'Yes - treat sample without information as active detection'),
                (4, 'Yes - treat sample without information as another category'),
            ]
        )
    )

    markers_field = form.get('marker_ids')
    markers_field.set(extra_control = markers_field.extra_control +
    					' | <a id="APMEN-Pv9">APMEN-Pv9</a>' +
                        ' | <a id="All-Pv">All-Pv</a>' +
                        ' | <a id="All-Pf">All-Pf</a>')
    dbh = get_dbhandler()
    apmen_markers = [ dbh.get_marker(code) for code in
    			['pv/MS1', 'pv/MS5', 'pv/MS8', 'pv/MS10', 'pv/MS12', 'pv/MS16', 'pv/MS20',
    			'pv/msp1F3', 'pv/pv3.27']]
    code += ( "\n$('#APMEN-Pv9').on('click', function() {"
    				"$('#marker_ids').val([%s]).trigger('change'); })"
					% ','.join( '"%d"' % m.id for m in apmen_markers ) )

    return (form, code)
