#!/usr/bin/env python

__author__      = "sebastian wendel"
__copyright__   = "copyright 2012, attraktor e.v."
__license__     = "GPL"
__version__     = "0.0.1"

config_file     = "twooris.cfg"
semaphore_file  = '/tmp/twooris'

import os
import time
import datetime
import ConfigParser
import urllib2
import twitter
import RPi.GPIO as GPIO

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(config_file)

GPIO.setmode(GPIO.BCM)
GPIO.setup(config.get("gpios", "led"), GPIO.OUT)
GPIO.setup(config.get("gpios", "switch"), GPIO.OUT)
api = twitter.Api(consumer_key=config.get("twitter", "consumer_key"), consumer_secret=config.get("twitter", "consumer_secret"), access_token_key=config.get("twitter", "access_token_key"), access_token_secret=config.get("twitter", "access_token_secret"))


t = datetime.datetime.now()
print "Epoch Seconds:", time.mktime(t.timetuple())

'''
var=1
while var==1 :
    GPIO.output(18, False)
    time.sleep(1)
    GPIO.output(18, True)
    time.sleep(1)


if os.path.exists(semaphore_file):
  file_input = open(semaphore_file, "r+")
  input_str = file_input.readlines()
  if str(input_str[0]) != '':
    if not html_lines[0] in input_str[0]:
      status = api.PostUpdate('The Attraktor door is ' + html_lines[0] + '.')
      print status.text
  file_input.close()

file_input = open(semaphore_file, "wb")
file_input.write(html);
file_input.close()
'''