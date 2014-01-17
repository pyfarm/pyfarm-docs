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

import sys
assert sys.version_info[0:2] >= (2, 6), "Python 2.6 or higher is required"

# Because we have to install libraries directly from repos, we must
# use the setup.py directly for now.  PIP runs this file as a script which
# means it does not always pickup our custom install clas

from setuptools import setup
from setuptools.command import easy_install
from setuptools.command.install import install
from distutils.command.install import install as _install


class Install(install):
    def run(self):
        # easy_install from urls
        install_urls = [
            "https://github.com/pyfarm/pyfarm-core/archive/master.zip",
            "https://github.com/pyfarm/pyfarm-agent/archive/master.zip",
            "https://github.com/pyfarm/pyfarm-master/archive/master.zip",
            "https://github.com/pyfarm/pyfarm-models/archive/master.zip",
            "https://github.com/pyfarm/pyfarm-jobtypes/archive/master.zip"]
        easy_install.main(install_urls)

        # regular install command
        if self.old_and_unmanageable or self.single_version_externally_managed:
            _install.run(self)
        else:
            self.do_egg_install()

setup(
    name="pyfarm-docs",
    version="0.7.0",
    cmdclass={"install": Install},
    install_requires=[
        "sphinx", 
        "sphinxcontrib-httpdomain", 
        "sphinxcontrib-programoutput"])
