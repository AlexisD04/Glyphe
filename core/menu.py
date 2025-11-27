from core.config import *
from core.utils import clearConsole, print_colored, quit
from core.tools import toolSetAccess, toolSetEnumeration, toolSetReconnaissance, toolSetScanning, toolSetVulnerability

def getChoice(menu,text="Your action"):
    max_value = len(menu)-1
    while(True):
        try:
            clearConsole()
            printMenu(menu)
            choice = int(input(f"\n {text}:"))
            if 0 <= choice <= max_value:
                return choice
            else:
                clearConsole()
                print_colored(f" Please enter a number between 0 and {max_value}.\n", "red")
            
        except ValueError:
            clearConsole()
            print_colored(" Please enter a valid integer.\n", "red")

        except KeyboardInterrupt:
            quit()


def printMenu(menu):
    for i in range(len(menu)):
        print(f" {i}. {menu[i][0]}")

    return None

def mainMenu():
    while True:
        menu = [
            ("Reconnaissance / Footprint", toolSetReconnaissance),
            ("Scanning network", toolSetScanning),
            ("Enumeration", toolSetEnumeration),
            ("Vulnerability analysis", toolSetVulnerability),
            ("Gaining access", toolSetAccess),
            ("Leave", [])
        ]

        choice = getChoice(menu)

        if choice == len(menu)-1:
            quit()
            return None

        menu = menu[choice][1]
        choice = -1

        while choice != len(menu)-1:
            choice = getChoice(menu)
            menu[choice][1]()

    return None