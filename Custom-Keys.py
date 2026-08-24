import time
import random
import threading
import os
import shutil

from rich.console import Console

from pynput.mouse import Controller as M, Listener as mL, Button
from pynput.keyboard import Controller as K, Listener as kL, HotKey, Key

from data.values import op, seperator
from data.visuals import render
from data.helpers import switch, key_press, config_parse, read_file, dir_mtime, files_count

# ===================================< PREP
console = Console()
temp_timer = None

k = K()
m = M()

# ===================================< KILL SWITCH
def ks_switch():
    ks = op[1]['stat']
    acc = op[2]
    afk = op[3]

    acc['stat'] = 0
    op[4]['stat'] = 0  # qi
    op[5]['stat'] = 0

    switch(op[1], 'stat')

    if ks:
        acc['count'] = 0
        afk['time'] = 0
    else:
        afk.update({'stat': 0, 'lock': 0})

    render()


# ===================================< AUTO CLICK CLIP
def acc_switch():
    ks = op[1]['stat']
    acc = op[2]

    switch(op[2], 'stat')

    if acc['mouse'] == 0:
        acc['trigger'] = 0
    else:
        switch(op[2], 'trigger')

    if ks:
        render()

    if acc['stat'] and acc['mode']:
        acc['count'] = 0

    # to use just switch, flip trigger and stat together!


def acc_handler():
    ks = op[1]['stat']
    acc = op[2]

    if ks and acc['stat']:
        switch(acc, 'trigger')
        render()


def acc_prot():
    acc = op[2]

    if acc['stat'] and acc['trigger']:
        if acc['mouse'] == 0:
            key_press(acc['key_action'], 37, 50)
        else:
            m.click(Button.left)

        if acc['mode'] and acc['count'] < 20:
            op[2]['count'] += 1

    if acc['mode'] and acc['trigger'] and acc['count'] >= 20:
        if acc['mouse'] == 1:
            switch(acc, 'stat')
        switch(acc, 'trigger')
        render()
        acc['count'] = 0
    else:
        timeoutNd = random.randint(90, 111) / 1000
        time.sleep(timeoutNd)


# ===================================< SMART AFK
def smartAFK_switch():
    ks = op[1]['stat']
    afk = op[3]['stat']

    switch(op[3], 'stat')

    if afk:
        op[3]['lock'] = 0

    if ks:
        render()


def afk_reset_timer():
    afk = op[3]
    global temp_timer

    minute = 60

    keys = ['w', 'a', 's', 'd']
    interactions = random.randint(2, 6)

    console.print(seperator + f' Keys Auto AFK Sequence')

    for i in range(interactions):
        rand_key = random.randint(0, 3)

        key_press(keys[rand_key], 178, 300)

        timeoutNd = random.randint(178, 300) / 1000
        time.sleep(timeoutNd)

    if afk['stat'] and afk['lock']:
        op[3]['time'] = random.randint(int(2 * minute), int(3.5 * minute))

        render()

        temp_timer = threading.Timer(op[3]['time'], afk_reset_timer)
        temp_timer.start()


def smartAFK_prot():
    afk = op[3]
    global temp_timer

    minute = 60

    if afk['stat'] and not afk['lock']:
        op[3]['lock'] = 1
        op[3]['time'] = random.randint(int(2 * minute), int(3.5 * minute))

        render()

        temp_timer = threading.Timer(op[3]['time'], afk_reset_timer)
        temp_timer.start()
    elif not afk['stat'] and temp_timer and temp_timer.is_alive():
        temp_timer.cancel()
        op[3]['lock'] = 0


# ===================================< QUICK INSERT
def qi_switch():
    ks = op[1]['stat']

    switch(op[4], 'stat')

    if ks:
        render()


def qi_prot():
    qi = op[4]

    text = read_file('essentials/quick insert text.txt')

    if text is None or text == '':
        text = 'Hello There!'

    if qi['stat']:
        render()

        key_press(qi['key_action'], 178, 250)

        for char in text:
            if qi['stat'] == 0:
                break

            key_press(char, 178, 250)

        key_press(Key.enter, 178, 250)

        qi['stat'] = 0

        render()


