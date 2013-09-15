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

Installation
============

.. warning::
    this document is a draft

These instructions cover the general installation of PyFarm's components.
Please note they may vary between platforms though these differences are usually
noted.  These instructions have been tested on the following platforms:
    * Debian 7.1 64-bit
    * Windows 7 Professional 32-bit
    * Windows XP w/SP3 32-bit

Python Setup
------------
Before installing PyFarm you must install Python.  Below are the various steps
required to install the base Python interpreter and associated libraries.  When
linked to a web page instead of a download please locate the installer package
for your architecture and download it.

Windows
+++++++
Windows requires a little extra work in order to setup Python.  Unlike platforms
such as Linux which make installing a compatible C-compiler a simple task
Windows adds a few extra steps.


Required Downloads
~~~~~~~~~~~~~~~~~~
#. `7-zip <http://www.7-zip.org/download.html>`_ - to extract the ISO
#. `Visual Studio 2008 Express w/SP1 <http://download.microsoft.com/download/E/8/E/E8EEB394-7F42-4963-A2D8-29559B738298/VS2008ExpressWithSP1ENUX1504728.iso>`_
   - used to compile C extensions on the fly
#. `Python 2.7 MSI Installer <http://python.org/download/releases/2.7.5/>`_ -
   interpreter to run PyFarm
#. `setuptools <https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.5.tar.gz>`_ - contains easy_install (used later on)

Installation
~~~~~~~~~~~~
#. 7-zip - execute the installation package and follow the steps on the screen
#. Visual Studio 2008 Express
    #. Right click on the ISO file and select 7-zip ->
       Extract to "VS2008ExpressWithSP1ENUX1504728\".  After this is complete
       you are free to delete the ISO image if you wish.
    #. Run (double click) VS2008ExpressWithSP1ENUX1504728\Setup.hta
    #. When the setup begins you will be prompted with a few different additions
       to choose from.  Select "Microsoft Visual C++ 2008 Express Edition"
    #. Accept the EULA and continue forward.
    #. There should be two boxes checked for additional components to install:
        * Microsoft Silverlight Runtime
        * Microsoft SQL Server 2008 Express Edition

       These components are not required and you are welcome to uncheck them to
       save time and space.
    #. Click next and continue with the installation.  If the installation fails
       check to make sure you don't have any pending updates for windows or a
       reboot scheduled because of a new driver.
