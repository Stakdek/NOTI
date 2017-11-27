URL='https://www.google.de/'
def fetch_message_online(URL):
    '''
    get data from page
    filter a message

    begin message key word '<h3>Spruch des Tages:</h3>'
    end message key word '<hr>'

    begin second message key word '<h3>Und noch ein Spruch:</h3>'
    end second message key word '</div>'
    '''
    print URL
    resp = urllib2.urlopen(URL)
    print resp
    html = response.read()
    print html
    if 'Spruch des Tages:' in html:
       print 'YEEEEES'



    '''BAUSTELLE

    import urllib

    resp = urllib.urlopen('https://somewebsite.com') # open url
    page = resp.read()                               # copy website source to 'page' variable
    text_file = open("Output.txt", "w")              # open txt file
    text_file.write(page)                            # insert website source into txt file
    text_file.close()


    nottizen

    entweder automatisiertes erweitern der sprüche oder aus dem internet holen und dann anzeigen
    run.py in mehrere biblios packen


    '''



online = True
if online is True:
    fetch_message_online(URL=URL)
elif online is None:
    dehtml('jello')
else:
    fetch_message_offline()

'''




# html pasrer start

from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()

def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text

    print(dehtml(text))

# html pasrer end
# switch from online to offline
online = True
if online is True:
    fetch_message_online(URL=URL)
elif online is None:
    dehtml('jello')
else:
    fetch_message_offline()
'''
