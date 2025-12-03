#!framework_env/bin/python3
from core.utils import define_cursor_color, clearConsole, authentification
from core.cmd import mainCmd

def main():
    define_cursor_color("white")
    
    while True:
        clearConsole(False)
        #authentification()
        mainCmd()

    return None


if __name__ == "__main__":
    main()