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

from setuptools import setup

setup(
    name="pyfarm-docs",
    version="0.7.0",
    install_requires=[
        "sphinx",
        "flask", "flask-sqlalchemy", "flask-login", "flask-admin",
        "pyfarm.core",
        "pyfarm.models",
        "pyfarm.jobtypes",
        "netifaces",
        "netaddr",
        "psutil"])