.. _sec-downloads:

Downloads
=========

Besides compiling **itom** from the sources, there are binaries for the Windows version of **itom** (32/64bit).
These binaries contain the core application of **itom** together with a small selection of plugins and most designer plugins
that provide the plot and figure widgets of **itom**.

The installers are available in a default version and an All-In-One version. The default version simply contains **itom** and
the necessary runtime libraries while the all-in-one solution also contains 3rd party dependencies that can be installed as optional
component. These components are:

* Python 3.3
* Numpy 1.8.1
* Scipy 0.14.0
* Matplotlib 1.3.1
* Pillow 2.0
* PyParsing 2.0
* six 1.6.1
* dateutil 2.2

The current version 1.4.0 is available from

* `<https://bitbucket.org/itom/itom/downloads>`_ or
* `<http://sourceforge.net/projects/itom/files/v1.4.0/>`_

.. note::
    
    There is a known issue in the setup 1.4.0 concerning an unsuccessful startup of the external Qt designer. If you want to open
    the designer using the button in the toolbox of the itom main window, the startup may fail. This bug is known and will be fixed
    in future releases. Until then, please open the designer either by starting the designer.exe in the application folder of itom
    or open an existing ui-file (e.g. in the demo folder of itom).

Older versions are only hosted at sourceforge.net:

* `itom 1.3.0 <http://sourceforge.net/projects/itom/files/v1.3.0>`_
* `itom 1.2.0 <http://sourceforge.net/projects/itom/files/v1.2.0>`_
* `itom 1.1.0 <http://sourceforge.net/projects/itom/files/v1.1.0>`_
* `itom 1.0.14 <http://sourceforge.net/projects/itom/files/v1.0.14>`_
* `itom 1.0.13 <http://sourceforge.net/projects/itom/files/v1.0.13>`_
* `itom 1.0.12 <http://sourceforge.net/projects/itom/files/v1.0.12>`_