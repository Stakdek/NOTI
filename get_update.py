# -*- coding: utf-8 -*-
import os
import random
import urllib
import urllib2
import re
import json

HTML=''
URL='http://sprichwortgenerator.de/'


def update(URL):
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
    parsed_message = parsedHTML.group(0)[20:-6] # get just the message
    # open json
    with open('quotes.json') as file:
        quotes = json.load(file)
    # check length
    print len(quotes)
    print parsed_message
    # fetch into list of dict
    data = [{"author" : "unknown", "quote" : parsed_message}]
    # fetch with list from file
    quotes = data + quotes
    with open('quotes.json', 'w') as outfile:
        json.dump(quotes, outfile)
    return


update(URL)
