# -*- coding: utf-8 -*-
import os
import random
import urllib
import urllib2

PATH=os.path.dirname(os.path.abspath( __file__ )) # get current path and merge with imager path
IMAGE_PATH_PARAM=" -i '" + PATH + "/no-country-for-old-men-3.jpg' "
PARAM=" --expire-time=1 -t 20000 " # set params current param: set expire-time to 20 second
MESSAGE=""
SUBJECT=" '→→Sprüche, Tipps und Philosophien←←' "
print PATH
def send_cmd(MESSAGE):
    '''
    fetch command and
    send command to terminal
    '''
    print MESSAGE
    os.system('notify-send ' + PARAM + IMAGE_PATH_PARAM + SUBJECT + MESSAGE )

def create_bash(PATH):
    '''
    get length of data
    choose random string from data
    fetch it to a message together
    TODO: crawl from website
    '''
    send_cmd(MESSAGE=MESSAGE)

create_bash(PATH=PATH)
