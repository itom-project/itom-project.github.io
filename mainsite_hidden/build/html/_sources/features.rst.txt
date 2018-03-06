.. _sec-features:



Features
=========

**Itom** is an open source software suite for operating measurement systems, laboratory automation and data evaluation.

One main application of **itom** is the development and operation of sensor and measurement system for instance in a laboratory environment. Therefore, the software has to be able to communicate with a wide range of different hardware systems, such as cameras or actuators and should provide a diversified and as complete as possible set of evaluation and data processing methods. Additionally, the rapid prototyping of modern measurement and inspection setups requires a system, where parameters or components can easily be changed at runtime, necessitating the availability of an embedded scripting language. Finally, when operating a measurement system, it is also desirable to extend the graphical user interface by system adapted dialogs and windows.

.. raw:: html

	<div class="mdl-grid">
			<div class="mdl-cell mdl-cell--12-col">
				<img class="" src="_static/desk_lg.jpg" width="130%" style="position:relative; ; left:-15%; margin:0 0" alt="itom desk"/>
			</div>
	</div>

When using itom you benefit from the following main features:

* The embedded Python scripting language (version 3) allows you to use all functionalities that are provided by Python or other freely available packages as Numpy, Scipy or Matplotlib. Additionally, itom is connected to the Python scripting language by the package itom that acts as an interface to the core application as well as all its plugins.
* For developing scripts, itom provides important functionalities like syntax highlighting, auto completion, debugging possibilities, workspace introspection...
* The core application of itom with its graphical user interface already gives access to the most important functions such that small setups and experiments can quickly be adjusted and installed.
* *itom* benefits from a modular software architecture. Therefore, all external hardware components are provided by external libraries (plugins) that are dynamically loaded at runtime. All itom-plugins are divided into different groups, where each group is defined by a specific interface, allowing communication with the corresponding plugin via itom or specific scriptable commands. One group of plugins provides access to hardware components, such as cameras or actuators. Since their implementation must follow the rules given by specific interfaces, it is guaranteed that the call to any camera or actuator plugin is the same, hence, plugins can be simply changed without adaption to your scripted code. Other plugins contain data processing and analysis algorithms as well as complex user interfaces like additional windows or dialogs. Another group of plugins provides plotting and figure components for showing live images of cameras or visualizing other data structures. One example of enhanced plugin is the project MacroSim, that provides a GUI for a GPU accelerated ray tracing engine.
* Measurement systems can be extended by specific user interfaces. Therefore, a WYSIWYG design tool allows the creation of personalized user interfaces at runtime without requiring C++ programming experience. Furthermore, it is possible to integrate itom's plot and visualization tools into these interfaces. Afterwards, interface elements can be connected to scripted functionalities. As a result, users can configure the appearance of their measurement system to optimally enable or protect the underlying functionalities.

Implementation
---------------

**Itom** is written in C++ using the open source framework Qt. Qt enhances the functionalities of C++, mainly by providing a cross-platform GUI, allowing itom to run on both Windows and Linux operating systems. Since itom is also designed for multi-core processors, its modules run partly in different threads that allow operating an actuator, simultaneously acquiring images while keeping the main window reactive for user interaction. Therefore, the core application, the python script engine as well as all plugins run in their separate threads.


.. toctree::
   :maxdepth: 1
   :hidden:
   
   features/python.rst
   features/opencv.rst
   features/qt.rst
   features/plots.rst
   features/hw.rst
   features/macrosim.rst
