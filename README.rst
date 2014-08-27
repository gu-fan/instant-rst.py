#################
InstantRst Server
#################

:version: 0.9

This is a server for preview rst document instantly.

You can use it with instantRst.vim_

Install
=======

.. code:: sh

   # Got some issue on pypi
   # sudo pip install instant-rst
   sudo pip install https://github.com/Rykka/instant-rst.py/archive/master.zip

Useage
======

usage: instantRst [-h] [-f FILENAME] [-b BROWSER] [-p PORT]

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
