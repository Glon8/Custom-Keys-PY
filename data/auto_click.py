import random
import time

from pynput.mouse import Controller as M, Button

from .values import op
from .helpers import switch, key_press
from .visuals import render

m = M()


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
