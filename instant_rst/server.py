from flask import Flask, escape, request, render_template, jsonify, send_from_directory
from flask_socketio import SocketIO

import os, sys, time

from instant_rst.rst import html_body
from instant_rst import settings, util

app = Flask(__name__,
            static_folder=settings.FLASK_STATIC_FOLDER,
            template_folder=settings.FLASK_TEMPLATE_FOLDER)
app.config['SECRET_KEY'] = settings.SECRET
sock = SocketIO(app)

# ROUTE

@app.route('/', methods=['GET'])
def index_get():
    _file = request.args.get('rst', '')
    if os.path.isfile(_file):
        with open(_file,'r') as _fo:
            _doc = html_body(_fo.read())
            return render_template('index.html', HTML=_doc)
    else:
        return render_template('index.html')

@app.route('/', methods=['POST', 'PUT'])
def index_post():
    print(str(request.form))
    if util.emit_doc(sock, 
                    request.form.get('dir',''),
                    request.form.get('file',''),
                    request.form.get('pos', '-1')):
        return jsonify(code=0, msg='success')
    else:
        return jsonify(code=2, msg='file not exist', file=request.form.get('file'))
    return 'error', 502

@app.route('/', methods=['DELETE'])
def index_delete():
    sock.emit('die', {'exit': 1})
    shutdown_server()
    return 'bye'

# FILES

# serve static with additional directories
@app.route("/<path:directory>/<path:filename>")
def serve_additional_file(directory, filename):
    for additional_dir in settings.ADDITIONAL_DIRS:
        base_dir = os.path.basename(os.path.normpath(additional_dir))
        if base_dir != directory:
            continue

        if os.path.isabs(additional_dir):
            return send_from_directory(additional_dir, filename)

    # if empty use the default dir's sub directory
    if settings.STATIC_DIR and filename:
        full_path = os.path.join(settings.STATIC_DIR, directory)
        if os.path.isabs(full_path):
            return send_from_directory(full_path, filename)

    return '', 404


# serve static with current directory
@app.route("/_static/<path:filename>")
@app.route("/<path:filename>")
def serve_static_file(filename):
    print("serve", settings.STATIC_DIR)
    if settings.STATIC_DIR and filename:
        return send_from_directory(
                settings.STATIC_DIR, 
                filename)
    else:
        return '', 404


# SOCKET

@sock.on('file')
def handler(detail):
    print('received file: ' + str(detail))
    util.emit_doc(sock, 
             detail.get('dir',''),
             detail.get('file',''),
             detail.get('pos', ''))

@sock.on('message')
def handler(message):
    print('received message: ' + message)


# ERROR

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html', err=e), 500

def shutdown_server():
    # time.sleep(0.5)
    # settings._p2.terminate()
    # settings._p2.join()
    exit = request.environ.get('werkzeug.server.shutdown')
    if exit is None:
        sys.exit()
    else:
        exit()


