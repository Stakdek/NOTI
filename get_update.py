# -*- coding: utf-8 -*-
import os
import random
import urllib
import urllib2
import re
import data #source of messages

HTML=''
URL='http://sprichwortgenerator.de/'


def fetch_message_online(URL):
    '''
    *WORKING*
    get data from page
    filter the message

    begin message key word '<div class="spwort"'
    end message key word '</div>'
    get the match and filter the message
    '''
    print ('get new message from: ' + URL)
    resp = urllib.urlopen(URL)
    # print resp
    HTML = resp.read()
    parsedHTML = re.search('<div class="spwort".*[</div>$]',str(HTML)) # match the message
    parsed_message = parsedHTML.group(0)[20:-6] # get juste the message
    return parsed_message


def update_data(parsed_message):
    '''
    *NOT WORKING*
    '''
    data.data.append(parsed_message)
    text_file = open("data.py", "w")              # open txt file
    text_file.write('# -*- coding: utf-8 -*- \ndata = ' + str(data.data))        # insert website source into txt file
    text_file.close()


def update():
    parsed_message = fetch_message_online(URL)
    print parsed_message
    # update_data(parsed_message)





update()
