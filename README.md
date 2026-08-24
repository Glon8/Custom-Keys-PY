# CustomKeys

Scripts for games, written on python and its libraries. Works mainly on binds over keyboard or mouse.
Mainly build for windows and may work in most of the games, since the core work is through the OS controls.

## DEPENDENCIES

* **python3** - Core
* **rich** - Display
* **pynputs** - Keys binding/listening
* **pyinstaller** - Builds the final app in to executable

## HOW TO RUN

1. Build as it is with ``pyinstaller``, by typing ``pyinstaller --onefile CustomKeys.py``.
2. Copy ``essentials`` folder to directory of the executable.
3. Run the ``CustomKeys.exe`` file.

## GENERAL

Both users and modders use the same 'lazy style' display. Check for key ``key_trigger`` field, to see what bind used to activate every script.
Description for every available right now script and its quirks, you can find in **SETTINGS** chapter.

## SETTINGS

* Config files will be created in ``essentials`` folder in the same directory.
* All the description of existing scripts and their options will be below, while ``stat`` displays the state of the scripts.
* **Adjust to your needs:** 
  * ``0`` OFF
  * ``1`` ON

## FIELDS DESCRIPTION

1. **General** - general settings.
   * ``display`` Changes between plain text and emojis of the toggles(due the display in console, not every consoles can use emoji).
2. **Kill Switch** - Switches on and off the entire script.
3. **Auto Click Clip** - Clicker, by default will click 20 times on given action key on keyboard.
   * ``mode`` Switches between 20 clicks and infinite clicks(by default ON, if set on OFF, it wont wait for users signal).
   * ``mouse`` Switches between LMB clicks and Keyboard clicks(by default OFF, check action key for keyboard clicks).
   * ``trigger`` Displays if script got users signal or not.
   * ``count`` Counts clicks made by clicker, wont work if mode is OFF(infinite).
4. **Smart AFK** - Fakes your presence in a game, if turned ON, will press random keys on W,A,S,D every few minutes.
   * ``lock`` Shows if script is set, will switch to ON as the scripts works.
   * ``time`` Shows the time until the next action.
5. **Quick Insert** - Presses the keys from the ``quick_insert_text.txt`` after ``key_action``, as you use the bind(used to push stuff in to games chat).
6. **Saves Snatcher** - Looks for the ``path_from`` folder and for any updates copies in to ``path_to`` folder(used to make copies of "Hardcore" games with saves delete).
   * ``backup time`` It will display the date of the last update(for the backup files that you HAVE).
   * ``dir files`` Amount files in the backup directory.
   * ``self replace`` If ON, copies files from backup to original folder, if original miss files or deleted completely.

## HOW TO ADD CUSTOM SCRIPTS

1. Open the ``CustomKeys.py`` file, and scroll down till ``Control Pannel``.
2. For basic use, you must create two functions, ``[your_app_name]-switch`` and ``[your_app_name]-prot``.
3. ``[your_app_name]`` prot, must go to ``ControlPannel`` loop.
4. ``[your_app_name]`` switch, goes to ``Main -> Hotkeys`` section.
5. All the values and display written in operations list, so keep in mind, that all what you write there will be displayed. You can configure the display by tag in render function.
6. Add a copy of your values from ``operations`` list to ``config.json`` to be able to modify them, with just a simple text document.
7. After updating the script, you can build the program with ``pyinstaller`` library, by typing in terminal ``pyinstaller --onefile CustomKeys.py``.
8. Copy ``essentials`` folder to directory of the executable.
9. Run the ``CustomKeys.exe``.