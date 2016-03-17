from pyramid.config import Configurator
from rhombus.lib.utils import cerr, cout, set_dbhandler_class
from rhombus import add_route_view

#from plasmogen.models.handler import DBHandler
import plasmogen.scripts.run
#set_dbhandler_class( DBHandler )

from genaf import includeme as genaf_includeme, init_app
from genaf.views.tools import set_form_factory

from plasmogen.views.tools import plasmogen_form_factory



def includeme( config ):


    # specific PlasmoGen configuration

    add_route_view( config, 'plasmogen.views.subject', 'plasmogen.subject',
        '/subject',
        '/subject/@@action',
        '/subject/{id}@@edit',
        '/subject/{id}@@save',
        ('/subject/{id}', 'view')

    )

    # set essential pages
    config.add_route('home', '/')
    config.add_view('plasmogen.views.home.index', route_name = 'home')

    config.add_route('login', '/login')
    config.add_view('plasmogen.views.home.login', route_name = 'login')

    config.add_route('logout', '/logout')
    config.add_view('plasmogen.views.home.logout', route_name = 'logout')

    add_route_view( config, 'plasmogen.views.docs', 'plasmogen.docs',
        #'/docs{path:.*}@@view',
        #'/docs{path:.*}@@edit',
        #'/docs{path:.*}@@save',
        #'/docs{path:.*}@@action',
        ('/docs{path:.*}', 'index'),
    )

    # include GenAF configuration
    config.include( genaf_includeme)

    config.add_view('plasmogen.views.tools.sample.index', route_name='tools-sample')

    config.override_asset('rhombus:templates/base.mako', 'plasmogen:templates/base.mako')
    config.override_asset('rhombus:templates/plainbase.mako', 'plasmogen:templates/plainbase.mako')


    return config



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    cerr('PlasmoGEN main() in running...')
    config = init_app(global_config, settings, prefix='/mgr')
    config.include(includeme)

    cover_template = settings.get('override.cover', None)
    if cover_template:
        config.override_asset( 'plasmogen:templates/cover.mako', cover_template)

    set_form_factory(plasmogen_form_factory)

    return config.make_wsgi_app()
