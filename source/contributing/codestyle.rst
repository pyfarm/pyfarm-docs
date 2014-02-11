.. Copyright 2014 Oliver Palmer
..
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..   http://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.


Coding Style
------------
PyFarm developers should follow the conventions set fourth in :pep:`8` unless
told to do so otherwise.  Any exceptions or more specific example will be noted
below and other may be added as time progresses.  Coding style is an important
part of PyFarm because it keeps the code consistent and readable which
contributes to the overall quality of the source code.

One final thing to note is that there are places where there's inconsistencies
in style and there always will be.  It's up to the team to maintain the style
so if you spot something inconsistent with this guide while working you should
always feel free to fix it.

For other areas where there's contention about style the developers should
come to a consensus and then add their findings to this document.

Whitespace
++++++++++
Whitespace is an important component of any Python program.  The below sets
out the standards that PyFarm follows which in practice is not far off
from :pep:`8`

Tabs and Spaces
```````````````
Follow PEP8 and use spaces.  To be more exact when working on PyFarm please
use four spaces.  For non-python source code please also use four spaces unless
the language you're working with explicitly does not allow this.

Basic Syntax Considerations
+++++++++++++++++++++++++++
As with the parts above you should follow :pep:`8` when considering how you
use Python's basic syntax structures.  Below are some additional considerations
that are specific to PyFarm as well as some short explanations.

Quotations
``````````
Python has two forms of quotations ``'`` and ``"``.  Functionally there's not
any difference between two however all code, strings, error messages, etc
should use ``"``.  The exception to this rule is if you need ``"`` inside of
a string, then you should use ``'``: ``'hello "world"'``.  The reason for this
rule is two parts:

    * it's easy to be, and often is, inconsistent when you mix ``'`` and ``"``
    * developers from other languages, such as C++, are more more used to
      using ``"`` for strings instead of ``'``

Standard Documentation
``````````````````````
Docstrings are high encouraged for all callable functions, methods,
classmethods, and staticmethods.  When creating a docstring please use ``"""``
instead of ``'''`` to enclose the documentation.

.. code-block:: python

    def foo():
        """This is a single line doc string"""

    def bar():
        """
        This is a multi-line documentation string.  When you need to
        use multiple lines you should keep the left and right side of
        the opening and closing quotes clear.
        """

Endpoint Documentation
``````````````````````
A large part of PyFarm is :mod:`pyfarm.master` which includes HTTP endpoints
serving as the master's API.  It's important to document these using the
:mod:`sphinxcontrib.httpdomain` syntax so it's readable.  Take special note
that in the top level url the type and name of the thing being posted is in
the url, ``<str:item>``, however in the examples it's the real text.

.. code-block:: python

    from flask.views import MethodView
    class FooItemsAPI(MethodView):
        def post(self, item=None):
            """
            ``POST`` method which

            .. http:post:: /api/v1/foo/<str:item> HTTP/1.1

                **Request**

                .. sourcecode:: http

                    POST /api/v1/foo/foobar HTTP/1.1
                    Accept: application/json

                    {
                        "item": "foobar"
                    }

                **Response (new item created)**

                .. sourcecode:: http

                    HTTP/1.1 201 CREATED
                    Content-Type: application/json

                    {
                        "item": "foobar",
                        "id": 1
                    }

            :statuscode 200: an existing tag was found and returned
            :statuscode 201: a new tag was created
        """

Which ends up looking like this when rendered:

.. http:post:: /api/v1/foo/<str:item> HTTP/1.1

    **Request**

    .. sourcecode:: http

        POST /api/v1/foo/foobar HTTP/1.1
        Accept: application/json

        {
            "item": "foobar"
        }

    **Response (agent newly tagged)**

    .. sourcecode:: http

        HTTP/1.1 201 CREATED
        Content-Type: application/json

        {
            "item": "foobar",
            "id": 1
        }

:statuscode 200: an existing tag was found and returned
:statuscode 201: a new tag was created

Line Continuations
``````````````````
The default max line length for the project is 80 characters.  Anything longer
should use a line continuation if it can't be split up otherwise.

.. code-block:: python

    # import continuations should use (), it's cleaner and easier to
    # modify later on
    try:
        from httplib import (
            BAD_REQUEST, NOT_FOUND, UNAUTHORIZED, INTERNAL_SERVER_ERROR)
    except ImportError:
        from http.client import (
            BAD_REQUEST, NOT_FOUND, UNAUTHORIZED, INTERNAL_SERVER_ERROR)

    # preferred
    message = ("this is a message which you may not be "
               "able to fit onto one linet")

    # but this is ok too
    message = "this is a message which you may not be " \
              "able to fit onto one line"

    # preferred
    if (a == b and c == d and a == b
            or a and b and c and d):
        pass

    # but this is ok too
    if a == b and c == d and a == b \
            or a and b and c and d:
        pass


HTTP Endpoints
++++++++++++++
URL Formatting
``````````````
The following rules should be applied when constructing an HTTP endpoint:

    * endpoints referring to objects should be plural so ``/items/`` instead
      of ``/item/``
    * any endpoint that's not referring to a specific document should
      contain a trailing slash: ``/items/``
    * endpoints that refer to a specific document shouldn't contain a
      trailing slash ``/items/1``
    * when working with groups of items under a single item the trailing
      slash should be added ``/items/1/children/``
    * any endpoint that's an API should contain a version number
      ``/api/v1/items/``


Validating Data in API Endpoints
````````````````````````````````
Most of the time you'll want a standard way of validating the incoming
request before you have to deal with it yourself.  For this there's the
:func:`validate_with_model <pyfarm.master.utility.validate_with_model>`
function that in combination with
:func:`before_request <pyfarm.master.application.before_request>` will:

    * ensure the incoming data to the API is json
    * test the incoming data to ensure it has all the required keys
    * test to make sure the incoming data does not contain keys that don't
      exist in the table
    * check to ensure that all data included matches the expected types based
      on the types in the model
    * set ``flask.g.json`` if all of the above proceed without problems
    * return a useful error message in response to the request if there's
      problems

A short example of how this works is below

.. code-block:: python

    try:
        from httplib import CREATED
    except ImportError:  # pragma: no cover
        from http.client import CREATED

    from flask import g
    from pyfarm.master.application import app, db
    from pyfarm.master.utility import validate_with_model, jsonify
    from pyfarm.models.tag import Tag

    # NOTE: this is an example only, not functional code as it does not
    # setup the route
    @validate_with_model(Tag)  # does all the validation in the points above
    def put_tag():
        model = Tag(**g.json)
        db.session.add(model)
        db.session.commit()
        return jsonify(model.to_dict()), CREATED



Logging
+++++++
General
```````
You are welcome to use the print function on your own but before pushing code
or writing tests please switch to a logger:

