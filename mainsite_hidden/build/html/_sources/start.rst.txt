.. _sec-start:

Get Started
====================================

| **WELCOME TO ITOM!** Before you start measuring and programming the world around you, you'll need to set up the software on your PC or Mac.
| Here you'll find information and help on **HOW TO START USING ITOM!**
| Below we've summarized easy instructions to install and use our software

Introduction
--------------

| The itom software (ITOM) allows to interactively create measurements with labratory equipment down to simple webcams.
| It is also capable of data generation, data mining, data analysis and much more data stuff...
| The built-in Qt-designer enables the user to create neat looking GUIs for end-user measurement processes or automation.
| In short, it combines many advantages of both **Matlab** and **Labview** in one free software!

.. glossary::

	Measurement software
		| Data aquisition, Image recording and Signal detection with Plug'n'Play hardware integration.
		| Equipped with its own filters, algorithms and data analysis plugins.
		| Plot the data in awesome looking graphs, save and export data results in various formats.
		
	Easy programming (PYTHON)
		| ITOM is one of the best **PYTHON IDE** on the web with lots of features to make your python experience alot easier
		| Create your own **Scripts** or type in commands directly into to **Console**
		| Install any python packages with our simple **Package Manager**
		| Debug your scripts on-the-fly with the our included **Debugger**
		
	Python packages
		| Powerful through the greatest range of additional extensions: **Python packages**
		| Examples are: Matplotlib, Scipy, Numpy for easy mathematical calculations - up to skimage, scikit-learn and TensorFlow for MachineLearning and AI



Installation
------------------

Currently the Setup-Version is only available for WINDOWS OS. MacOS and Linux Distros need to compile source from `Git <https://bitbucket.org/itom/itom/overview>`_

| Get the latest version from :ref:`sec-downloads` page or see the link below.

**Download Setup .EXE-File**

.. container:: mdl-grid

	.. button:: :text: SourceForge
	   :link: https://sourceforge.net/projects/itom/files/latest/download

.. glossary::

	Run the Setup file
		| After the download, proceed with the installation by opening the Setup.exe. (You might be asked for *Administrator rights* to continue)
		| 
		
	Select the Destination folder:
	
		|setup1|
		
	Choose Components and Packages to include:
		| Python packages: Numpy, SciPy and Matplotlib need to be included
		| itom SDK is needed if you want to include further plugins
		
		|setup2|
		
	Click on **Install** in the summary:
		
		|setup3|
		
	*Optional: If not already installed, VisualC++ will be installed*
		
		|setupVC|
		
	Automatic install of Python packages:
		
		|setupPip|
		
	Install done:
	
		|setup4|
		
	Open itom.exe to start:
	
		|setup5|

.. |setup1| image:: _static\\setup1.jpg
                         :width: 400px
.. |setup2| image:: _static\\setup2.png
                         :width: 400px
.. |setup3| image:: _static\\setup3.png
                         :width: 400px
.. |setup4| image:: _static\\setup4.jpg
                         :width: 400px
.. |setup5| image:: _static\\setup5.jpg
                         :width: 600px
.. |setupPip| image:: _static\\setupPip.png
                         :width: 400px
.. |setupVC| image:: _static\\setupVC.png
                         :width: 400px

How to start using ITOM
-----------------------

First of all, let's introduce you to the IDE and your first steps using itom.

* Visit the `Getting Started <https://itom.bitbucket.io/latest/docs/03_gettingStarted/getting-started-lvl2.html>`_ part of our documentation to get an overview.

* Use our `Cheatsheet for Python with itom <documents/itom_cheatsheet.pdf>`_ to learn some basics

*	See `Documentation <https://itom.bitbucket.io/latest/docs>`_ for information on itom details and functions