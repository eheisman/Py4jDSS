# initPy4JDSS.py
# Evan Heisman
# USACE NWW-EC-H
# Initializes the Py4J Gateway Server from Jython so that regular old "C"Python can make calls to the HEC Java API.  Tested with Py4J 0.8.4.1.
# 17 Dec 2014
#
# Installation:
# 1) Install the latest version of Py4J module. (pip install py4j or grab the .tar.gz file from their website)
# 2) Place the Py4J .jar file in the HEC-DSSVue plugins directory.

# Instructions for use
# 1) Run this file in Jython or as a DSS-Vue Jython script
# 2) In Python, call 
#  >>> from py4j.java_gateway import JavaGateway
#  >>> gateway = JavaGateway()                   # connect to the JVM
#  >>> jhec = gateway.jvm.hec
#  >>> dssFile = jhec.heclib.dss.HecDss.open("C:/path/to/myfile.dss")
#
# and then you can operate on dssFile as if it was existing in HEC-DSSVue Jython world.
#  Remember, this only works as long as the Jython or HEC-DSSVue that called this program remains open.
#
# Since py4j java objects do not support python introspection Java's methods are needed.
# - here's an example
# to get class of an object, for example to check if a returned DSS Record is a TimeSeriesContainer, use:
#  >>> myRecord.getClass().toString()
#  and to get a list of methods on a java object:
#  >>> for m in dssfile.getClass().getMethods():
#  >>>     print m.toString()
#  see http://docs.oracle.com/javase/tutorial/reflect/index.html for more on reflection

## this is the entire script to open the GatewayServer
from java.lang import Object
from py4j import GatewayServer

##  Not sure why it requires an object  as a start point, but hey, this works.
server = GatewayServer(Object())
server.start()
#print("Server created")
## let this script run until finished accessing Java.