.. code-block:: python

    from pyfarm.core.logger import getLogger
    logger = getLogger("foobar")

The above will create a logger under the proper namespace with a reasonable
set of defaults applied.  It will also create it under the proper namespace, in
this case ``pyfarm.foobar``.

.. warning::

    The above is not actually true for the agent and job types.  Those will
    require a special logging setup which is not yet addressed in this guide.

Usage
`````
Below are some general guidelines that apply specifically to logging to
minimize potential performance problems and decrease inconsistencies in
usage.  The following examples assume the code in the section above
was run.

Log Formatting
~~~~~~~~~~~~~~
When providing arguments to the logger use lazy formatting

.. code-block:: python

    greeting = "morning"
    logger.info("good %s", greeting)



Use %r For Objects Instead of repr()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Instead of always calling repr() on the object just use the %r string
formatter

.. code-block:: python

    data = {"true": True, "none", None}
    logger.info("data: %r", data)



Don't Capitalize Partial or Single Sentences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Messages are not really complete sentences in the general sense so we don't
treat them as such here either.

.. note::

    This rule also applies to responses too:

    ``jsonify(error="this is an error")``

.. code-block:: python

    logger.info("this is a single sentence so no capitalization")
    logger.info("There's two sentences here now.  So you should "
                "capitalize them both.")



Exceptions and Errors
+++++++++++++++++++++
At some point you'll have to handle or produce exception within PyFarm.
Depending on where in the code base you're working the patterns may vary so
please see below for more information.

Suppressing All Exceptions
``````````````````````````
Always use ``try: except Exception`` when you must suppress all unhandled
exceptions.  It's also advised that you log the original exception message too
so we can find and better handle these errors in the future.

.. code-block:: python

    try:
        foobar()

    # always document exactly why you're suppressing
    # all unhandled exceptions.  Generally speaking there
    # are **very few** cases where this should ever be a standard
    # practice.
    except Exception as e:
        logger.exception(e)  # this is sometimes skipped
        logger.warning("unhandled exception: %s", e)
        pass

Custom Exceptions
`````````````````
PyFarm used to throw more custom exceptions but since then nearly all of the
code has switched back to using standard exceptions.  In the event a custom
exception must be created it should follow the general pattern below.

.. code-block:: python

    class PyFarmBaseException(Exception):
        """The base exception which all PyFarm exceptions derive from"""
        pass

    # you may optional subclass from a related builtin type too
    class FileHandlingError(PyFarmBaseException):
        """Raised when there's a problem handling files"""
        pass


Throwing Exceptions Inside A Request
````````````````````````````````````
When working with :mod:`pyfarm.master` you'll often need to throw exceptions
that will be used as responses to a request.  There's a couple of ways to do
this:

