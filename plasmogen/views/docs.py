
from genaf.views import *
from plasmogen.views import *

from genaf.views import docs
from rhombus.views import fso

import os

@roles( PUBLIC )
def index(request):

    path = request.matchdict.get('path', '')
    if not path:
        return error_page(request, 'ERR - Path not specified!')

    path = os.path.normpath(path)
    if path == '/':
        # root path, just return error page
        return error_page(request, 'ERR - Virtual indexing not allowed!')

    return fso.serve_file(path, mount_point=('/', "plasmogen:docs/"),
        formatter = lambda x: docs.formatter(x, request) )
