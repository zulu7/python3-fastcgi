"""
Python bindings for the Open Market FastCGI library
"""

__author__  = "Cody Pisto <cody@hpcs.com>"
__version__ = "1.2"

from fastcgi.Server import ThreadedServer, ForkingServer
from fastcgi.WSGI import ThreadedWSGIServer, ForkingWSGIServer
