.. note::
    this document is a draft, not all commands are present at this time

Commands
========

PyFarm has several commands for managing, running, testing, and development.


Agent
-----

The agent is controlled the ``pyfarm-agent`` command which has numerous flags
for controlling everything from starting the agent to how it should terminate
as well as how it should interact with the master.  For more information on
the options available for each command please see the sections below.


pyfarm-agent
%%%%%%%%%%%%

**TODO**


Master
------

In production the master will typically be run by WSGI server such as uWSGI 
however when working locally or developing something new the ``pyfarm-master``
command line tool can be used.  Please note that much like in production 
``pyfarm-master`` is primarily configured using environment variables.


pyfarm-master
%%%%%%%%%%%%%

**TODO**