# ===================================< SAVES SNATCHER
def snt_switch():
    ks = op[1]['stat']
    snt = op[5]

    switch(op[5], 'stat')

    if ks:
        if snt['stat'] and snt['backup_time'] == -1 and snt['dir_files'] == 0:
            if isinstance(snt['path_to'], str) and os.path.exists(snt['path_to']):
                # raw dst name
                dst_name = os.path.basename(snt['path_from'].rstrip('\\/'))
                # edited destination
                dst_path = os.path.join(snt['path_to'], dst_name)
                # recover backup specks
                mtime = dir_mtime(dst_path)
                snt['backup_time'] = mtime if mtime != 0 else -1
                snt['dir_files'] = files_count(dst_path)

        render()


def snt_prot():
    snt = op[5]

    if snt['stat']:
        p_from = snt['path_from']
        p_to = snt['path_to']
        # raw dst name
        dst_name = os.path.basename(p_from.rstrip('\\/'))
        # edited destination
        dst_path = os.path.join(p_to, dst_name)

        if isinstance(p_from, str) and isinstance(p_to, str):
            if os.path.exists(p_from) and os.path.exists(p_to):
                # mtime of the origins
                new_time = dir_mtime(p_from)
                # inner files check
                new_count = files_count(p_from)

                if new_time > snt['backup_time'] and new_count > snt['dir_files']:
                    # slight delay < game has a delay between ~0 to 3 seconds to overwrite
                    time.sleep(3)
                    # delete old backed file
                    if os.path.exists(dst_path):
                        shutil.rmtree(dst_path)
                    # copy creation
                    shutil.copytree(p_from, dst_path, dirs_exist_ok=True)
                    # time update
                    snt['backup_time'] = new_time
                    snt['dir_files'] = new_count
                    render()

            # self_replace - ll replace the backed up, in to original folder
            if snt['self_replace']:
                # check if backup has files
                backup = files_count(dst_path)
                # files count in original folder
                origin = files_count(p_from)
                # mtime check may break, flag may be needed!
                if (not os.path.exists(p_from) or origin == 0 or origin < backup) and (
                        os.path.exists(dst_path) and backup > 0):
                    # slight delay < game may delete files to rewrite < may trigger a loop
                    time.sleep(0.3)
                    # double check files count in original folder
                    origin_del = files_count(p_from)
                    # if folder size stays the same then copy
                    if origin == origin_del:
                        # copy creation
                        shutil.copytree(dst_path, p_from, dirs_exist_ok=True)


# ===================================< CONTROL PANNEL
def control_panel():
    while True:
        if op[1]['stat']:
            acc_prot()
            smartAFK_prot()
            qi_prot()
            snt_prot()


# ===================================< MAIN
def main():
    config_parse(read_file('essentials/config.json'))

    # \/===================================< HOTKEYS SETTINGS
    def mouse_click(x, y, button, pressed):
        if button == Button.left and pressed:
            if op[2]['mouse'] == 0:
                acc_handler()

    hotkeys = [
        HotKey(HotKey.parse(op[1]['key_trigger']), ks_switch),
        HotKey(HotKey.parse(op[2]['key_trigger']), acc_switch),
        HotKey(HotKey.parse(op[3]['key_trigger']), smartAFK_switch),
        HotKey(HotKey.parse(op[4]['key_trigger']), qi_switch),
        HotKey(HotKey.parse(op[5]['key_trigger']), snt_switch),
    ]

    def on_press(key):
        for thing in hotkeys:
            thing.press(key)

    def on_release(key):
        for thing in hotkeys:
            thing.release(key)

    # /\===================================< HOTKEYS SETTINGS

    render()

    with kL(on_press=on_press, on_release=on_release), mL(on_click=mouse_click):
        control_panel()


# ===================================< MAIN START
if __name__ == '__main__':
    main()
