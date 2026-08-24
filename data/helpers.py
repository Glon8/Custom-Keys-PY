import os
import random
import time
import json

from pynput.keyboard import Controller as K

from .values import op

k = K()


# ===================================< SWITCH
# dic - dictionary to use
# key - from the dictionary to flip
def switch(dic, key):
    dic[key] = 1 - dic[key]


# ===================================< KEY PRESS
# key - to press
# delay - between press and release
def key_press(key, min_delay, max_delay):
    k.press(key)

    timeout = random.randint(min_delay, max_delay) / 1000
    time.sleep(timeout)

    k.release(key)


# ===================================< READ FILE
# file_path - to read from
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


# ===================================< PATH MTIME
# folder_path - to check mtime for
def dir_mtime(folder_path):
    newest = 0

    for root, dirs, files in os.walk(folder_path):
        try:
            newest = max(newest, os.path.getmtime(root))
        except OSError:
            pass

        for file in files:
            path = os.path.join(root, file)
            try:
                mtime = os.path.getmtime(path)
                if mtime > newest:
                    newest = mtime
            except OSError:
                pass;

    return newest


# ===================================< CONFIG PARSER
# string - to pars in to config
def config_parse(string):
    if string == '' or string is None:
        return

    config_pack = json.loads(string)

    for ind in range(len(config_pack)):
        for key, val in config_pack[ind].items():
            if key != 'name':
                op[ind][key] = val


# ===================================< FILES COUNT
def files_count(file_path):
    return sum(len(files) for _, _, files in os.walk(file_path))
