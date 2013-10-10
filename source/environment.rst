.. Copyright 2013 Oliver Palmer
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


Environment Variables
======================
PyFarm has several environment variables which can be used to change the
operation at runtime.  For more information see the individual sections
below.

.. note::
    Not all environment variables defined below are directly used by
    PyFarm.  Many of these values are provided to make it easier to group
    settings together and so settings for PyFarm won't conflict with any
    existing software.


Master
------
Environment variables that are used within the server processes on the
master.

.. envvar:: PYFARM_CONFIG

    Controls which configuration should be loaded.  Currently the only
    supported values are `debug` and `prod` and the configuration itself
    is handled internally.

.. envvar:: PYFARM_DATABASE_URI

    The URI to connect to the backend database.  This should be a valid
    `sqlalchemy uri <http://docs.sqlalchemy.org/en/rel_0_8/core/engines.html#database-urls>`_
    which looks something like this::

        dialect+driver://user:password@host/dbname[?key=value..]




.. envvar:: PYFARM_SECRET_KEY

    When present this value is used by forms and the password storage as
    a seed value for several operations.

.. envvar:: PYFARM_CSRF_SESSION_KEY

    Key used to set the cross site request forgery key for use
    by :mod:`wtforms`.  If not provided this will be set to
    :envvar:`PYFARM_SECRET_KEY`


.. envvar:: PYFARM_JSON_PRETTY

    If set to `true` then all json output by the REST api will be human
    readable.  Setting :envvar:`PYFARM_CONFIG` to `debug` will also produce
    the same effect.