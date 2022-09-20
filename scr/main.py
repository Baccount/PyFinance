from argm.argms import arguments
from classes.mclass import Finance
from functions.functions import getInput, showSplash


def main():
    while True:
        arg = arguments()
        finance = Finance(arg.name, arg.money) if arg.name and arg.money else None
        if not finance:
            showSplash()
            finance = getInput()
            
        input("Press enter to continue...")

def askUsr():
    usr = input("Do you want to continue? (y/n): ")
    return usr


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
