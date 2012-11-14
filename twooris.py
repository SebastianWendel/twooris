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
semaphore_file  = '/tmp/twooris'

###############################################################################################

import os
import ConfigParser
import urllib2
import twitter

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(config_file)

response = urllib2.urlopen(config.get("dooris", "dooris_url"))
html = response.read()
html_lines = html.splitlines()

api = twitter.Api(consumer_key=config.get("twitter", "consumer_key"), consumer_secret=config.get("twitter", "consumer_secret"), access_token_key=config.get("twitter", "access_token_key"), access_token_secret=config.get("twitter", "access_token_secret"))

if os.path.exists(semaphore_file):
  file_input = open(semaphore_file, "r+")
  input_str = file_input.readlines()
  if str(input_str[0]) != '':
    if not html_lines[0] in input_str[0]:
      status = api.PostUpdate('The door is ' + html_lines[0] + '.')
      print status.text
  file_input.close()

file_input = open(semaphore_file, "wb")
file_input.write(html);
file_input.close()

###############################################################################################
