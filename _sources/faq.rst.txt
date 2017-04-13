.. _sec-known-issues:

Known bugs, issues and workarounds
====================================

In the following a list of known bugs and issues in specific setup versions of itom are listed. Some of these bugs
can be overcome by the listed workarounds or solutions:

General
--------------

.. glossary::

    Error message from Python packages
        If some Python packages (**matplotlib, scipy, numpy**) return an error message that a dll-file can not be load, 
        the Visual C++ Redistributable is not correctly installed. Try to reinstall it. 
        The current version can be downloaded here: https://www.microsoft.com/de-de/download/details.aspx?id=48145

itom 3.0.0
--------------

.. glossary::
    
    Error message at startup: python35.dll could not be found (fixed in version 3.0.0)
        From Python 3.5 on, the Windows installer does not copy the corresponding DLL libraries to the Windows system directory. Please make
        sure that the Python directory, containing the requested DLL library is added to the PATH environment variable of Windows. 
        Usually this is automatically done within the Python installer, however it is possible to unselect this option. Re-logon to your Windows session
        in order to let Windows reload this environment variable. See http://www.computerhope.com/issues/ch000549.htm for
        information how to add a value to the PATH environment variable in Windows.
    
    Scaling problems on high-resolution displays (4k) (fixed in version 3.0.0)
        itom for all versions up to 2.2.1 will not be properly scaled on high-resolution displays. We are currently working on this issue to 
        improve the problem. In order to overcome this problem (Windows only), it is possible to tell Windows that an application is only
        prepared for 96dpi (default) screens such that Windows will internally handle the scaling for 4k displays.
        Place the following manifest file (`qitom.exe.manifest <documents/qitom.exe.manifest>`_) into the same folder of itom to start the application in the
        compatibility mode. For more information see http://www.danantonielli.com/adobe-app-scaling-on-high-dpi-displays-fix/

itom 2.1.0
--------------

.. glossary::

    itom crashes at startup when *python* should be loaded. 
        Problem: There are two known reasons for this crash. The first is, that you probably installed python with another 
        user than the one you are currently logged in. When the python library (see above) is loaded at startup of itom, 
        it interally tries to find out, where the entire python installation including the modules and packages are located 
        on your harddrive. Usually, this information is contained in the Windows registry. However, if Python has been installed 
        under a local or different user, the registry information cannot be properly read. In this case, either reinstall Python 
        as adminstrator and for all users or set the environment variable PYTHONHOME (see http://www.computerhope.com/issues/ch000549.htm)
        to the base directory of Python (the directory where the Python executable is located). 
        
        Another problem  might be, that your computer has a default charset that differs from the european or american one 
        (e.g. russian operating system). In this case, a known bug is contained in the qitom.exe application of the 32bit 
        and 64bit Windows setup. There is a corrected application file for the 64bit setup. Download the archive 
        **qitom_2.1.0_64bit_encoding_fix.zip** from https://sourceforge.net/projects/itom/files/v2.1.0/ and replace the file 
        **qitom.exe** by the one in the zip-file.
        
        Both issues will be fixed in upcoming itom versions.
        
itom 1.4.0
--------------

.. glossary::
    
    Qt Designer does not start
        There is a known issue in the former setup 1.4.0 concerning an unsuccessful startup of the external Qt designer. If you want 
        to open the designer using the button in the toolbox of the itom main window, the startup may fail. This bug is known and will 
        be fixed in future releases. Until then, please open the designer either by starting the designer.exe in the application folder 
        of itom or open an existing ui-file (e.g. in the demo folder of itom).