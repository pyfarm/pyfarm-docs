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

import pkg_resources

import sys
import tempfile
from datetime import datetime
from os.path import abspath, join, dirname

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = "1.0"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named "sphinx.ext.*") or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.httpdomain"]

pymajor, pyminor = sys.version_info[0:2]
intersphinx_mapping = {
    "python": ("http://docs.python.org/%s.%s" % (pymajor, pyminor), None),
    "sqlalchemy": ("http://www.sqlalchemy.org/docs/", None),
    "flask": ("http://flask.readthedocs.org/en/latest/", None),
    "numpy": ("http://docs.scipy.org/doc/numpy", None)}

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"PyFarm"
author = "Oliver Palmer"
parsed_version = (1, 0, 0)
root = abspath(join(dirname(__file__), ".."))
docroot = join(root, "source")
tmpdir = tempfile.mkdtemp(suffix="-pyfarm-docs")

print "generating dynamic content"

# Parse the __init__.py file instead of importing it.  So even if we
# have code that can't be imported we can at least read the proper version
# information
print "..parsing version/author(s)"

# General information about the project.

now = datetime.now()
copyright = "%s, %s" % (now.year, author)
release = ".".join(map(str, parsed_version))
version = ".".join(map(str, parsed_version[0:2]))


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["include/*", "downloads/*"]
pygments_style = "sphinx"
html_theme = "default"
html_static_path = ["_static"]
htmlhelp_basename = "PyFarmdoc"
latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ("index", "PyFarm.tex", u"PyFarm Documentation",
   u"Oliver Palmer", "manual"),
]


man_pages = [
    ("index", "pyfarm", u"PyFarm Documentation",
     [u"Oliver Palmer"], 1)
]

texinfo_documents = [
  ("index", "PyFarm", u"PyFarm Documentation",
   u"Oliver Palmer", "PyFarm", "A Python based distributed job system",
   "Miscellaneous"),
]