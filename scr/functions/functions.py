from pyfiglet import Figlet


def getInput():
    name = input("Enter your name: ")
    money = input("Enter your deposit amount: ")
    return name, money

def showSplash():
    """
    Display splash screen
    """

    clear_screen()
    title = "Py\n Finance"
    f = Figlet(font="standard")
    print(purple(f.renderText(title)))


def clear_screen():
    """
    Clear the screen
    """
    print("\033c", end="")


def purple(text):
    """
    Make text dark purple
    """
    return "\033[95m" + text + "\033[0m"
