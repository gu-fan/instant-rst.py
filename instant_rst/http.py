#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

def get(url, headers={}):
    req = Request(
        url = url,
        headers = headers
    )
    f = urlopen(req)
    con = f.read()
    return {'code':f.getcode(), 'content':con}

def post(url, data, headers={}):
    req = Request(
        url = url,
        headers = headers
    )
    f = urlopen(req, urlencode(data).encode('utf-8'))
    con = f.read()
    return {'code':f.getcode(), 'content':con}

