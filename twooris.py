#!/usr/bin/env python
#-----------------------------------------------------------------------------------------------------
__author__      = "sebastian wendel"
__copyright__   = "copyright 2012, attraktor e.v."
__license__     = "GPL"
__version__     = "0.2.1"
#-----------------------------------------------------------------------------------------------------

import os
import sys
import time
import linecache
import ConfigParser
import urllib2
import twitter
import RPi.GPIO as GPIO

#-----------------------------------------------------------------------------------------------------
# static configuration
#-----------------------------------------------------------------------------------------------------

config_file = "/opt/twooris/twooris.cfg"
temp_file = "/tmp/twooris"

#-----------------------------------------------------------------------------------------------------
# initialisation
#-----------------------------------------------------------------------------------------------------

# LOAD TIMESTAMP
timestamp = time.time()

# LOAD CONFIG FILE
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(config_file)

# LOAD GPIO SETTINGS
gpio_led      = int(config.get("gpios", "led"))
gpio_switch   = int(config.get("gpios", "switch"))

# INITIALISE RASPBERRY PI GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio_led, GPIO.OUT)
GPIO.setup(gpio_switch, GPIO.IN)

# INITIALISE TWITTER API
api = twitter.Api(consumer_key=config.get("twitter", "consumer_key"), \
                  consumer_secret=config.get("twitter", "consumer_secret"), \
                  access_token_key=config.get("twitter", "access_token_key"), \
                  access_token_secret=config.get("twitter", "access_token_secret"))

#-----------------------------------------------------------------------------------------------------
# initialisation
#-----------------------------------------------------------------------------------------------------

# GET STATE OF THE DOOR SWITCH
input_value = GPIO.input(gpio_switch)

# GET LATEST STATE FOR TEMP FILE
latest_change = linecache.getline(temp_file, 3)

#-----------------------------------------------------------------------------------------------------
# program logic
#-----------------------------------------------------------------------------------------------------

# IF TEMP FILE EXISTS CHECK STATE FOR TEMP AND COMPARE TO CURRENT
if os.path.exists(temp_file):
  file_input = open(temp_file, "r+")
  input_str = file_input.readlines()
  file_input.close()
  # IF TEMP INPUT IS NOT EMPTY CONTINUE
  if str(input_str[0]) != "":
    file_input = open(temp_file, "wb")
    file_input.write(str(input_value) + "\n")
    file_input.write(str(timestamp) + "\n")
    file_input.write(str(timestamp))
    file_input.close()
    # IF TEMP AND CURRENT STATE IS NOT IDENTICAL POST ON TWITTER
    if not str(input_value).rstrip() in input_str[0].rstrip():
      if input_value == False:
        # IF DOOR IS OPEN POST MESSEGE OPEN ON TWITTER
        status = api.PostUpdate(time.strftime("%x %X ") + config.get("messeges", "open"))
        # IF DOOR IS OPEN DISABLE THE LED
        GPIO.output(gpio_led, False)
      else:
        # IF DOOR IS CLOSED POST MESSEGE CLOSED ON TWITTER
        status = api.PostUpdate(time.strftime("%x %X ") + config.get("messeges", "closed"))
        # IF DOOR IS CLOSED ENABLE THE LED
        GPIO.output(gpio_led, True)
      print status.text
      sys.exit(0)

# WRITE CURRENT STATE TO TEMP FILE IF FILE NOT EXISTS
file_input = open(temp_file, "wb")
file_input.write(str(input_value) + "\n")
file_input.write(str(timestamp) + "\n")
file_input.write(str(latest_change))
file_input.close()
