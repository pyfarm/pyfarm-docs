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


Contributing To PyFarm
======================
Summary
-------
PyFarm is a Python based project with the goal of creating an easy to use and
deploy render farm.  The project is written on top of several existing libraries
including `SQLAlchemy <http://www.sqlalchemy.org/>`_,
`Flask <http://flask.pocoo.org/>`_,
`Twisted <https://twistedmatrix.com/trac/>`_, and many more.  While PyFarm's
original goal is providing the base for running a render farm it can be used
for other types of work as well.

As flexible and easy to use as the project may be, contributions from the
community are always welcome.  There are many ways one can contribute to the
overall project but generally they fall under either documentation, bug fixes,
features, or testing.  With that in mind, if you're looking to contribute to
any of these three areas then read on to get started.


Project Structure
-----------------
Sub-Projects
++++++++++++
The project is broken down into several smaller sub-projects to aid in long
term maintnance and isolation of code scope.  Generally speaking there are two
kinds of sub-projects, supporting and operational.  ``Supporting`` sub-projects
support all consumers of the project in some capacity (ex. documentation or
deployment tools).  ``Operational`` sub-projects contain the code which operate
PyFarm (ex. agent or master).  See the below table to get familiar with the
various sub-projects as they will be referenced later on:

.. some simple subs. for the table below
.. _pyfarm: https://github.com/pyfarm/pyfarm
.. _pyfarm-docs: https://github.com/pyfarm/pyfarm-docs
.. _pyfarm-core: https://github.com/pyfarm/pyfarm-core
.. _pyfarm-models: https://github.com/pyfarm/pyfarm-models
.. _pyfarm-master: https://github.com/pyfarm/pyfarm-master
.. _pyfarm-agent: https://github.com/pyfarm/pyfarm-agent
.. _pyfarm-jobtypes: https://github.com/pyfarm/pyfarm-jobtypes

.. table:: **Sub-Projects of PyFarm**

    ================= =========== ==============================================
    Sub-Project       Type        Description
    ================= =========== ==============================================
    pyfarm_           Supporting  * project wide command line tools
                                  * development tools for tagging and deployment
                                    to PyPi
    pyfarm-docs_      Supporting  * source code to documentation in restructured
                                    text form
                                  * pushes to this repo will:
                                      * build docs at https://readthedocs.org/builds/pyfarm/
    pyfarm-core_      Operational * common library used by all other
                                    operational type sub-projects containing
                                    standard library backports, enums, basic
                                    file handling, base logger, general
                                    utilities, and system information collection
                                  * setup.py **does not** specify all
                                    dependencies, the consuming sub-project will
                                    do this instead (ex. pyfarm-agent specifies
                                    the dependencies that the system information
                                    library needs)
                                  * must support Python 2.5 until Python 3.0
                                    support is added
                                  * pushes to repo will:
                                      * build at https://travis-ci.org/pyfarm/pyfarm-core
                                      * collect coverage at https://coveralls.io/r/pyfarm/pyfarm-core
    ================= =========== ==============================================