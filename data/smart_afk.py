import random
import threading
import time

from rich.console import Console

from .values import op, _SEPERATOR
from .helpers import switch, key_press
from .visuals import render

console = Console()

temp_timer = None


# ===================================< SMART AFK
def afk_switch():
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

    console.print(_SEPERATOR + f' Keys Auto AFK Sequence')

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


def afk_prot():
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
