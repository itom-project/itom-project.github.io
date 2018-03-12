# coding=iso-8859-15 

# -*- coding: utf-8 -*-

#this file requires the python package: sphinxcontrib-fulltoc (obtain via pip)

import os
import sys
from os import path
from sphinx.util import format_exception_cut_frames, save_traceback
from sphinx.util.console import darkred, nocolor

from sphinx.application import Sphinx
from docutils.utils import SystemMessage
import subprocess
import itom
import __main__
import shutil
import glob
import distutils.dir_util
import __main__
    
buildernames = ["html"]

def pathConv(p):
    if (os.sep == "\\"):
        return p.replace("/","\\")
    return p

def createDocumentation(buildernames):

    all_files = True
    filenames = False
    confoverrides = {}
    freshenv = True #fresh environment variable, else False

    basedir = itom.getCurrentPath()
    srcdir = pathConv(os.path.join(itom.getCurrentPath(), "source_plugins"))
    confdir = pathConv(os.path.join(itom.getCurrentPath(), "source_plugins"))
    
    for buildername in buildernames:
        outdir = pathConv(os.path.join(itom.getCurrentPath(),"build/" + buildername + "/plugins"))
        doctreedir = pathConv(os.path.join(itom.getCurrentPath(),"build/doctrees"))
        postcopydir = pathConv(os.path.join(itom.getCurrentPath(), ".."))
            
        confoverrides = {}
    
        app = Sphinx(srcdir, confdir, outdir, doctreedir, buildername,
                     confoverrides, sys.stdout, sys.stderr, freshenv)

        nocolor()

        if not app.builder:
            raise RuntimeError

        if all_files:
            app.builder.build_all()
        elif filenames:
            app.builder.build_specific(filenames)
        else:
            app.builder.build_update()
        
        #if (buildername == "html"):
            #distutils.dir_util.copy_tree(outdir, postcopydir)
            #print("files copied to ", postcopydir)

def setOverloads():
    
    res = {}
    
    d = {"license": "licensed under LGPL",
            "description": "Video4Linux2 camera grabber (USB-Cams)",
            "detaildescription":"This plugin uses the Video4Linux2 (V4L2) for capturing supported camera devices (e.g. ordinary USB or integrated cameras). \n\n"\
"This driver detects an internal list of connected cameras. The parameter *cameraNumber* indicates the device to open, it is linked to the devices (/dev/videoX, where X is the *cameraNumber*). \n\n" \
"Any detected and supported device can offer multiple framerates and sizes. Use the parameter *mediaTypeID* to select the right value. Open your device with *mediaTypeID* = -1 \n"\
"to let the plugin print a list of supported formats (the plugin initialization then stops with a desired error).",
            "author":"V. Ferreras Paz, M. Gronle, ITO, University Stuttgart",
            "type":"DataIO",
            "version":"0.0.1"}
    res["V4L2"] = d
    
    d = {"license": "licensed under LGPL",
            "description": "Firewire - Fire Package Capture (Windows) / FireForLinux (Linux)",
            "detaildescription":"Camera plugin that uses the FireGrab driver from the AVT FirePackage in order to communicate with corresponding cameras. The cameras are connected to the computer via \
firewire. \n\
\n\
This plugin can only be loaded and used once the AVT FirePackage driver has been correctly installed on your computer. For more information about AVT FirePackage and their \
license browse to http://www.alliedvisiontec.com. This plugin was mainly tested with the cameras AVT Malin, Guppy and Pike. Not all parameters are supported by this plugin.",
            "author":"G. Baer, A. Bielke, M. Gronle, ITO, University Stuttgart",
            "type":"DataIO",
            "version":"1.0.0"}
    res["FireGrabber"] = d
    
    d = {"license": "licensed under LGPL. For further license information of the **xiQ** interface from Ximea see its specific documentation.",
            "description": "Ximea xiQ-Camera",
            "detaildescription":"itom plugin for cameras from Ximea (xiQ interface). It has only been tested under Windows and supports monochrome cameras. \n\
\n\
For compiling this plugin, please set the CMake variable **XIMEA_APIDIR** to the base directory of the Ximea API. This directory must contain the file *m3Api.h*.",
            "author":"C. Kohler, twip optical solutions GmbH, Stuttgart",
            "type":"DataIO",
            "version":"0.0.1"}
    res["Ximea"] = d
    
    d = {"license": "licensed under LGPL. For the license information of **FlyCapture2** see the specific documentation of Point Grey Research.",
            "description": "Plugin for PGR FlyCapture2 Camerainterface",
            "detaildescription":"itom plugin for Point Grey Research cameras that can be run with the **FlyCapture2** camera interface (e.g. the USB 3.0 Flea3 camera). \n\
\n\
For compiling this plugin, install FlyCapture2 in 32bit or 64bit depending on **itom** and set the CMake variable **PGRFLYCAP_API_DIR** to the base directory of FlyCapture2.",
            "author":"W. Lyda, ITO, University Stuttgart",
            "type":"DataIO",
            "version":"0.0.1"}
    res["PGRFlyCapture"] = d
    
    d = {"license": "licensed under LGPL / ISO5436-2 XML under LPGL",
            "description": "x3p Import/Export",
            "detaildescription":"This plugin provides methods to save and load dataObjects in/from the file format 'x3p'. \
This format is specified in ISO 25178 - Geometrical product specification (GPS). \n\
\n\
The library ISO 5436-2 XML, that is necessary for this plugin and included in the sources, \n\
is licensed under the LGPL license and uses further libraries. For more information about the license \n\
of the library itself see www.opengps.eu",
            "author":"C. Kohler, ITO, University Stuttgart",
            "type":"Algorithm",
            "version":"0.0.1"}
    res["x3pio"] = d
    
    d = {"license": "licensed under LGPL",
            "description": "Filters and methods for pointClouds and polygonMeshes",
            "detaildescription":"This plugin contains methods for filtering, transforming, saving and loading \n\
point clouds and polygon meshes. Most methods are wrappers for functions provided \n\
by the open source project PointCloudLibrary (pcl). The function calls are usually \n\
implemented for the cloud types supported by the itom classes itom.pointCloud \n\
and itom.polygonMesh (XYZ,XYZI,XYZRGBA,XYZNormals...). \n\
\n\
This library uses also methods from the current pcl version 1.7.1, however also \n\
compiles with older versions. In this case some methods are not compiled. \n\
\n\
This plugin also covers the methods for loading and saving point clouds and polygon \n\
meshes to common formats like pcd, ply, stl, obj... Once the plugin is loaded \n\
itom in general is also able to load and save such structures using the methods provided \n\
by this plugin.",
            "author":"M. Gronle, ITO, University Stuttgart",
            "type":"Algorithm",
            "version":"0.0.1"}
    res["PclTools"] = d
    
    __main__.__dict__["pluginOverloads"] = res
            

if (__name__ == "__main__"):
        
        setOverloads()
        createDocumentation(buildernames)
