import atexit
import sys
import os
import tempfile
import time
import shutil
import subprocess
from os.path import join, isdir

import virtualenv

try:
    REPO_ROOT = sys.argv[1]
except IndexError:
    print "usage: %s <checkout root>" % sys.argv[0]
    sys.exit(1)

PIP_CACHE = join(tempfile.gettempdir(), "pip_download_cache")
if not isdir(PIP_CACHE):
    os.makedirs(PIP_CACHE)

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


def cleanup():
    print "Removing %s" % VIRTUALENV
    try:
        shutil.rmtree(VIRTUALENV)
    except OSError:
        pass

# atexit.register(cleanup)

_, logfile = tempfile.mkstemp(suffix=".log")
print "Logging to %s" % logfile

start = time.time()
for package in (PYFARM_CORE, PYFARM_MASTER, PYFARM_AGENT, PYFARM_DOCS):
    print "Installing %s" % package
    return_code = subprocess.call(
        [PIP, "install", "-e", package, "--egg", "--download-cache", PIP_CACHE,
         "--upgrade"])

    if return_code != 0:
        print open(logfile).read()
        print "ERROR %s" % return_code
        sys.exit(1)

print "Installed PyFarm in %s seconds" % (time.time() - start, )

activate = join(BIN, "activate")
subprocess.call(["make", "clean"], cwd=PYFARM_DOCS)
with open(tempfile.mkstemp()[-1], "w") as script:
    print >> script, "#!/bin/bash"
    print >> script, "source %s" % join(BIN, "activate")
    print >> script, "make clean"
    print >> script, "make html"

return_code = subprocess.call(["sh", script.name], cwd=PYFARM_DOCS)
print return_code