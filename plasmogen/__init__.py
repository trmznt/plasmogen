from pyramid.config import Configurator
from rhombus.lib.utils import cerr, cout, set_dbhandler_class
from rhombus import add_route_view

from plasmogen.models.handler import DBHandler

set_dbhandler_class( DBHandler )

from genaf import includeme as genaf_includeme, init_app


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

    # include GenAF configuration
    config.include( genaf_includeme)

    config.override_asset('rhombus:templates/base.mako', 'plasmogen:templates/base.mako')

    return config



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    cerr('PlasmoGEN main() in running...')
    config = init_app(global_config, settings, prefix='/mgr')
    config.include(includeme)
    return config.make_wsgi_app()