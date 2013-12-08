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


.. note::
    this document is a draft, not all commands are present at this time

Commands
========

PyFarm has several commands for managing, running, testing, and development.


Agent
-----

The agent is run using Twisted's ``twistd`` application which starts a
daemon on the local machine.  ``twistd`` can run the daemon as another user
or even launch the agent directly using the ``-n`` flag.  For help with
``twistd`` see ``-h`` or for help with the agent flags you can run
``twistd pyfarm.agent -n``

.. include:: include/autogen_command_agent_daemon.rst