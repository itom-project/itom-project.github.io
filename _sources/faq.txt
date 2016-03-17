.. _sec-known-issues:

Known bugs, issues and workarounds
====================================

In the following a list of known bugs and issues in specific setup versions of itom are listed. Some of these bugs
can be overcome by the listed workarounds or solutions:

**itom 2.1.0**

* The error message **python35.dll could not be found** shows up at startup. Solution: From Python 3.5 on, 
    the Windows installer does not copy the corresponding dll file to the Windows system directory. Please make
    sure that the Python directory is added to the PATH environment variable of Windows. Usually this is automatically
    done within the Python installer, however it is possible to unselect this option. Re-logon to your Windows session
    in order to let Windows reload this environment variable.

* itom crashes at startup when *python* should be loaded. Problem: There are two known reasons for this crash. The first is,
    that you probably installed python with another user than the one you are currently logged in. When the python library (see above)
    is loaded at startup of itom, it interally tries to find out, where the entire python installation including the modules and
    packages are located on your harddrive. Usually, this information is contained in the Windows registry. However, if Python has
    been installed under a local or different user, the registry information cannot be properly read. In this case, either reinstall
    Python as adminstrator and for all users or set the environment variable PYTHONHOME to the base directory of Python. Another problem
    might be, that your computer has a default charset that differs from the european or american one (e.g. russian operating system).
    In this case, a known bug is contained in the qitom.exe application of the 32bit and 64bit Windows setup.
    There is a corrected application file for the 64bit setup. Download the archive **qitom_2.1.0_64bit_encoding_fix.zip** from https://sourceforge.net/projects/itom/files/v2.1.0/
    and replace the file **qitom.exe** by the one in the zip-file.