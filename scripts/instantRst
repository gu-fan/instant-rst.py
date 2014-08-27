#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
''' Simply open browser 1 seconds after start server,
    As we don't want to use hooking
    which need rewrite HttpServer.run() '''
import time
import sys,os

from multiprocessing import Process

from instant_rst import args
from instant_rst.http import post
from instant_rst.server import socketio,app 

def browse(b, port, filename):
    time.sleep(1)
    url = 'http://localhost:'+port
    os.system(b+'  ' + url+ ' &')
    time.sleep(1)
    post(url, {'file': filename})

ag = args.parse()

p = Process(target=browse, args=(ag.browser, ag.port, ag.filename))
p.start()

try:
    socketio.run(app, port=int(ag.port))
except:
    print '\nSome error/exception occurred.'
    print sys.exc_info()
    p.terminate()
    sys.exit()
