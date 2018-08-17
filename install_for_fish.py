# -*- coding: utf-8 -*-
import os
# WIP
PATH=os.path.dirname(os.path.abspath( __file__ )) # get current path and merge with imager path
PARAM="fish_greeting.fish"
FISH_PATH = PATH
MESSAGE="Ein Bash Script zum Ausführen des Scripts wurde erstellt"
FISH='''
function fish_greeting
    python ''' + FISH_PATH + '''/run.py ''' + FISH_PATH + ''' noNotify
end
'''

def send_cmd(PATH, PARAM):
    '''
    fetch path from runner-script
    make folder
    touch File
    open file and write fish function with path to run the run.py
    '''
    runner_path = PATH + PARAM
    os.system('mkdir ' + PATH)
    os.system('touch "' + PATH + '"' + PARAM)
    bash_in = open(runner_path)
    bash_out = open(runner_path,"w")
    bash_out.write(FISH)
    bash_in.close()
    bash_out.close()
    print 'fish_greeting - Function created'


def create_path(PATH, PARAM):
    '''
    get path and params
    cut path to get path from /home/…/Schreibtisch/
    '''
    path_str = ''
    PATH=PATH.split('/',4)
    del_path = PATH[4]
    PATH.remove(del_path)
    del_path = PATH[3]
    PATH.remove(del_path)
    for path_item in PATH:
        path_str = path_str+path_item+'/'
    PATH=path_str+'.config/fish/functions/'
    send_cmd(PATH=PATH, PARAM=PARAM)

create_path(PATH=PATH, PARAM=PARAM)
