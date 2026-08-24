import os
import platform
import time

from rich.console import Console

from .values import op, seperator

console = Console()
# ===================================< VISUALS
def render():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    pos = 'on' if op[0]['display'] == 'plain' else chr(0x2705)
    neg = 'off' if op[0]['display'] == 'plain' else chr(0x274C)

    for thing in op:
        for att, stat in thing.items():
            if att == 'name':
                console.print(seperator + ' ' + str(stat))
            elif att == 'key_action' or att == 'key_trigger' or att == 'text' or att == 'path_from' or att == 'path_to' or att == 'note' or att == 'display' or att == 'dir_files':
                console.print(f"{att} : {stat}")
            elif att == 'count':
                console.print(f"{att} : {int(stat)} clicks")
            elif att == 'time':
                time_seconds = stat % 60
                console.print(f"{att} : {int((stat - time_seconds) / 60)} minutes {int(time_seconds)} seconds")
            elif att == 'backup_time':
                if stat == -1:
                    console.print(f"{att} : {stat}")
                else:
                    console.print(f"{att} : {time.ctime(stat)}")
            else:
                console.print(f"{att} : {pos if stat else neg}")