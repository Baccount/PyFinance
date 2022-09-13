from argm.argms import arguments
from classes.mclass import Finance
from classes.rclass import ReadFinances
from classes.sclass import SaveFinances
from functions.functions import getInput

def main():
    arg = arguments()
    finance = Finance(arg.name, arg.age, arg.money) if arg.name and arg.money else None
    if not finance:
        finance = getInput()
    SaveFinances().save(finance)
    print(ReadFinances().getFinance())


if __name__ == "__main__":
    main()
