from pynput.keyboard import Key

from .values import op
from .helpers import switch, key_press, read_file
from .visuals import render


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
