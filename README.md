How to update the itom website
==============================

Pre-requirements
----------------

itom, plugins and designerplugin must be compiled and loaded by itom. 
Install the Python Package **requirementsDocuBuild.txt** from [itom](https://github.com/itom-project/itom) form the subfolder ``itom/docs/userDoc/``.

* Delete all files in ``../mainsite_hidden/build/``
* If there are new plugin copy the ``*.rst`` file from [plugin](https://github.com/itom-project/plugin) source repository to ``../mainsite_hidden/source_plugins/``
* Start ITOM (As Admin)

Update Plugin-Doc
-----------------

* Run script: ``../mainsite_hidden/update_plugindoc_source_plugins.py``. Skript will ask you for a folder. Select the ``itom/source`` folder. Script will update exsiting plugin's ``*.rst`` files.
* Run Script: ``../mainsite_hidden/create_plugin_documentation.py``. This creates the plugin docu for the website. 

Update Website
--------------	
* Run Script: ``../mainsite_hidden/create_html_documentation.py``. This creates the itom website and is copied to main website dir. 

Update USER-DOC
---------------
* Update ``..mainsite_hidde/source/documentation.rst`` file with new itom version.
* Create new folder ``../vM.M.P``. 
* Run script ``../build/itom/doc/userDoc/create-doc.py`` in the build folder of [itom](https://github.com/itom-project/itom).
* Check in line 44 for ``buildernames = ["qthelp", "html", "latex"]`` to at least build in several formats.
* Copy the folder ``../build/itom/docs/userDoc/build/html/`` to the folder ``../latest`` of this repository. 
* Script will ask you if you want to run doxygen. Select the ``doxygen.exe``.  
* Copy ``../build/itom/doc/doxygen/html/`` files to the folder ``../latest/doxygen/``
* Finally commit and push to the repository. The website is available afterwards. 
