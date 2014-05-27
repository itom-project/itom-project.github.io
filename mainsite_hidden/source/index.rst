.. itom documentation master file, created by
   sphinx-quickstart on Thu Aug 22 22:45:55 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

itom - an Open Source Measurement, Automation and Evaluation Software
============================================================================

**itom** is an open source software suite for operating measurement systems, laboratory automation and data evaluation.

.. image:: _static\\itom.png
    :alt: itom software
    :width: 740px
    :align: center

**Contents:**

.. toctree::
   :maxdepth: 2
   
   download.rst
   documentation.rst
   media.rst
   features.rst
   plugins.rst
   screenshots.rst

News
-----

* 2014-05-27: Today **itom 1.2.0** has been released. The Windows setups and the sources (tag v1.2.0) are ready for download. It consists now of all plugins that are released under an open source license. For more information see the changelog at http://itom.bitbucket.org/latest/docs/00_releaseNotes/whats-new.html
* 2014-04-09: An improved and more detailed version of the plugin documentation is now online, see :ref:`plugins <sec-plugins>`.
* 2014-04-05: The sources for the plugins **V4L2** (Video for Linux), **MSMediaFoundation** (Windows Vista or higher), **PCOCamera** (cameras supported by the pco.sdk) and **PCLTools** (point cloud processing, filtering... using the PointCloudLibrary) are online.
* 2014-03-12: The plugin for support of x3p-file format is online (see :ref:`plugins <sec-plugins>`).
* 2014-02-25: From today on, **itom** can be build using Qt5. Get the current sources and have Qt5 ready on your computer (no Qt4). The right version of Qt is automatically selected.
* 2014-02-24: The cameras :ref:`plugins <sec-plugins>` **Ximea** and **PGRFlyCapture** are online (https://bitbucket.org/itom/plugins).
* 2014-01-27: Today, **itom 1.1.0** has been released. The Windows setups and the sources (tag v1.1.0) are ready for download. It contains many bugfixes, better plot functionalities including geometric measurement tools in plots, more open-source plugins (all included in the setups now) and an online script reference as toolbox of itom that also informs about the documentation and parameterization of all loaded algorithm plugins.
* 2014-01-13: The plugins **AerotechEnsemble** (Ensemble controller of Aerotech axes) and **BasicFilters** are online (https://bitbucket.org/itom/plugins).
* 2013-12-22: Newest documentation :ref:`documentation <sec-documentation>` online (small changes with respect to v1.0.14).
* 2013-10-10: The plugins **OpenCVFilters** (wrapper for some OpenCV functions) and **DispWindow** (OpenGL based cosine and graycode fringe pattern display) are put online (https://bitbucket.org/itom/plugins).
* 2013-10-10: The new section about :ref:`plugins <sec-plugins>` has been added to this website.
* 2013-09-12: The introduction to **itom** and a poster, presented at the `Fringe 2013 conference <http://www.fringe13.de>`_, is available in the :ref:`media section <sec-media>`.
* 2013-09-02: Today **itom 1.0.14** has been released. The Windows setups and the sources (tag v1.0.14) are ready for download. It contains many bugfixes, an extended set of open-source plugins as well as renamed and improved designer plugins.

Project Repositories
---------------------

The sources of **itom** are separated into several repositories, hosted at bitbucket.org:

* Main access at `<https://bitbucket.org/itom>`_
* `itom core repository <https://bitbucket.org/itom/itom>`_
* `itom plugins <https://bitbucket.org/itom/plugins>`_
* `itom designer plugins (plots...) <https://bitbucket.org/itom/designerplugins>`_
* `MacroSim raytracer <https://bitbucket.org/itom/macrosim>`_

These repository also contain more information in their corresponding wiki.

Information, Bug reports, Mailing Lists
----------------------------------------

Please register to the `mailing list <https://lists.sourceforge.net/lists/listinfo/itom-discussions>`_ in order to obtain news about *itom*. You can also use this mailing list if you have questions or comments.

For specific bug reports or feature requests, please use the issue tracking system of bitbucket, depending on the specific repositories (itom, plugins, designer plugins...):

* `itom <https://bitbucket.org/itom/itom/issues>`_
* `plugins <https://bitbucket.org/itom/plugins/issues>`_
* `designer plugins <https://bitbucket.org/itom/designerplugins/issues>`_

Licensing and Copyright
------------------------

The core components and the main application of **itom** are covered by the **GNU Library General Public Licence** (GNU LGPL). All components belonging to the SDK of **itom** (e.g. dataObject, pointCloud, addInInterface,...) are additionally covered by an **itom** exception. The main idea of this exception is to allow other libraries (e.g. plugins) to include and link agains components of **itom** SDK independent on the specific license model of the respective “other” library. For more information see http://itom.bitbucket.org/latest/docs/01_introduction/introduction.html#licensing.

**itom** is a project provided by

+--------------------+--------------------------------------+
| |itologo|          | | Institut für Technische Optik      |
|                    | | Universität Stuttgart              |
|                    | | Pfaffenwaldring 9                  |
|                    | | 70569 Stuttgart                    |
|                    | | http://www.uni-stuttgart.de/ito    |
+--------------------+--------------------------------------+

.. |itologo| image:: _static\\ITO_Logo_standard.png
                         :width: 150px

.. |ito| replace:: Institut für Technische Optik
                   Universität Stuttgart
                   Pfaffenwaldring 9
                   70569 Stuttgart
                   Germany
                   http://www.uni-stuttgart.de/ito


