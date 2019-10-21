#!/usr/bin/env python3
from multiprocessing import Process
from threading import Thread
import socket
import sys 

from instant_rst.server import sock, app
from instant_rst import util, args, settings

_args = args.parse()

if _args.localhost_only:
    settings.HOST = "localhost"
    APP_HOST = "127.0.0.1"
else:
    # get hostname of local LAN IP
    settings.HOST = socket.gethostbyname(socket.gethostname())
    APP_HOST = "0.0.0.0"

settings.URL = f"http://{settings.HOST}:{settings.PORT}"

def run():
    settings._p1 = Thread(target=util.delay, args=(1, "browseAndPost", [_args.browser, settings.URL]))
    settings._p2 = Thread(target=sock.run, args=(app,), kwargs={'host':APP_HOST,'port':settings.PORT})

    try:
        if not _args.debug:
            settings._p1.start()
        # sock.run(app, host=APP_HOST, port=settings.PORT)
        settings._p2.start()
    except:
        print('\nSome error/exception occurred.')
        print(sys.exc_info())
        settings._p1.terminate()
        settings._p2.terminate()
        sys.exit()

if __name__ == '__main__':
    run()
