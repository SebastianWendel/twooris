#!/usr/bin/env python

###############################################################################################

__author__      = "sebastiian wendel"
__copyright__   = "copyright 2012, attraktor e.v."
__license__     = "glp"
__version__     = "0.0.1"
__status__      = "production"
__install__     = "sudo aptitude install python-simplejson python-httplib2 python-oauth2"

###############################################################################################

dooris_url      = "http://dooris.koalo.de/door.txt"
temp_folder     = "/tmp"
temp_file       = "twooris"
config_file     = "twooris.conf"

###############################################################################################

import urllib2
import twitter

api = twitter.Api()
response = urllib2.urlopen(dooris_url)
html = response.read()


config = open(temp_folder + '/' + temp_file, "wb")

file_input = open(temp_folder + '/' + temp_file, "wb")
str = file_temp.read(10);
print "Read String is : ", str
fo.close()

api = twitter.Api(consumer_key='consumer_key', consumer_secret='consumer_secret', access_token_key='access_token', access_token_secret='access_token_secret')





file_temp = open(temp_folder + '/' + temp_file, "wb")
file_temp.write(html);
file_temp.close()