Default Method
~~~~~~~~~~~~~~
This is the standard method for throwing exceptions in the web application
in response to a request.  The below code will cause
:func:`pyfarm.master.errors.error_400` to produce an error response to the
request depending on the mimietype.  For example if the incoming request it
``application/json`` the below will construct a json response.

.. code-block:: python

    try:
        from httplib import BAD_REQUEST
    except ImportError:  # pragma: no cover
        from http.client import  BAD_REQUEST

    from flask import g, abort
    from pyfarm.master.application import app

    @app.route("/foobar/")
    def foobar():
        # NOTE: like logging incomplete or single sentences should
        # start with a lower case letter
        g.error = "something went wrong"
        abort(BAD_REQUEST)

Alternate Method
~~~~~~~~~~~~~~~~
Although uncommon in other cases it may make sense to response directly when
there's a problem.

.. code-block:: python

    try:
        from httplib import BAD_REQUEST
    except ImportError:  # pragma: no cover
        from http.client import  BAD_REQUEST

    from flask import g, abort
    from pyfarm.master.application import app
    from pyfarm.master.utilities import jsonify

    @app.route("/foobar/")
    def foobar():
        # NOTE: like logging incomplete or single sentences should
        # start with a lower case letter
        return jsonify(error="something went wrong"), BAD_REQUEST


Platform Specific Code
++++++++++++++++++++++
PyFarm is a cross-platform application and because of this some consideration
about support multi-platforms in the same code base must be considered.

Import Handling
```````````````
Imports for platform specific modules should be setup like below.  This is
better than simply ``except ImportError: pass`` because the exception thrown
in the event of misuse will make more sense.  In cases where you've tried the
best you can to determine the proper coarse of action raise an exception that
describes the situation best.


.. code-block:: python

    try:
        from os import fork
    except ImportError:
        fork = NotImplemented

    try:
        import win32process
    except ImportError:
        win32process = NotImplemented

    if fork is NotImplemented and win32process is not NotImplemented:
        subprocess.Popen(
        commands, creationflags=win32process.DETACHED_PROCESS)

    elif fork is not NotImplemented:
        os.fork()

    else:
        raise NotImplemented(
            "failed to determine correct way to launch process")


Internal Logic Handling
```````````````````````
If you're not working with imports like above and you just need to know what
platform you're on use constants from :mod:`pyfarm.core.enums`.

.. code-block:: python

    from pyfarm.core.enums import (
        LINUX, MAC, WINDOWS, POSIX, CASE_SENSITIVE_ENVIRONMENT,
        CASE_SENSITIVE_ENVIRONMENT)



Supporting Multiple Python Versions
+++++++++++++++++++++++++++++++++++
PyFarm supports Python 2.6+ in most modules except for :mod:`pyfarm.agent` or
:mod:`pyfarm.jobtypes` which currently supports only Python 2.6 and Python 2.7
due to problems with Twisted and Python 3.x.  Because of this certain
considerations must be made when working on the project.


Checking Python Versions
````````````````````````
:mod:`pyfarm.core.enums` has some special constants for getting the current
Python version.  There are other ways of checking the Python version however
these constants are provided for consistency and readability.

.. code-block:: python

    from pyfarm.core.enums import PY26, PY26, PY2, PY3


Type Information
````````````````
Certain types consolidated or removed when Python 3 was released.  Because of
this some of the older ways of checking for basic types had to change.  Again
:mod:`pyfarm.core.enums` should be used for consistent and clean behavior
across Python versions.

.. code-block:: python

    from pyfarm.core.enums import STRING_TYPES, NUMERIC_TYPES


2.x vs. 3.x Version Specific Python Imports
```````````````````````````````````````````
Certain built-in imports where also consolidated or renamed when Python 3
came about.  Rather than using constants to do a version check let Python's
import system do the work for you.

.. code-block:: python

    # Python 2.x imports should always go first since
    # most studios and operating systems that ship with Python
    # still default to 2.x
    try:
        from UserDict import UserDict
    except ImportError:  # pragma: no cover
        from collections import UserDict

    # for objects or functions that were renamed
    try:
        _range = xrange
    except NameError:  # pragma: no cover
        _range = range

    # for attributes which have changed
    data = {}
    try:
        items = data.iteritems
    except AttributeError:
        items = data.items

Backwards Compatible Imports
````````````````````````````
Sometimes you'll need access to new functions or modules that don't with
whatever Python version or package you're working with.  In these situations,
like with version specific Python imports, you should use the import system
to make the decision for you.

.. code-block:: python

    # NOTE: Python 2.6 and up includes json, which is what PyFarm requires,
    # this is just an example
    try:
        import json
    except ImportError:  # pragma: no cover
        import simplejson as json

