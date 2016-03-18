
from rhombus.lib.utils import cout, cerr
from genaf.lib import query

class FieldBuilder(query.FieldBuilder):

    def passive_detection(self, arg):
        return ( self._eval_arg(arg, self._dbh.Sample.passive_case_detection),
                None )

    def symptomatic_status(self, arg):
        return ( self._eval_arg(arg, self._dbh.Sample.symptomatic_status),
                None )

    def microscopy_identity(self, arg):
        return ( self._eval_ek_arg(arg, self._dbh.Sample.microscopy_id),
                None )

    def blood_withdrawal(self, arg):
        return (self._eval_ek_arg(arg, self._dbh.Sample.method_id),
                None )

    def pcr_identity(self, arg):
        return ( self._eval_ek_arg(arg, self._dbh.Sample.pcr_id),
                None )


class Selector(query.Selector):

    def get_fieldbuilder(self, dbh):
        cerr('>>>> Plasmogen Selector FiledBuilder >>>>')
        return FieldBuilder(dbh)


def set_query_class():
    query.set_query_class(Selector, query.Filter, query.Differentiator)

