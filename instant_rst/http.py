#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error,urllib.request,urllib.error,urllib.parse

def get(url, headers={}):
    req = urllib.request.Request(
        url = url,
        headers = headers
    )
    f = urllib.request.urlopen(req)
    con = f.read()
    return {'code':f.getcode(), 'content':con}

def post(url, data, headers={}):
    req = urllib.request.Request(
        url = url,
        headers = headers
    )
    f = urllib.request.urlopen(req, urllib.parse.urlencode(data).encode('utf-8'))
    con = f.read()
    return {'code':f.getcode(), 'content':con}

