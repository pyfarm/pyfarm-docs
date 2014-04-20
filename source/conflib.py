# No shebang line, this module is meant to be imported
#
# Copyright 2013 Oliver Palmer
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

import ast
import shutil
import sys
import tempfile
import urllib2
from StringIO import StringIO
from os.path import join, isfile, realpath, dirname
from collections import namedtuple
from importlib import import_module
from inspect import getfile
from sphinx import apidoc
from textwrap import dedent


UNSUPPORTED = object()

# locations we search for setup.py
TEMPLATE_URL = "https://raw.github.com/pyfarm/%(repo)s/master/setup.py"
TEMPLATE_PATH = join("..", "..", "%(repo)s", "setup.py")

# objects used to construct a fake sys.version_info
VERSION = namedtuple(
    "version_info", ["major", "minor", "micro", "releaselevel", "serial"])
PYTHON_VERSIONS = (
    VERSION(major=2, minor=6, micro=9, releaselevel="final", serial=0),
    VERSION(major=2, minor=7, micro=9, releaselevel="final", serial=0),
    VERSION(major=3, minor=0, micro=0, releaselevel="final", serial=0),
    VERSION(major=3, minor=1, micro=0, releaselevel="final", serial=0),
    VERSION(major=3, minor=2, micro=0, releaselevel="final", serial=0),
    VERSION(major=3, minor=3, micro=0, releaselevel="final", serial=0))

# the repos we should construct the requirements for
REPOS = (
    "pyfarm",
    "pyfarm-docs",
    "pyfarm-core",
    "pyfarm-agent",
    "pyfarm-master")


def get_setup_paths():
    for repo_name in REPOS:
        template_data = {"repo": repo_name}
        local_path = TEMPLATE_PATH % template_data
        remote_url = TEMPLATE_URL % template_data

        # first try reading locally
        if isfile(local_path):
            print "parsing setup.py from %s" % realpath(local_path)
            fd, setup_path = tempfile.mkstemp(suffix=".py")
            shutil.copy(local_path, setup_path)

        # otherwise download the setup.py directly from the repo
        else:
            print "reading setup.py from %s" % remote_url
            try:
                setup = urllib2.urlopen(remote_url).read().strip()
                fd, setup_path = tempfile.mkstemp(suffix=".py")
                with open(setup_path, "w") as setup_stream:
                    setup_stream.write(setup)

            except Exception, e:
                print >> sys.stderr, \
                    "ERROR: could not open %s (%s)" % (remote_url, e)
                continue

        yield repo_name, setup_path


def get_setup_call_lineno(setup_path):
    if isfile(setup_path):
        setup = open(setup_path, "r").read()
    else:
        setup = setup_path

    module = ast.parse(setup)
    for node in ast.walk(module):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and \
                        node.func.id == "setup":

            return setup, node.lineno


def generate_autogen_replacements():
    output = StringIO()
    print >> output, ".. !!! THIS FILE IS GENERATED DO NOT EDIT DIRECTLY !!!"

    for repo, setup_path in get_setup_paths():
        setup, setup_lineno = get_setup_call_lineno(setup_path)
        clipped_source = "\n".join(setup.split("\n")[:setup_lineno-1])
        new_setup_lineno = get_setup_call_lineno(clipped_source)
        assert new_setup_lineno is None, "expected to not find setup()"

        # write the clipped file back
        with open(setup_path, "w") as setup_stream:
            setup_stream.write(clipped_source)

        # load up locals and globals from the file
        version_info = sys.version_info
        supported_versions = []

        for sys_version in PYTHON_VERSIONS:
            # trick setup.py into thinking it's a different version
            # of Python
            sys.version_info = sys_version

            # don't pollute our local environment
            _locals = {}
            _globals = {}

            try:
                execfile(setup_path, _globals, _locals)
            except AssertionError:  # unsupported version
                continue
            else:
                supported_versions.append(
                    ".".join(map(str, sys.version_info[0:2])))

        print >> output, ".. |versions_%s| replace:: %s" % (
            repo.replace("pyfarm-", ""), ", ".join(supported_versions))

        # return sys.version_info back to its original state
        sys.version_info = version_info

    print >> output, ".. !!! THIS FILE IS GENERATED DO NOT EDIT DIRECTLY !!!"
    return output.getvalue()


def write_autogen_replacements(path):
    data = generate_autogen_replacements()
    print "writing autogen replacements: %s" % path
    with open(path, "w") as stream:
        stream.write(data)


def write_autogen_agent_daemon_script(path):
    data = generate_autogen_agent_daemon_script()
    print "writing autogen twistd agent command line flags: %s" % path
    with open(path, "w") as stream:
        stream.write(data)


def write_module_docs(root):
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
        noheadings=False,
        destdir=root,
        suffix="rst",
        dryrun=False,
        force=True)

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

    with open(root+"/pyfarm.rst", "w") as index:
        index.write(index_source)