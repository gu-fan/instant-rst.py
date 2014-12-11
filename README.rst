#################
InstantRst Server
#################

:version: 0.9.0.5

**WHAT'S NEW**
    Now, You Can View The Page within lan.



This is a server for preview rst document instantly.

You can use it with instantRst.vim_


.. figure:: https://github.com/Rykka/github_things/raw/master/image/rst_quick_start.gif
    :align: center

    riv.vim_ (vim) +  InstantRst_ (web server) +  rhythm.css_ (theme)

----


Install
=======

.. code:: sh

   # Got some issue on pypi
   # sudo pip install instant-rst
   sudo pip install https://github.com/Rykka/instant-rst.py/archive/master.zip

Useage
======

usage: instantRst [-h] [-f FILENAME] [-b BROWSER] [-p PORT] [-s STATIC_DIR] [-t TEMPLATE_DIR]

optional arguments:

-h, --help          
                    show this help message and exit
-f FILENAME, --file FILENAME
                    The local filename for Converting
-b BROWSER, --browser BROWSER
                    The browser command for viewing
                    Default is 'firefox'
-p PORT, --port PORT  The port for server to use
                      Default is '5676'
-t TEMPLATE_DIR, --template-dir TEMPLATE_DIR 
                      Directory containing a template to 
                      be used when rendering the output. 
                      Defaults to a bundled rhythm.css_
-s STATIC_DIR, --static-dir STATIC_DIR 
                      The directory containing static 
                      files used by the template.
                      Defaults to a bundled rhythm.css_


To convert a rst document
    You can start with ``instantRst -f file.rst``

    Then the brower will opened the converted file at ``http://localhost:<port>``

API
===

+----------------------+------------+----------------------------+---------------------------------------------------------------+
| Action               | Http       |  Request Body or Param     | Curl Command                                                  |
|                      | Method     |                            |                                                               |
+======================+============+============================+===============================================================+
| Show Converted file  |  ``GET``   | ``?file=/pat/to/file.rst`` | ``curl http://localhost:5676?file=/tmp/test.rst``             |
|                      |            |                            |                                                               |
|                      |            | When file is omitted,      |                                                               |
|                      |            | Then a default index page  |                                                               |
|                      |            | will be opened.            |                                                               |
+----------------------+------------+----------------------------+---------------------------------------------------------------+
| Refresh window with  |  ``POST``  | ``{file:file.rst, p:pos}`` | ``curl -d file='file.name' -d p='0.3' http://localhost:5676`` |
|                      |            |                            |                                                               |
|                      |            | When file is omitted,      |                                                               |
| a file and scroll to |  or        | Then will only scroll to   |                                                               |
| a position(a float)  |  ``PUT``   | that pos                   |                                                               |
+----------------------+------------+----------------------------+---------------------------------------------------------------+
| Close Server         | ``DELETE`` |                            | ``curl -X DELETE http://localhost:5676``                      |
+----------------------+------------+----------------------------+---------------------------------------------------------------+

.. _instantRst.vim: https://github.com/Rykka/InstantRst
.. _riv.vim: https://github.com/Rykka/riv.vim
.. _rhythm.css: https://github.com/Rykka/rhythm.css
.. _InstantRst: https://github.com/Rykka/InstantRst

Issues
------
for debian user, you may need to install gevent manually

::

    sudo apt-get install libevent-dev
    sudo apt-get install python-all-dev
    sudo pip install greenlet
    sudo pip install gevent



