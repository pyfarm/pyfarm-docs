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

from __future__ import with_statement

import os
import sys
from distutils.core import setup

# we're generating documentation, we really shouldn't support anything lower
assert sys.version_info[0:3] >= (2, 6), "Python 2.6 or higher is required"

setup(
    name="pyfarm-docs",
    version="pyfarm-docs",
    install_requires=["pyfarm", "sphinx"]
)