import time
import os
import sys
from urllib import request, parse
from instant_rst.rst import html_body
from instant_rst import settings


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def delay(t, func, args):
    time.sleep(t)
    # call function in globals with unzipped args[]
    globals()[func](*args)


def browse(browser, url):
    if sys.platform.startswith('darwin'):
        if browser:
            os.system(f'open -a "{browser}" {url} &')
        else:
            os.system(f'open {url} &')
    elif os.name == 'nt':
        if browser:
            os.system(f'start "{browser}" {url}')
        else:
            os.system(f'start {url}')
    elif os.name == 'posix':
        linux = ['xdg-open', 'kioclient', 'exo-open', 'gnome-open', 'cygstart']
        for _open in linux:
            if which(_open):
                if browser:
                    # xdg-open or gnome-open will use the default app only.
                    os.system(f'{browser} {url} &')
                else:
                    os.system(f'{_open} {url} &')
                break


def browseAndPost(browser, url):
    browse(browser, url)
    time.sleep(1)
    # print('post', settings.DEFAULT_FILE, settings.STATIC_DIR )
    post(url, {'file': settings.DEFAULT_FILE, 'dir': settings.STATIC_DIR})
    time.sleep(1)
    # settings._p1.terminate()


def getDir(_dir):
    return _dir if os.path.isabs(_dir) else os.path.join(os.getcwd(), os.path.dirname(_dir))


def post(url, data):
    data = parse.urlencode(data).encode('utf-8')
    # req = request.request(url, data)
    # res = request.urlopen(req)
    with request.urlopen(url, data) as f:
        print(f.read().decode('utf-8'))


def emit_doc(sock, _dir='', _file='', _pos='-1'):

    _dir = str(_dir)
    _file = str(_file)
    _pos = str(_pos)

    if _dir:
        settings.STATIC_DIR = getDir(_dir)

    if os.path.isfile(_file):
        settings.DEFAULT_FILE = _file

        with open(_file, 'r') as _fo:
            _doc = html_body(_fo.read())
            sock.emit('updatingContent', {'HTML': _doc, 'pos': _pos})
            return True

    elif _pos != '-1':
        sock.emit('updatingContent', {'pos': _pos})
        return True

    return False
