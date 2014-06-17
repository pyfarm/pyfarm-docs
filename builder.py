import sys
import os
import shutil
import subprocess
import tempfile
import time
from os.path import join, isdir, isfile

import virtualenv

try:
    REPO_ROOT, DEST_DIR = sys.argv[1], sys.argv[2]
except IndexError:
    print "usage: %s <checkout root> <output dir>" % sys.argv[0]
    sys.exit(1)

PIP_CACHE = join(tempfile.gettempdir(), "pip_download_cache")
if not isdir(PIP_CACHE):
    os.makedirs(PIP_CACHE)

if not isdir(DEST_DIR):
    os.makedirs(DEST_DIR)

PYFARM_CORE = join(REPO_ROOT, "pyfarm-core")
PYFARM_MASTER = join(REPO_ROOT, "pyfarm-master")
PYFARM_AGENT = join(REPO_ROOT, "pyfarm-agent")
PYFARM_DOCS = join(REPO_ROOT, "pyfarm-docs")

assert isdir(PYFARM_CORE) and isdir(PYFARM_MASTER) and isdir(PYFARM_AGENT)

VIRTUALENV = join(tempfile.gettempdir(), "docs_virtualenv")
HOME, LIB, INCLUDE, BIN = virtualenv.path_locations(VIRTUALENV)
PIP = join(BIN, "pip")
virtualenv.create_environment(VIRTUALENV)
print "Created virtualenv at %s" % VIRTUALENV

_, logfile = tempfile.mkstemp(suffix=".log")
print "Logging to %s" % logfile

start = time.time()
assert subprocess.call(
    [PIP, "install", "nose", "--download-cache", PIP_CACHE,
     "--upgrade"]) == 0
assert subprocess.call(
    [PIP, "install", "coverage", "--download-cache", PIP_CACHE,
     "--upgrade"]) == 0

for package in (PYFARM_CORE, PYFARM_MASTER, PYFARM_AGENT, PYFARM_DOCS):
    print "Installing %s" % package
    assert subprocess.call(
        [PIP, "install", "-e", package, "--egg", "--download-cache", PIP_CACHE,
         "--upgrade"]) == 0

print "Installed PyFarm in %s seconds" % (time.time() - start, )

builddir = tempfile.mkdtemp()
print "Building documentation to %s"
with open(tempfile.mkstemp()[-1], "w") as script:
    print >> script, "#!/bin/bash"
    print >> script, "source %s" % join(BIN, "activate")
    print >> script, "make clean"
    print >> script, "make html BUILDDIR=%s" % builddir
assert subprocess.call(["bash", script.name], cwd=PYFARM_DOCS) == 0

print "Built %s" % builddir
out_html = join(DEST_DIR, "html")
build_html = join(builddir, "html")
if isdir(out_html):
    shutil.rmtree(out_html)
shutil.move(build_html, DEST_DIR)
print "Moved %s %s" % (build_html, DEST_DIR)
