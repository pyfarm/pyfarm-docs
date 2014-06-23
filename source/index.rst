.. |status_core| image:: https://travis-ci.org/pyfarm/pyfarm-core.svg?branch=master
.. |status_master| image:: https://travis-ci.org/pyfarm/pyfarm-master.svg?branch=master
.. |status_agent| image:: https://travis-ci.org/pyfarm/pyfarm-agent.svg?branch=master
.. |coverage_core| image:: https://coveralls.io/repos/pyfarm/pyfarm-core/badge.png?branch=master
.. |coverage_master| image:: https://coveralls.io/repos/pyfarm/pyfarm-master/badge.png?branch=master
.. |coverage_agent| image:: https://coveralls.io/repos/pyfarm/pyfarm-agent/badge.png?branch=master

PyFarm - A Python Based Distributed Job System
==============================================

.. attention::
    These documents are still undergoing revision

PyFarm is a Python based distributed job system which is intended to be easy
to deploy and maintain. Initially developed for individual use new revisions
have been engineered with larger deployments in mind.  It's a system that's
focused on providing a framework for customized command execution while
taking into account resource management.

Components
----------

PyFarm has several distinct roles that it must fill in order to accomplish
what it was designed to do.  Because of this the project has been broken
down into three components to help manage scope and limit interdependencies
as much as possible.

Core
++++

|status_core| | |coverage_core| |
`Documentation <../../projects/pyfarm-core/>`_ |
`Source Code <https://github.com/pyfarm/pyfarm-core>`_

This is the base library which provides a few modules and objects which the
other two components of PyFarm use.  The primary purpose of this component
is to centralize code basic functionality such as logging and configuration.

Master
++++++

|status_master| | |coverage_master| |
`Documentation <../../projects/pyfarm-master/>`_ |
`Source Code <https://github.com/pyfarm/pyfarm-master>`_

This is the component responsible for storing jobs and tasks to run as well
as allocation of work to remote hosts.  This component is the largest of the
three components and contains the code necessary to run the web interface,
interact with the relational database, REST APIs and scheduler.

Agent
+++++

|status_agent| | |coverage_agent| |
`Documentation <../../projects/pyfarm-agent/>`_ |
`Source Code <https://github.com/pyfarm/pyfarm-agent>`_

This component controls the execution of commands on remote systems as
instructed by the master.  This component also contains the job types which
are used as a framework for executing commands.

**Contents**

.. toctree::
    :maxdepth: 3

    contributing/index
    requirements
    install
    license



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
