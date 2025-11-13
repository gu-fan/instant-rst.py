#!/usr/bin/env python3
from threading import Thread
import argparse
import socket
import sys

from instant_rst.server import sock, app
from instant_rst import util
from instant_rst import settings

import ubelt as ub
import scriptconfig as scfg


class InstantRST_CLI(scfg.DataConfig):
    """
    Preview rst instantly.
    """
    filename = scfg.Value(
        settings.DEFAULT_FILE,
        alias=['file'], short_alias=['f'],
        help='The local filename for Converting',
        position=1)
    browser = scfg.Value(settings.BROWSER, short_alias=['b'], help=ub.paragraph(
            '''
            The browser command for viewing, empty will use default
            '''))
    port = scfg.Value(settings.PORT, short_alias=['p'], help='The port for server to use')
    static_dir = scfg.Value(settings.FLASK_TEMPLATE_FOLDER, short_alias=['s'], help=ub.paragraph(
            '''
            Directory with static files for rendering
            '''))
    template_dir = scfg.Value(settings.FLASK_STATIC_FOLDER, short_alias=['t'], help=ub.paragraph(
            '''
            Directory with template files for rendering
            '''))
    localhost_only = scfg.Value(False, isflag=True, short_alias=['l'], help=ub.paragraph(
            '''
            Only use localhost, disable lan. default: False
            '''))
    additional_dirs = scfg.Value([], alias=['aditional_dir'], short_alias=['d'], help='Additional directories to serve')
    debug = scfg.Value(False, isflag=True, help='debug mode or not')


def make_argparse():
    """
    Ignore:
        from instant_rst.main import *  # NOQA
        import scriptconfig
        parser = make_argparse()
        print(scriptconfig.DataConfig.port_from_argparse(parser, name='InstantRST_CLI'))

    """
    parser = argparse.ArgumentParser(description='Preview rst instantly.')
    parser.add_argument('-f', '--file', dest='filename',
                        default=settings.DEFAULT_FILE,
                        help='The local filename for Converting')
    parser.add_argument('-b', '--browser', dest='browser',
                        default=settings.BROWSER,
                        help='The browser command for viewing, empty will use default')
    parser.add_argument('-p', '--port', dest='port',
                        default=settings.PORT,
                        help='The port for server to use')
    parser.add_argument('-s', '--static-dir', dest='static_dir',
                        default=settings.FLASK_STATIC_FOLDER,
                        help='Directory with static files for rendering')
    parser.add_argument('-t', '--template-dir', dest='template_dir',
                        default=settings.FLASK_TEMPLATE_FOLDER,
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

    return parser


def run():
    try:
        _args = InstantRST_CLI.cli(strict=True, verbose='auto')
    except Exception:
        parser = make_argparse()
        _args = parser.parse_args()

    # Settings are stored in a global module, might be best to change this.
    settings.FLASK_TEMPLATE_FOLDER = _args.template_dir
    settings.FLASK_STATIC_FOLDER = _args.static_dir
    settings.DEFAULT_FILE = _args.filename
    settings.ADDITIONAL_DIRS = _args.additional_dirs
    settings.PORT = _args.port

    if _args.localhost_only:
        settings.HOST = "localhost"
        APP_HOST = "127.0.0.1"
    else:
        # get hostname of local LAN IP
        settings.HOST = socket.gethostbyname(socket.gethostname())
        APP_HOST = "0.0.0.0"

    settings.URL = f"http://{settings.HOST}:{settings.PORT}"

    print(settings.URL)
    settings._p1 = Thread(target=util.delay, args=(1, "browseAndPost", [_args.browser, settings.URL]))
    settings._p2 = Thread(target=sock.run, args=(app,), kwargs={'host': APP_HOST, 'port': settings.PORT})

    try:
        if not _args.debug:
            settings._p1.start()
        # sock.run(app, host=APP_HOST, port=settings.PORT)
        settings._p2.start()
    except Exception:
        print('\nSome error/exception occurred.')
        print(sys.exc_info())
        settings._p1.terminate()
        settings._p2.terminate()
        sys.exit()

if __name__ == '__main__':
    run()
