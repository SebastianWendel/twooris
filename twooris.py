#!/usr/bin/env python

###############################################################################################

__author__      = "sebastian wendel"
__copyright__   = "copyright 2012, attraktor e.v."
__license__     = "glp"
__version__     = "0.0.1"
__install__     = """

https://dev.twitter.com/apps

cat >> twooris.cfg << 'EOF'
[dooris]                                                                                                                                                   
dooris_url          = http://dooris.koalo.de/door.txt

[twitter]
consumer_key        =
consumer_secret     =
access_token        =
access_token_secret =
EOF

sudo aptitude install python-simplejson python-httplib2 python-oauth2 """

###############################################################################################

config_file     = "twooris.cfg"
semaphore       = '/tmp/twooris'

###############################################################################################

import os
import ConfigParser
import urllib2
import twitter

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(config_file)

response = urllib2.urlopen(config.get("dooris", "dooris_url"))
html = response.read()

if os.path.exists(semaphore):
  file_input = open(semaphore, "r+")
  input_str = file_input.readlines()
  if str(input_str[0]) != '':
    if 'locked' in input_str[0]:
      print input_str[0]
  file_input.close()
else:
  file_input = open(semaphore, "wb")
  file_input.write(html);
  file_input.close()

'''
  test_string = file_input.read();
  print test_string

fo.close()

api = twitter.Api()
api = twitter.Api(consumer_key='consumer_key', consumer_secret='consumer_secret', access_token_key='access_token', access_token_secret='access_token_secret')

file_temp = open(temp_folder + '/' + temp_file, "wb")
file_temp.write(html);
file_temp.close()
'''
