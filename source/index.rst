.. |buildcore| image:: https://travis-ci.org/pyfarm/pyfarm-core.svg?branch=master
    :target: https://travis-ci.org/pyfarm/pyfarm-core
    :alt: Build Status

.. |buildmaster| image:: https://travis-ci.org/pyfarm/pyfarm-master.svg?branch=master
    :target: https://travis-ci.org/pyfarm/pyfarm-master
    :alt: Build Status

.. |buildagent| image:: https://travis-ci.org/pyfarm/pyfarm-agent.svg?branch=master
    :target: https://travis-ci.org/pyfarm/pyfarm-agent
    :alt: Build Status

.. |coveragecore| image:: https://coveralls.io/repos/pyfarm/pyfarm-core/badge.png?branch=master
    :target: https://coveralls.io/r/pyfarm/pyfarm-core?branch=master
    :alt: Code Coverage

.. |coverageagent| image:: https://coveralls.io/repos/pyfarm/pyfarm-agent/badge.png?branch=master
    :target: https://coveralls.io/r/pyfarm/pyfarm-agent?branch=master
    :alt: Code Coverage

.. |coveragemaster| image:: https://coveralls.io/repos/pyfarm/pyfarm-master/badge.png?branch=master
    :target: https://coveralls.io/r/pyfarm/pyfarm-master?branch=master
    :alt: Code Coverage


PyFarm - A Python Based Distributed Job System
==============================================

.. attention::
    These documents are still undergoing revision

PyFarm is a Python based distributed job system which is intended to be easy
to deploy and maintain. Initially developed for individual use new revisions
have been engineered with larger deployments in mind.  It's a system that's
focused on providing a framework for customized command execution while
taking into account resource management.

Since this project is under active development, if you have specific
questions or comments you're always welcome to post to the google groups
`discussion list <https://groups.google.com/forum/#!forum/pyfarm>`_
or via email to pyfarm@googlegroups.com.

Components
----------

PyFarm has several distinct roles that it must fill in order to accomplish
what it was designed to do.  Because of this the project has been broken
down into three components to help manage scope and limit interdependencies
as much as possible.

Core
++++

|buildcore| | |coveragecore| |
`Documentation <../../projects/pyfarm-core/>`_ |
`Source Code <https://github.com/pyfarm/pyfarm-core>`_

This is the base library which provides a few modules and objects which the
other two components of PyFarm use.  The primary purpose of this component
is to centralize code basic functionality such as logging and configuration.

Master
++++++

|buildmaster| | |coveragemaster| |
`Documentation <../../projects/pyfarm-master/>`_ |
`Source Code <https://github.com/pyfarm/pyfarm-master>`_

This is the component responsible for storing jobs and tasks to run as well
as allocation of work to remote hosts.  This component is the largest of the
three components and contains the code necessary to run the web interface,
interact with the relational database, REST APIs and scheduler.

Agent
+++++

|buildagent| | |coverageagent| |
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
