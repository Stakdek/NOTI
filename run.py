# -*- coding: utf-8 -*-
import os
import random
import urllib
import urllib2
#source of messages
import data

PATH=os.path.dirname(os.path.abspath( __file__ )) # get current path and merge with imager path
IMAGE_PATH_PARAM=" -i '" + PATH + "/no-country-for-old-men-3.jpg' "
PARAM=" --expire-time=1 -t 20000 " # set params current param: set expire-time to 20 second
MESSAGE=""
SUBJECT=" '→→Sprüche, Tipps und Philosophien←←' "

def send_cmd(MESSAGE):
    '''
    get message
    fetch command and
    send and print command to terminal
    '''
    print MESSAGE
    os.system('notify-send ' + PARAM + IMAGE_PATH_PARAM + SUBJECT + MESSAGE )

def fetch_message_offline():
    '''
    get length of data
    choose random string from data
    fetch it to a message together
    '''
    length = len(data.data) - 1
    rand_message = random.randint(0, length)
    message = data.data[rand_message]
    MESSAGE="'"+ message +"'"
    send_cmd(MESSAGE=MESSAGE)

    '''
    nottizen

    entweder automatisiertes erweitern der sprüche oder aus dem internet holen und dann anzeigen
    run.py in mehrere biblios packen


    '''
fetch_message_offline()
