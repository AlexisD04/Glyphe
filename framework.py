#!framework_env/bin/python3
from core.utils import define_cursor_color, clearConsole, authentification
from core.menu import mainMenu

def main():
    define_cursor_color("white")
    clearConsole(False)

    authentification()

    mainMenu()

    return None


if __name__ == "__main__":
    main()