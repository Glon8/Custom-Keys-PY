from .helpers import switch
from .values import op
from .visuals import render


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
