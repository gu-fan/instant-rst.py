import argparse

from instant_rst import settings
from instant_rst.settings import DEFAULT_FILE, PORT, BROWSER, \
    FLASK_TEMPLATE_FOLDER, FLASK_STATIC_FOLDER

def setup(_args):
    settings.FLASK_TEMPLATE_FOLDER = _args.template_dir
    settings.FLASK_STATIC_FOLDER = _args.static_dir
    settings.DEFAULT_FILE = _args.filename
    settings.ADDITIONAL_DIRS = _args.additional_dirs
    settings.PORT = _args.port

def parse():
    parser = argparse.ArgumentParser(description='Preview rst instantly.')
    parser.add_argument('-f', '--file', dest='filename',
                        default=DEFAULT_FILE,
                        help='The local filename for Converting')
    parser.add_argument('-b', '--browser', dest='browser',
                        default=BROWSER,
                        help='The browser command for viewing, empty will use default')
    parser.add_argument('-p', '--port', dest='port',
                        default=PORT,
                        help='The port for server to use')
    parser.add_argument('-s', '--static-dir', dest='static_dir',
                        default=FLASK_STATIC_FOLDER,
                        help='Directory with static files for rendering')
    parser.add_argument('-t', '--template-dir', dest='template_dir',
                        default=FLASK_TEMPLATE_FOLDER,
                        help='Directory with template files for rendering')
    parser.add_argument('-l', '--localhost-only', dest='localhost_only',
                        action='store_true',
                        help='Only use localhost, disable lan. default: False')
    parser.add_argument('-d', '--aditional-dir', dest='additional_dirs',
                        action='append',
                        default=[],
                        help='Additional directories to serve')

    parser.add_argument('--debug',
                        action='store_true',
                        default=False,
                        help='debug mode or not')

    _args = parser.parse_args() 

    setup(_args)

    return _args
