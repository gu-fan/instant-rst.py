import os

ADDITIONAL_DIRS = []

STATIC_DIR = os.path.join( os.path.dirname(os.path.realpath(__file__)),'templates')
DEFAULT_FILE = os.path.join( os.path.dirname(os.path.realpath(__file__)),'templates', "index.rst")
HOST = "127.0.0.1"
PORT = "5000"
URL =  "http://127.0.0.1:5000"
BROWSER = 'firefox'
SECRET = 'JO34h#F*$HFHA@#&('

FLASK_STATIC_FOLDER = os.path.join( os.path.dirname(os.path.realpath(__file__)),'static')
FLASK_TEMPLATE_FOLDER = os.path.join( os.path.dirname(os.path.realpath(__file__)),'templates')


_p1 = None
_p2 = None
