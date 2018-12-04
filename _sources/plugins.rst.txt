.. _sec-plugins:

Plugins
=========

One of the most important features of **itom** is its plugin system. Using plugins, **itom** is able to communicate with many hardware components, such as framegrabbers, cameras, motor stages or other devices. 
Furthermore it is possible to develop user defined algorithms in C/C++ and put them into an algorithm plugin. The call to these algorithms is then possible via the Python scripting language or other plugins.


.. container:: mdl-grid

	.. button:: :text: Plugin Documentation
	 :link: .\plugindoc\index.html


The **itom** setup already comes with many exemplary plugins. Other plugins are available as source files in the corresponding `Plugins repository <https://bitbucket.org/itom/plugins>`_. 
Furthermore, the SDK of **itom** provide some template files for creating your own plugin using CMake and the development environment of your choice (see `CMake Plugin <http://itom.bitbucket.org/latest/docs/07_plugins/development/pluginCreateCMake.html>`_).


Add a plugin to itom
---------------------

Requirements to load a plugin library at startup of **itom**:

1. The plugin library is contained in any subfolder of the folder **plugin** contained in the application (root) directory of **itom**
2. If **itom** is build in debug, the plugin must be compiled in debug as well. The same holds for the default release versions.
3. If the plugin depends on further 3rd party libraries, these libraries must be accessible by your operating system (on Windows: Their path must be contained in the PATH environment variable OR the necessary DLLs must be in the **lib** subfolder of **itom** or in the root directory of **itom**). Only if the plugin is able to load further libraries by means of a delay load mechanism, it is possible to also put 3rd party libraries in arbitrary folders.
4. If your plugin depends on 3rd party libraries, please make sure that all plugins use exactly the same version of the same library.

Available plugins
------------------

The following plugins are contained in the open source `Plugins repository <https://bitbucket.org/itom/plugins>`_ (and some of them are also already included in the setup of **itom**):

.. csv-table::
	:header: Cameras
	:widths: auto
	:class: mdl-table
	
	AndorSDK3, Andor Cameras supported by their SDK3
	AvantesAvaSpec, Avantes AvaSpec Spectrometer
	AvtVimba, AVT Cameras driven by Vimba interface
	CMU1394, Firewire cameras supported by CMU1394 driver
	CommonVisionBlox, GenICam via Common Vision Blox
	DummyGrabber, Virtual camera providing random noise images
	FileGrabber, Virtual file camera (grabbing from image files)
	FireGrabber, Cameras supported by FirePackage from Allied Vision
	Genicam, Camera control of devices that support the GenICam standard
	IDSuEyeCamera, All IDS Imaging cameras
	MSMediaFoundation, "USB Plug&Play Cameras, Webcams, including cameras from The Imaging Source"
	NITWidySWIR, Cameras from company NIT (tested with USB2 WidySWIR 640U-S)
	OpenCVGrabber, USB Plug&Play Cameras and further cameras supported by OpenCV
	PCOCamera, PCO Cameras supported by the pco.sdk
	PCOPixelFly, PCO Pixelfly qet cameras with frame grabber board
	PCOSensicam, PCO Cameras supported by the pco.sensicam SDK
	PGRFlyCapture, "Point Grey cameras (USB3) supported by Fly Capture driver"
	PmdPico, "pico flexx, pico maxx, pico monster"
	QCam, Cameras from company QImaging
	ThorlabsCCS,
	Vistek, Cameras from company Vistek
	VRMagic, USB Cameras from company VRMagic (tested with framegrabber VRmAVC-2)
	Ximea, "Cameras from company Ximea (tested with various xiQ USB3 cameras, mono & color)"

.. csv-table:: 
	:header: Motors/Actuators
	:widths: 300 400
	:class: mdl-table
	
	AerotechEnsemble, Axes from company Aerotech that can be driven using the Aerotech Ensemble interface
	DummyMotor, Virtual dummy motor with axis
	FirgelliLAC, One axis motor controller FirgelliLAC
	LeicaMotorFocus, "Z-stage controller of Leica MZ12 or MZ12.5"
	NanotecStepMotor, Motor-Controller Nanotec SMCP
	PiezosystemJena_NV40_1, One axis piezo actuator from Piezosystem Jena (NV 40/1 CLE)
	PI GCS2, Piezo controllers from Physik Instrumente - controlled by GCS2 commands (e.g. E753)
	PI PiezoCtrl, "Piezo controller E662, E-816, E-621, E-625, E665 from Physik Instrumente"
	ST8SMC4USB (Standa), Motor-Controller STANDA 8SMC4-USB-B8-1
	ThorlabsBP, One or multi-axis piezo controllers of type Thorlabs Benchtop Piezo
	ThorlabsISM, "Control Thorlabs Integrated Stepper Motors, e.g. K10CR1 Rotation Stage"
	UhlRegister, Stages from Uhl (also compatible with Lang)
	UhlText, Stages from Uhl (also compatible with Lang and Merzhaeuser)
	usbMotion3XIII, USB Motion 3x III controller from COPTONIX GmbH (www.coptonix.com)

.. csv-table:: 
	:header: DataIO
	:widths: 300 400
	:class: mdl-table

	CyUSB, Any generic USB devices
	DispWindow, OpenGL based widget to show cosine and graycode sequences
	GLDisplay, OpenGL based widget to show any textures given by dataObjects
	GWInstekPSP, "Power supplies PSP-405, PSP-603, PSP-2010 of company GWInstek"
	hidApi, Any generic HID device
	libUSB, Any generic USB devices
	LibModBus, Modbus communication over TCP/IP and RTU
	SerialIO, "COM-Ports (Windows), ttySx and ttyUSBx (Linux)"
	SuperlumBL, Lightsource from company Superlum
	SuperlumBS, Lightsource from company SuperlumBS
	ThorlabsPowerMeter, Thorlabs Power and Energy Meter Consoles PM100x

.. csv-table:: 
	:header: AD-Converter
	:widths: 300 400
	:class: mdl-table

	MeasurementComputing, Access to USB digital to analog converter
	NI-DAQmx, "NI-ADDA Converter (requires NI-DAQmx Lib and DLL)"

.. csv-table:: 
	:header: Algorithm/Filter
	:widths: 300 400
	:class: mdl-table

	basicFilters, Many filters for dataObject
	basicGPLFilters, "Basic filter for dataObject (Despeckle,...)"
	dataObjectArithmetic, Arithmetic calculations for dataObject
	dataObjectIO, Import/Export functions for dataObject
	fittingFilters, Fitting planes and surfaces
	FFTWfilters, Filter for FFT calculations
	FringeProj, Fringe projections methods
	OpenCV Filters, Wrapped algos for image processing
	PclTools, pointClouds and polygonMesh methods
	RawImport, Loading raw image format
	Roughness, Algo for roughness evaluation
	X3P IO, Load and Save x3p files





Plugin Development
-------------------

If you have any hardware component that is not yet supported by **itom** or if you need to have a specific algorithm implemented as algorithm plugin, you have the following possibilities:

* Start to develop your own plugin library and make this plugin available to anybody if you want to. More information about this can be found under `Plugin Development <http://itom.bitbucket.org/latest/docs/07_plugins/development/plugin-development.html>`_
* Since not all plugins are already available in the internet, ask us if for instance we already have the plugin you need.
* Feel also free to contact us if you want us to develop a plugin for you.
* Register to the `mailing list <https://lists.sourceforge.net/lists/listinfo/itom-discussions>`_ and write further questions.

