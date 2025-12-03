from pywebcopy import save_website, save_webpage
from core.utils import quit, clearConsole, delete_lines
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))
DIR = path.join(BASE_DIR, "..", "..", "..", "data", "guest", "web")

def webcopy_tool():
    choix = 0
    try:
        while(choix != 3):
            clearConsole(False)
            print_webcopy_logo()
            print("\n 1. Web page copy")
            print(" 2. Website copy")
            print(" 3. Quit")

            choix = input("\n What do you want to do?:")

            if choix in ["1","2"]:
                copy(int(choix))

            elif choix == "3":
                return None

            else:
                clearConsole(False)
                print_webcopy_logo()

    except KeyboardInterrupt:
        quit()

    return None

def copy(choix):
    print()
    try:
        url = input(" URL:")
        project_folder=DIR
        project_name = input(" Save as:")


        bypass_robots = input(" Bypass robots(Y/N)?")
        while bypass_robots not in ["Y", "y", "YES", "Yes", "yes", "N", "n", "NO", "No", "no"]:
            delete_lines()
            bypass_robots = input(" Bypass robots(Y/N)?")

        if bypass_robots[0] == 'Y' or bypass_robots[0] == 'y':
            bypass_robots = True
        else:
            bypass_robots = False


        debug = False
        open_in_browser=False

        delay = input(" Delay (in ms):")
        try:
            delay = int(delay)
        except:
            pass
        while type(delay) != int:
            delete_lines()
            delay = input(" Delay (in ms):")
            try:
                delay = int(delay)
            except:
                pass
        delay = int(delay)

        threaded = False

    except KeyboardInterrupt:
        quit()

    if choix == 1:
        save_webpage(url,project_folder,project_name,bypass_robots,debug,open_in_browser,delay,threaded)
        print(f" Web page saved.")

    else:
        save_website(url,project_folder,project_name,bypass_robots,debug,open_in_browser,delay,threaded)
        print(f" Website saved")

    input(" Leave?")


def print_webcopy_logo():
    print(r"          _______  ______     _______  _______  _______          ")
    print(r"|\     /|(  ____ \(  ___ \   (  ____ \(  ___  )(  ____ )|\     /|")
    print(r"| )   ( || (    \/| (   ) )  | (    \/| (   ) || (    )|( \   / )")
    print(r"| | _ | || (__    | (__/ /   | |      | |   | || (____)| \ (_) / ")
    print(r"| |( )| ||  __)   |  __ (    | |      | |   | ||  _____)  \   /  ")
    print(r"| || || || (      | (  \ \   | |      | |   | || (         ) (   ")
    print(r"| () () || (____/\| )___) )  | (____/\| (___) || )         | |   ")
    print(r"(_______)(_______/|/ \___/   (_______/(_______)|/          \_/   ")
    
    return None