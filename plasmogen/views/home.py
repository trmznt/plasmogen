import logging

log = logging.getLogger( __name__ )

from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from rhombus.views.home import login as rhombus_login, logout as rhombus_logout


def index(request):
    return render_to_response( "plasmogen:templates/home.mako",
                                {}, request=request )


def login(request):
    return rhombus_login(request)


def logout(request):
    return rhombus_logout(request)
