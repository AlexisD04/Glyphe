from core.menu import mainMenu
from core.utils import quit, clearConsole
from core.tools import TOOLS
import readline

def help():
    with open("core/help.txt") as file:
        print(file.read())
    
    return 0

def clear():
    return 1

DICT_CMD = {
    "simple" : mainMenu,
    "quit" : quit,
    "help" : help,
    "clear" : clear,
}

def init_dict():
    global DICT_CMD
    for tool in TOOLS:
        DICT_CMD[tool.split('_')[0]] = TOOLS[tool]


def completer(text, state):
    options = [cmd for cmd in DICT_CMD if cmd.startswith(text)]
    return options[state]

def mainCmd():
    clearConsole()
    init_dict()

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

    cmd = str()
    try:
        while cmd != "disconnect":
            cmd = input(" >>> ")
            if cmd in DICT_CMD:
                if DICT_CMD[cmd]():
                    clearConsole()
            else:
                print(f" Error: The command \"{cmd}\" doesn't exist.\n")
    except KeyboardInterrupt:
        quit()
    return None