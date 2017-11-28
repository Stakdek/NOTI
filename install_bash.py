# -*- coding: utf-8 -*-
import os

PATH=os.path.dirname(os.path.abspath( __file__ )) # get current path and merge with imager path
BASH_PATH = PATH
PARAM="NOTI.sh"
MESSAGE="Ein Bash Script zum Ausführen des Scripts wurde erstellt"
SUBJECT=" '→→Sprüche, Tipps und Philosophien←←' "
BASH='python ' + '"' + BASH_PATH + '/run.py' + '"'
print BASH
def send_cmd(PATH, PARAM):
    '''
    fetch path from runner-script
    touch File
    open file and write bash command with path to run the run.py
    '''
    runner_path = PATH + PARAM
    os.system('touch "' + PATH + '"' + PARAM)
    bash_in = open(runner_path)
    bash_out = open(runner_path,"w")
    bash_out.write(BASH)
    bash_in.close()
    bash_out.close()

def create_bash(PATH, PARAM):
    '''
    get path and params
    cut path to get path from /home/…/Schreibtisch/
    '''
    path_str = ''
    PATH=PATH.split('/',4)
    del_path = PATH[4]
    PATH.remove(del_path)
    for path_item in PATH:
        path_str = path_str+path_item+'/'
    PATH=path_str
    send_cmd(PATH=PATH, PARAM=PARAM)

create_bash(PATH=PATH, PARAM=PARAM)
