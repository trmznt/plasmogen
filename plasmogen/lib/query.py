
from rhombus.lib.utils import cout, cerr
from genaf.lib import query

class FieldBuilder(query.FieldBuilder):

    def passive_detection(self, arg):
        return ( self._eval_arg(arg, self._dbh.Sample.passive_detection),
                None )

    def symptomatic_status(self, arg):
        return ( self._eval_arg(arg, self._dbh.Sample.symptomatic_status),
                None )


class Selector(query.Selector):

    def get_fieldbuilder(self, dbh):
        cerr('>>>> Plasmogen Selector FiledBuilder >>>>')
        return FieldBuilder(dbh)


def set_query_class():
    query.set_query_class(Selector, query.Filter, query.Differentiator)

