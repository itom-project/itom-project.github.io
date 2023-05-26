===================
 HBMSpider8
===================

=============== ========================================================================================================
**Summary**:    :pluginsummary:`HBMSpider8`
**Type**:       :plugintype:`HBMSpider8`
**License**:    :pluginlicense:`HBMSpider8`
**Platforms**:  not known
**Devices**:    HBMSpider8
**Author**:     :pluginauthor:`HBMSpider8`
**Requires**:	SerialIO
=============== ========================================================================================================
 
Overview
========

.. pluginsummaryextended::
    :plugin: HBMSpider8
	
The plugin implements the Spider8 functions for the analog-digital-converter from HBM. 
The installation needs an initialized serial port 

Initialization
==============
  
The following parameters are mandatory or optional for initializing an instance of this plugin:
    
    .. plugininitparams::
        :plugin: HBMSpider8


Parameters
==========

These parameters are available and can be used to configure the **NI-DAQmx** instance. 
During the runtime of an instance, the values of these parameters are obtained by the method *getParam*, 
writeable parameters can be changed using *setParam*.

**SerialIO**: {Union[itom.dataIO, itom.actuator]}
	Open com-port where Spider8 device is connected 

**baud**: {int}
	baud rate for hbm
	Value range: [9600, 76800], Default: 57600
