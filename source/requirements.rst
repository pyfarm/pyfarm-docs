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

Requirements
============

This document covers the basic requirements for installation and operation of
PyFarm.  These are the requirements to run PyFarm itself regardless of the
service being executed.  These requirements do **not** cover the software
PyFarm may be executing or the infrastructure required.

Summary
-------

* **Python** Depending on the module being used, different versions of Python
  may be supported.  Eventually Python 2.5 support will be dropped however this
  likely will not happen until Python 3.0 support is added.  In any case, notice
  will be provided well in advance of a release if any of the below changes.

    .. csv-table:: **Module Specific Python Version Support**
        :header: Module, Python Version
        :widths: 10, 50

        :mod:`pyfarm.core`,2.5 - 2.7
        :mod:`pyfarm.api`,2.5 - 2.7
        :mod:`pyfarm.agent`,2.5 - 2.7
        :mod:`pyfarm.master`,2.7 (2.6 should work too but is untested)

* **Operation System** Linux, Mac, and Windows.  Some features may be limited
  on disabled on certain platforms.

* **Memory** 64MB of memory, more may be required to run some components

* **Storage** 128MB of disk space

Database
--------

PyFarm stores a large amount of the information it needs to operate in a
relational database.  Cross database support is provided by
`SQLAlchemy <http://www.sqlalchemy.org/>`_, for more information on
supported databases see
`this document <http://docs.sqlalchemy.org/en/rel_0_8/dialects/index.html>`_.

Python
------
There's not currently a `requirements.txt` file associated with this
project because of the differences in dependencies between Python versions.
PyFarm however can still be installed into a virtual environment using pip:::

    pip install -e . --egg

By doing this you ``pip`` will download and install all the necessary
requirements for your specific Python version and platform.

Supported Software (Job Types)
------------------------------

PyFarm 1.0.0 provides several job types out of the box.  Each of these software
packages will have their own requirements as well so please visit the
manufacturers website for more information.

* Maya
* Houdini
* Nuke

If you wish to request a new builtin type or check the integration status of
one checkout their tickets
`on github <https://github.com/pyfarm/pyfarm-jobtypes/issues?state=open>`_