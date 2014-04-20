# No shebang line, this module is meant to be imported
#
# Copyright 2014 Oliver Palmer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from collections import namedtuple
from os.path import dirname
from importlib import import_module
from inspect import getfile
from sphinx import apidoc
from textwrap import dedent


def make_options(**kwargs):
    return namedtuple("DummyOptions", kwargs.keys())(**kwargs)

packages = (
    "pyfarm.core",
    "pyfarm.models",
    "pyfarm.master",
    "pyfarm.scheduler",
    "pyfarm.agent",
    "pyfarm.jobtypes")
modules = map(import_module, packages)
options = make_options(
    separatemodules=True,
    noheadings=True,
    destdir=sys.argv[1],
    suffix="rst",
    dryrun=False,
    force=False)

# Write out all the module files
for package_root in map(dirname, map(dirname, map(getfile, modules))):
    apidoc.recurse_tree(package_root, [], options)

# Write out a better index page for pyfarm
index_source = dedent("""
PyFarm Package
==============

Subpackages
-----------

.. toctree::

    pyfarm.core
    pyfarm.models
    pyfarm.master
    pyfarm.scheduler
    pyfarm.agent
    pyfarm.jobtypes
""").strip()

with open(sys.argv[1]+"/pyfarm.rst", "w") as index:
    index.write(index_source)