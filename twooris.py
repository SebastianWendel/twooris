#!/usr/bin/env python

__author__      = "sebastiian wendel"
__copyright__   = "copyright 2012, attraktor e.v."
__license__     = "glp"
__version__     = "0.0.1"
__status__      = "production"

import urllib2

response = urllib2.urlopen('http://dooris.koalo.de/door.txt')
html = response.read()


print html
