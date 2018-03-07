=====================
Hardware
=====================


.. image:: ..\\_static\\drag&dropHW.svg
    :alt: drag & drop hardware
    :width: 30%
    :align: left


* Hardware (Grabber, A/D convertes, raw IO, actuator) can be included as hardware plugins
* Homogenous hardware implementation (use of same script to control different devices of same hardware type)
* Complex algorithms, filters, GUIs or widgets can be included as software plugins
* Already implemented plugins: `Plugins <../plugins.html>`_

Another main feature of ITOM is its simple integration of hardware.

The core application of itom with its graphical user interface already gives access to the most important functions such that small setups and experiments can quickly be adjusted and installed.

*Itom* benefits from a modular software architecture. Therefore, all external hardware components are provided by external libraries (plugins) that are dynamically loaded at runtime. 
All itom-plugins are divided into different groups, where each group is defined by a specific interface, allowing communication with the corresponding plugin via itom or specific scriptable commands. 
One group of plugins provides access to hardware components, such as cameras or actuators.
Since their implementation must follow the rules given by specific interfaces, it is guaranteed that the call to any camera or actuator plugin is the same, hence, plugins can be simply changed without adaption to your scripted code. 
Other plugins contain data processing and analysis algorithms as well as complex user interfaces like additional windows or dialogs. 
Another group of plugins provides plotting and figure components for showing live images of cameras or visualizing other data structures. 
One example of enhanced plugin is the project MacroSim, that provides a GUI for a GPU accelerated ray tracing engine.
