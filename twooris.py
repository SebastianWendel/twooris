#!/usr/bin/env python

__author__      = "sebastian wendel"
__copyright__   = "copyright 2012, attraktor e.v."
__license__     = "GPL"
__version__     = "0.2.0"

config_file     = "twooris.cfg"
semaphore_file  = '/tmp/twooris'

import os
import sys
import time
import linecache
import ConfigParser
import urllib2
import twitter
import RPi.GPIO as GPIO

timestamp = time.time()

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(config_file)

gpio_led      = int(config.get("gpios", "led"))
gpio_switch   = int(config.get("gpios", "switch"))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio_led, GPIO.OUT)
GPIO.setup(gpio_switch, GPIO.IN)

input_value = GPIO.input(gpio_switch)

api = twitter.Api(consumer_key=config.get("twitter", "consumer_key"), consumer_secret=config.get("twitter", "consumer_secret"), access_token_key=config.get("twitter", "access_token_key"), access_token_secret=config.get("twitter", "access_token_secret"))

latest_change = linecache.getline(semaphore_file, 3)

if os.path.exists(semaphore_file):
  file_input = open(semaphore_file, "r+")
  input_str = file_input.readlines()
  file_input.close()
  if str(input_str[0]) != '':
    if not str(input_value).rstrip() in input_str[0].rstrip():
      file_input = open(semaphore_file, "wb")
      file_input.write(str(input_value) + "\n")
      file_input.write(str(timestamp) + "\n")
      file_input.write(str(timestamp))
      file_input.close()
      if input_value == False:
        status = api.PostUpdate(time.strftime('%X %x ') + config.get("messeges", "open"))
        GPIO.output(gpio_led, False)
      else:
        status = api.PostUpdate(time.strftime('%X %x ') + config.get("messeges", "closed"))
        GPIO.output(gpio_led, True)
      print status.text
      sys.exit(0)

file_input = open(semaphore_file, "wb")
file_input.write(str(input_value) + "\n")
file_input.write(str(timestamp) + "\n")
file_input.write(str(latest_change))
file_input.close()
