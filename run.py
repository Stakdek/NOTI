# -*- coding: utf-8 -*-

'''
Regel des Zusammenbaus:
Entwirf Programme so,
dass sie mit anderen Programmen verknüpft werden können.
'''


import os
import random
import urllib
import urllib2
import sys
# import get_update
import json

PATH=os.path.dirname(os.path.abspath( __file__ )) # get current path and merge with imager path
IMAGE_PATH_PARAM=" -i '" + PATH + "/noo.jpg' "
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
    if len(sys.argv) < 3:
        os.system('notify-send ' + PARAM + IMAGE_PATH_PARAM + SUBJECT + MESSAGE )
        import get_update # get new quotes
    return MESSAGE

def fetch_message_offline():
    '''
    get length of data
    choose random string from data
    fetch it to a message together
    '''

    with open( sys.argv[1] + '/quotes.json') as file:
        quotes = json.load(file)
    length = len(quotes) - 1
    rand_message = random.randint(0, length)
    message = quotes[rand_message]['quote']
    MESSAGE="'"+ str(message.encode('utf-8')) +"'"
    send_cmd(MESSAGE=MESSAGE)

    '''
    nottizen

    entweder automatisiertes erweitern der sprüche oder aus dem internet holen und dann anzeigen
    run.py in mehrere biblios packen
    data_fetch.py to fetch to datas to one big data
    data to base 64 with JSON inside

    '''
fetch_message_offline()
