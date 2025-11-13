#################
InstantRst Server
#################

:version: 0.9.9.1


**WHAT'S NEW**

TOTALLY REWRITED, now python 3.0 only #22.  and support local image #13

will be a stable version.

only tested on Mac OS, please post issues and PR if have problems.

**DEPRECATED**

This is project will no more adding new features

Future project update will be found in http://github.com/ReadyState/inkup

This is a local server for preview rst document instantly.

You can use it with instantRst.vim_

.. figure:: https://github.com/Rykka/github_things/raw/master/image/rst_quick_start.gif
    :align: center

    riv.vim_ (vim) +  InstantRst_ (web server) +  mars.css_ (theme)


Install
=======

.. code:: sh

   # Got some issue on pypi
   # sudo pip install instant-rst

   sudo pip3 install https://github.com/Rykka/instant-rst.py/archive/master.zip

Usage
=====

usage: instantRst [-h] [-f FILENAME] [-b BROWSER] [-p PORT] [-s STATIC_DIR] [-t TEMPLATE_DIR]

optional arguments:

-h, --help
                    show this help message and exit
-f FILENAME, --file FILENAME
                    The local filename for Converting
-b BROWSER, --browser BROWSER
                    The browser command for viewing
                    Default is '' for using system default
-p PORT, --port PORT  The port for server to use
                      Default is '5676'
-t TEMPLATE_DIR, --template-dir TEMPLATE_DIR
                      Directory containing a template to
                      be used when rendering the output.
                      Defaults to a bundled ``rhythm.css_``
-s STATIC_DIR, --static-dir STATIC_DIR
                      The directory containing static
                      files used by the template.
                      Defaults to a bundled ``rhythm.css_``
-l, --localhost-only
                      Only use localhost, disable lan ip
                      default: False

-d, --additional-dir
                      Additional directories to serve.
                      One time per directory.
--debug-dir
                      Debug mode,
                      Do not open browser


To convert a rst document
    You can start with ``instantRst -f file.rst``

    Then the brower will opened the converted file at ``http://localhost:<port>``

API
===

+----------------------+------------+-------------------------------------+-----------------------------------------------------------------------------+
| Action               | Http       |  Request Body or Param              | Curl Command                                                                |
|                      | Method     |                                     |                                                                             |
+======================+============+=====================================+=============================================================================+
| Show Converted file  |  ``GET``   | ``?file=/pat/to/file.rst``          | ``curl http://localhost:5676?file=/tmp/test.rst``                           |
|                      |            |                                     |                                                                             |
|                      |            | When file is omitted,               |                                                                             |
|                      |            | Then a default index page           |                                                                             |
|                      |            | will be opened.                     |                                                                             |
+----------------------+------------+-------------------------------------+-----------------------------------------------------------------------------+
| Refresh window with  |  ``POST``  | ``{file:file.rst, p:pos, dir:dir}`` | ``curl -d file='file.name' -d p='0.3' -p dir='test' http://localhost:5676`` |
|                      |            |                                     |                                                                             |
|                      |            | file: the file to show              |                                                                             |
|                      |            |                                     |                                                                             |
|                      |            | dir: the static dir                 |                                                                             |
|                      |            |                                     |                                                                             |
|                      |            | p: the cursor position              |                                                                             |
|                      |            |                                     |                                                                             |
|                      |            | When file/dir is omitted,           |                                                                             |
| a file and scroll to |  or        | Then will only scroll to            |                                                                             |
| a position(a float)  |  ``PUT``   | that pos                            |                                                                             |
+----------------------+------------+-------------------------------------+-----------------------------------------------------------------------------+
| Close Server         | ``DELETE`` |                                     | ``curl -X DELETE http://localhost:5676``                                    |
+----------------------+------------+-------------------------------------+-----------------------------------------------------------------------------+

.. _instantRst.vim: https://github.com/Rykka/InstantRst
.. _riv.vim: https://github.com/Rykka/riv.vim
.. _mars.css: https://github.com/Rykka/mars.css
.. _InstantRst: https://github.com/Rykka/InstantRst

Issues
------
for debian user, you may need to install gevent manually

::

    sudo apt-get install libevent-dev
    sudo apt-get install python-all-dev
    sudo pip install greenlet
    sudo pip install gevent

STATIC FILES
============

0. Default Static file:

   the ``static/main.css|js`` is served there

   The instant rst's default theme is set there.

   You can pass the ``-s`` for default static directory.

1. Additional Static file:

   You can pass the ``-d`` for additional static directory.

   The basename of the directory is used as the static file's STATIC URL

   e.g.:

       You have a file named ``test/test.jpg``

       You can start instantRst with ``instantRst -f test/test.rst -d test``

       then the file is served with ``localhost:5676/test/test.jpg``

2. Dynamic static file:

   When using with dynamic files, you can post with '-dir=DYN_DIR_NAME' to update the ``DYN_STATIC_DIR``

   e.g.:

       You have a file named ``test/test.jpg``

       When you start instantRst ``instantRst -f test/test.rst``

       The file is served with ``localhost:5676/_static/test.jpg``

       When you switch to another file like ``test1/test.rst``
       Then you can post with ``dir=test1`` or ``dir=~/rst/test1`` to change
       the static dir.

Develop
=======

Contribution are welcomed.

git clone the project::

    git clone

install local package::

    sudo pip install . --upgrade

start test with local package::

    # localhost:5000
    python -m instant_rst -f README.rst

change to static/template file should change setup.py and manifest.in

publish to pypi::

    # register
    # python setup.py register -r pypi

    python setup.py sdist upload -r pypi


Error
=====

1. the template_dir option is not working
