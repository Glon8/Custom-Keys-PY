_TEMPLATE = [
    'Hello beautiful',
    'Looking extra sharp today',
]

_OPERATIONS = [
    {
        'name': 'General',
        'note': "display is either 'emoji' or 'plain'",
        'display': 'plain'
    },
    {
        'name': 'Kill Switch',
        'key_trigger': 'c+0',
        'stat': 0,
    },
    {
        'name': 'Auto Click Clip',
        'key_trigger': 'c+1',
        'stat': 0,
        'key_action': 'v',
        'mode': 1,
        'mouse': 0,
        'trigger': 0,
        'count': 0,
    },
    {
        'name': 'Smart AFK',
        'key_trigger': 'c+2',
        'stat': 0,
        'lock': 0,
        'time': 0,
    },
    {
        'name': 'Quick Insert',
        'key_trigger': 'c+3',
        'stat': 0,
        'key_action': 't',
    },
    {
        'name': 'Saves Snatcher',
        'key_trigger': 'c+4',
        'stat': 0,
        'path_from': '',
        'path_to': 'data/snatched files',
        'backup_time': -1,
        'dir_files': 0,
        'self_replace': 0,
    },
]

_SEPERATOR = f"===========================<"

op = _OPERATIONS
seperator = _SEPERATOR


def getTm():
    return _TEMPLATE


def setTm(value):
    global _TEMPLATE

    if isinstance(value, list) and value:
        _TEMPLATE = value
