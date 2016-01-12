import os, sys

from flask import Flask, render_template, request, url_for, jsonify, send_from_directory
from flask.ext.socketio import SocketIO, emit

from instant_rst.rst import html_body

from instant_rst.config import DEFAULT_FILE, SECRET_KEY,TEMPLATE_DIR,STATIC_DIR

app = Flask(__name__,
        static_folder=STATIC_DIR,
        template_folder=TEMPLATE_DIR)
# app.debug = True
app.config['SECRET_KEY'] = SECRET_KEY

socketio = SocketIO(app)

URL = 'http://127.0.0.1:5676'
ADDITIONAL_DIRS = []
DYN_STATIC_DIR = ''
def run(host, port, template_dir, static_dir, additional_dirs, default_file):
    app.template_folder = template_dir
    app.static_folder = static_dir
    global URL
    URL =  'http://' + host + ':' + str(port)
    global ADDITIONAL_DIRS
    ADDITIONAL_DIRS = additional_dirs
    global DEFAULT_FILE
    global DYN_STATIC_DIR
    DEFAULT_FILE = default_file if default_file else DEFAULT_FILE
    DYN_STATIC_DIR = os.path.dirname(DEFAULT_FILE) if os.path.isabs(DEFAULT_FILE) else os.path.join(os.getcwd(), os.path.dirname(DEFAULT_FILE))
    print DEFAULT_FILE

    # To open port listening on lan ,we should pass host='0.0.0.0' to flask
    socketio.run(app, port=port, host='0.0.0.0')


@app.route("/<path:directory>/<path:filename>")
def serve_additional_file(directory, filename):
    print 'ADD_STATIC'
    print ADDITIONAL_DIRS
    print additional_dir
    for additional_dir in ADDITIONAL_DIRS:
        if additional_dir == directory:
            # send with a file of relative path
            return send_from_directory(
                    os.path.join(os.getcwd(), additional_dir), 
                    filename)
        elif os.path.basename(additional_dir) == directory:
            return send_from_directory(additional_dir, filename)

    return '', 404


# Dynamically serve static with current directory
@app.route("/_static/<path:filename>")
def serve_static_file(filename):
    print 'DYN_STATIC'
    print DYN_STATIC_DIR
    return send_from_directory(
            DYN_STATIC_DIR, 
            filename)

@app.route("/", methods=['GET','PUT','POST','DELETE'])
def index():

    if request.method == 'PUT' or request.method == 'POST':
        f = request.form.get('file', '')
        p = request.form.get('p', '-1')
        _dir = request.form.get('dir', '')
        print f
        print p
        if _dir:
            print '_DIR'
            print _dir
            global DYN_STATIC_DIR
            DYN_STATIC_DIR = _dir if os.path.isabs(_dir) else os.path.join(os.getcwd(), os.path.dirname(_dir))
        if os.path.isfile(f):
            global DEFAULT_FILE
            DEFAULT_FILE = f
            print DEFAULT_FILE
            with open(f,'r') as rst:
                d = html_body(rst.read().decode('utf8'))
            socketio.emit('updatingContent', {'HTML': d,'p':p})
            return jsonify(success='true',file=f, p=p)
        elif p != '-1':
            socketio.emit('updatingContent', {'p':p})
            return jsonify(success='true',file=f, p=p)
        else:
            return jsonify(success='false',info='File Not Exist',file=f)

    elif request.method == 'DELETE':

        socketio.emit('die', {'exit': 1})
        shutdown_server()

    elif request.method == 'GET':
        print DEFAULT_FILE

        f = request.args.get('file', DEFAULT_FILE)
        if os.path.isfile(f):
            with open(f,'r') as rst:
                d = html_body(rst.read().decode('utf8'))
                return render_template('index.html',HTML=d, url=URL)
        else:
            return render_template('index.html', url=URL)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    console.log(e)
    return render_template('500.html', err=e), 500

def shutdown_server():
    exit = request.environ.get('werkzeug.server.shutdown')
    if exit is None:
        sys.exit()
    exit()

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})
