#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urllib,urllib2

def get(url, headers={}):
    req = urllib2.Request(
        url = url,
        headers = headers
    )
    f = urllib2.urlopen(req)
    con = f.read()
    return {'code':f.getcode(), 'content':con}

def post(url, data, headers={}):
    req = urllib2.Request(
        url = url,
        headers = headers
    )
    f = urllib2.urlopen(req, urllib.urlencode(data))
    con = f.read()
    return {'code':f.getcode(), 'content':con}

