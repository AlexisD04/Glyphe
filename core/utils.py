import time,hashlib,os
from core.config import *
from getpass import getpass
from os import system

# Se connecter
def authentification():
    print_colored(" Launching pentesting framework...")
    print_colored(" Authentification")
    print_colored("\n (Try guest:guest)")

    is_connected = False
    try:
        while(not is_connected):
            is_connected = True
            user = input(" username:")
            if user not in users:
                time.sleep(0.1)
                print_colored(" Error: user does not exist.\n")
                is_connected = False

            else:
                password = getpass(" password:")
                if hashlib.sha256(password.encode()).hexdigest() != users[user]:
                    time.sleep(0.1)
                    print_colored(" Error: user's password is wrong.\n")
                    is_connected = False

        clearConsole()
        print_colored(f" Access authorized\n Welcome {user}\n")
        return None
    
    except KeyboardInterrupt:
        quit()

# Changer couleur curseur
def define_cursor_color(color=DEFAULT_CURSOR_COLOR):
    print(COLORS_CURSOR[color],end="")
    return None

# Vide la console
def clearConsole(display=True):
    os.system('clear')
    if display: print_logo()
    return None

# Affiche le logo
def print_logo():
    print_colored(" ########################")
    print_colored(" # PENTESTING FRAMEWORK #")
    print_colored(" ########################\n")
    return None

# Imprime avec couleurs
def print_colored(message, color=main_color):
    print(f"{COLORS.get(color, COLORS[main_color])}{message}{COLORS[main_color]}")
    return None

# Ferme le framework
def quit():
    define_cursor_color()
    system('clear')
    exit(0)
    return None