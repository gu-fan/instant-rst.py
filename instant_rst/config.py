from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import os

DEFAULT_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),'templates','index.rst')
TEMPLATE_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)),'templates')
STATIC_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)),'static')
DEFAULT_PORT = 5676
DEFAULT_BROWSER = 'firefox'
SECRET_KEY = 'JO34h#F*$HFHA@#&('
