.. _sec-plugins:

Plugins
=========

One of the most important features of **itom** is its plugin system. Using plugins, **itom** is able to communicate with many hardware components, such as framegrabbers, cameras, motor stages or other devices. Furthermore it is possible to develop user defined algorithms in C/C++ and put them into an algorithm plugin. The call to these algorithms is then possible via the Python scripting language or other plugins.

The **itom** setup already comes with a small part of exemplary plugins. Other plugins are available as source files in the corresponding plugin repository (`Plugins <https://bitbucket.org/itom/plugins>`_). Furthermore, the SDK of **itom** provide some template files for creating your own plugin using CMake and the development environment of your choice (see `CMake Plugin <http://itom.bitbucket.org/latest/docs/07_plugins/development/pluginCreateCMake.html>`_).


Add a plugin to itom
---------------------

For loading a plugin library at startup of **itom**, the following things must be met:

1. The plugin library is contained in any subfolder of the folder **plugin** contained in the application (root) directory of **itom**
2. If **itom** is build in debug, the plugin must be compiled in debug as well. The same holds for the default release versions.
3. If the plugin depends on further 3rd party libraries, these libraries must be accessible by your operating system (on Windows: Their path must be contained in the PATH environment variable OR the necessary DLLs must be in the **lib** subfolder of **itom** or in the root directory of **itom**). Only if the plugin is able to load further libraries by means of a delay load mechanism, it is possible to also put 3rd party libraries in arbitrary folders.
4. If your plugin depends on 3rd party libraries, please make sure that all plugins use exactly the same version of the same library.

Available plugins
------------------

The following plugins are contained in the open source plugin repository `Plugins <https://bitbucket.org/itom/plugins>`_ (and some of them are also already included in the setup of **itom**):


.. toctree::
   :maxdepth: 1
   
   plugins/grabbers.rst
   
.. toctree::
   :maxdepth: 2
   
   plugins/actuators.rst
   
.. toctree::
   :maxdepth: 2
   
   plugins/GDIO.rst
   
.. toctree::
   :maxdepth: 2
   
   plugins/adconv.rst
   
.. toctree::
   :maxdepth: 2
   
   plugins/algorithms.rst



Plugin Development
-------------------

If you have any hardware component that is not yet supported by **itom** or if you need to have a specific algorithm implemented as algorithm plugin, you have the following possibilities:

* Start to develop your own plugin library and make this plugin available to anybody if you want to. More information about this can be found under `Plugin Development <http://itom.bitbucket.org/latest/docs/07_plugins/development/plugin-development.html>`_
* Since not all plugins are already available in the internet, ask us if for instance we already have the plugin you need.
* Feel also free to contact us if you want us to develop a plugin for you.
* Register to the `mailing list <https://lists.sourceforge.net/lists/listinfo/itom-discussions>`_ and write further questions.