#. Python
    #. Start the installation
    #. Install for all users in the default location
    #. Open a run dialog or hold down the windows key and 'r'.  When the dialog
       opens type 'run' (no quotes) and hit enter.
    #. When the terminal opens type 'python' and hit enter (again, no quotes).
       If you get something like this:
       ::

            'python' is not recognized as an internal or external command,
            operable program or batch file.

       Then we'll need to add some things to %PATH% to continue:
            .. warning::
               be careful editing these settings, deleting existing paths could
               cause damage to your installation

            #. Right click on Computer and select Properties
            #. For Windows along the left side select you'll select
               "Advanced System Settings".  If you're running Windows XP, skip
               this step.
            #. In the dialog that opens select Advanced (if it's not already)
               then click the "Environment Variables" button in the bottom right
            #. In the lower half of the window there's a "System Variables"
               section, select "Path" and then click "Edit"
            #. in the "Variable value" field add this to the end:
               ::

                   ;C:\Python27;C:\Python27\Scripts
    #. Right click on the setuptools gzipped tar (.tar.gz) and select 7-zip ->
       extract here
    #. Navigate down into the 'dist' directory it produces and do the same thing
       on the file inside that directory
    #. Once that's complete open up a command window using run and run the
       setup.py file.  It should look something like this:
       ::

            C:\Users\dev>python C:\Users\dev\Downloads\dist\setuptools-1.1.5\setup.py install

    #. Now easy_install pip:
       ::

            C:\Users\dev>easy_install pip
            Searching for pip
            Reading https://pypi.python.org/simple/pip/
            Best match: pip 1.4.1
            Downloading https://pypi.python.org/packages/source/p/pip/pip-1.4.1.tar.gz#md5=6afbb46aeb48abac658d4df742bff714
            Processing pip-1.4.1.tar.gz
            Writing c:\users\dev\appdata\local\temp\easy_install-g3mjsb\pip-1.4.1\setup.cfg
            Running pip-1.4.1\setup.py -q bdist_egg --dist-dir c:\users\dev\appdata\local\temp\easy_install-g3mjsb\pip-1.4.1\egg-dist-tmp-cthuvm
            warning: no files found matching '*.html' under directory 'docs'
            warning: no previously-included files matching '*.rst' found under directory 'docs\_build'
            no previously-included directories found matching 'docs\_build\_sources'
            Adding pip 1.4.1 to easy-install.pth file
            Installing pip-script.py script to C:\Python27\Scripts
            Installing pip.exe script to C:\Python27\Scripts
            Installing pip.exe.manifest script to C:\Python27\Scripts
            Installing pip-2.7-script.py script to C:\Python27\Scripts
            Installing pip-2.7.exe script to C:\Python27\Scripts
            Installing pip-2.7.exe.manifest script to C:\Python27\Scripts

            Installed c:\python27\lib\site-packages\pip-1.4.1-py2.7.egg
            Processing dependencies for pip
            Finished processing dependencies for pip

    #. Then pip install virtualenv:
       ::

            C:\Users\dev>pip install virtualenv
            Downloading/unpacking virtualenv
            Downloading virtualenv-1.10.1.tar.gz (1.3MB): 1.3MB downloaded
            Running setup.py egg_info for package virtualenv

                warning: no files found matching '*.egg' under directory 'virtualenv_support'
                warning: no previously-included files matching '*' found under directory 'docs\_templates'
                warning: no previously-included files matching '*' found under directory 'docs\_build'
            Installing collected packages: virtualenv
            Running setup.py install for virtualenv

                warning: no files found matching '*.egg' under directory 'virtualenv_support'
                warning: no previously-included files matching '*' found under directory 'docs\_templates'
                warning: no previously-included files matching '*' found under directory 'docs\_build'
                Installing virtualenv-script.py script to C:\Python27\Scripts
                Installing virtualenv.exe script to C:\Python27\Scripts
                Installing virtualenv.exe.manifest script to C:\Python27\Scripts
                Installing virtualenv-2.7-script.py script to C:\Python27\Scripts
                Installing virtualenv-2.7.exe script to C:\Python27\Scripts
                Installing virtualenv-2.7.exe.manifest script to C:\Python27\Scripts
            Successfully installed virtualenv
            Cleaning up...

    #. And now a quick test of the whole system.  Your results will vary but it
       should look something like this and say "Successfully installed psutil"
       towards the end:
       ::

            C:\Users\dev>virtualenv test
            New python executable in test\Scripts\python.exe
            Installing Setuptools........................................................................................................................................................................................................................
            ...............done.
            Installing Pip...............................................................................................................................................................................................................................
            .............................................................................................done.

            C:\Users\dev>test\Scripts\activate
            (test) C:\Users\dev>
            (test) C:\Users\dev>pip install psutil
            Downloading/unpacking psutil
            You are installing an externally hosted file. Future versions of pip will default to disallowing externally hosted files.
            You are installing a potentially insecure and unverifiable file. Future versions of pip will default to disallowing insecure files.
            Downloading psutil-1.0.1.tar.gz (159kB): 159kB downloaded
            Running setup.py egg_info for package psutil

            Installing collected packages: psutil
            Running setup.py install for psutil
                building '_psutil_mswindows' extension
                C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\cl.exe /c /nologo /Ox /MD /W3 /GS- /DNDEBUG -D_WIN32_WINNT=0x0601 -D_AVAIL_WINVER_=0x0601 -IC:\Python27\include -IC:\Users\dev\test\PC /Tcpsutil/_psutil_mswindows.c /Fobuild\temp.wi
            se\psutil/_psutil_mswindows.obj
                _psutil_mswindows.c
                psutil/_psutil_mswindows.c(307) : warning C4013: 'get_process_info' undefined; assuming extern returning int
                psutil/_psutil_mswindows.c(568) : warning C4047: 'function' : 'LPSTR' differs in levels of indirection from 'wchar_t (*)[260]'
                psutil/_psutil_mswindows.c(568) : warning C4024: 'GetProcessImageFileNameA' : different types for formal and actual parameter 2
                psutil/_psutil_mswindows.c(602) : warning C4133: 'function' : incompatible types - from 'PROCESS_MEMORY_COUNTERS_EX *' to 'PPROCESS_MEMORY_COUNTERS'
                psutil/_psutil_mswindows.c(2091) : warning C4047: 'function' : 'PDWORD_PTR' differs in levels of indirection from 'PDWORD_PTR *'
                psutil/_psutil_mswindows.c(2091) : warning C4024: 'GetProcessAffinityMask' : different types for formal and actual parameter 2
                psutil/_psutil_mswindows.c(2091) : warning C4047: 'function' : 'PDWORD_PTR' differs in levels of indirection from 'PDWORD_PTR *'
                psutil/_psutil_mswindows.c(2091) : warning C4024: 'GetProcessAffinityMask' : different types for formal and actual parameter 3
                psutil/_psutil_mswindows.c(2413) : warning C4005: '_ARRAYSIZE' : macro redefinition
                        C:\Program Files\Microsoft SDKs\Windows\v6.0A\include\winnt.h(1021) : see previous definition of '_ARRAYSIZE'
                psutil/_psutil_mswindows.c(2482) : warning C4047: 'function' : 'LPSTR' differs in levels of indirection from 'LPTSTR [261]'
                psutil/_psutil_mswindows.c(2482) : warning C4024: 'GetVolumeInformationA' : different types for formal and actual parameter 7
                C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\cl.exe /c /nologo /Ox /MD /W3 /GS- /DNDEBUG -D_WIN32_WINNT=0x0601 -D_AVAIL_WINVER_=0x0601 -IC:\Python27\include -IC:\Users\dev\test\PC /Tcpsutil/_psutil_common.c /Fobuild\temp.win32
            psutil/_psutil_common.obj
                _psutil_common.c
                C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\cl.exe /c /nologo /Ox /MD /W3 /GS- /DNDEBUG -D_WIN32_WINNT=0x0601 -D_AVAIL_WINVER_=0x0601 -IC:\Python27\include -IC:\Users\dev\test\PC /Tcpsutil/arch/mswindows/process_info.c /Fobui
            -2.7\Release\psutil/arch/mswindows/process_info.obj
                process_info.c
                psutil/arch/mswindows/process_info.c(36) : warning C4013: 'AccessDenied' undefined; assuming extern returning int
                psutil/arch/mswindows/process_info.c(36) : warning C4047: 'return' : 'HANDLE' differs in levels of indirection from 'int'
                psutil/arch/mswindows/process_info.c(42) : warning C4013: 'NoSuchProcess' undefined; assuming extern returning int
                C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\cl.exe /c /nologo /Ox /MD /W3 /GS- /DNDEBUG -D_WIN32_WINNT=0x0601 -D_AVAIL_WINVER_=0x0601 -IC:\Python27\include -IC:\Users\dev\test\PC /Tcpsutil/arch/mswindows/process_handles.c /Fo
            n32-2.7\Release\psutil/arch/mswindows/process_handles.obj
                process_handles.c
                psutil/arch/mswindows/process_handles.c(203) : warning C4022: 'NtDuplicateObject' : pointer mismatch for actual parameter 2
                C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\cl.exe /c /nologo /Ox /MD /W3 /GS- /DNDEBUG -D_WIN32_WINNT=0x0601 -D_AVAIL_WINVER_=0x0601 -IC:\Python27\include -IC:\Users\dev\test\PC /Tcpsutil/arch/mswindows/security.c /Fobuild\t
            \Release\psutil/arch/mswindows/security.obj
                security.c
                psutil/arch/mswindows/security.c(86) : warning C4996: 'strcpy': This function or variable may be unsafe. Consider using strcpy_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.
                C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\link.exe /DLL /nologo /INCREMENTAL:NO /LIBPATH:C:\Python27\Libs /LIBPATH:C:\Users\dev\test\libs /LIBPATH:C:\Users\dev\test\PCbuild psapi.lib kernel32.lib advapi32.lib shell32.lib ne
            hlpapi.lib wtsapi32.lib /EXPORT:init_psutil_mswindows build\temp.win32-2.7\Release\psutil/_psutil_mswindows.obj build\temp.win32-2.7\Release\psutil/_psutil_common.obj build\temp.win32-2.7\Release\psutil/arch/mswindows/process_info.obj bu
            2-2.7\Release\psutil/arch/mswindows/process_handles.obj build\temp.win32-2.7\Release\psutil/arch/mswindows/security.obj /OUT:build\lib.win32-2.7\_psutil_mswindows.pyd /IMPLIB:build\temp.win32-2.7\Release\psutil\_psutil_mswindows.lib /MAN
            ld\temp.win32-2.7\Release\psutil\_psutil_mswindows.pyd.manifest
                Creating library build\temp.win32-2.7\Release\psutil\_psutil_mswindows.lib and object build\temp.win32-2.7\Release\psutil\_psutil_mswindows.exp

            Successfully installed psutil
            Cleaning up...

            (test) C:\Users\dev>python -c "import psutil; print psutil"
            <module 'psutil' from 'C:\Users\dev\test\lib\site-packages\psutil\__init__.pyc'>


Linux
+++++
Linux generally won't require very much to be done to get started and in most
cases is already setup for you.  That said, it wouldn't hurt to run the steps
below to be sure.  The following commands will need to be executed either as
root or using the sudo command.

Debian Based Systems
~~~~~~~~~~~~~~~~~~~~
::

    aptitude -y install python python-setuptools python-virtualenv build-essential

Red Hat Based Systems
~~~~~~~~~~~~~~~~~~~~~
**TODO** instructions needed here