from pynput.mouse import Controller as M, Listener as mL, Button
from pynput.keyboard import Controller as K, Listener as kL, HotKey

from data.values import op
from data.visuals import render
from data.helpers import config_parse, read_file
from data.killswitch import ks_switch
from data.auto_click import acc_prot, acc_switch, acc_handler
from data.smart_afk import afk_switch, afk_prot
from  data.quick_insert import qi_prot, qi_switch
from data.snatcher import snt_switch, snt_prot

k = K()
m = M()

# ===================================< CONTROL PANNEL
def control_panel():
    while True:
        if op[1]['stat']:
            acc_prot()
            afk_prot()
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
        HotKey(HotKey.parse(op[3]['key_trigger']), afk_switch),
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
